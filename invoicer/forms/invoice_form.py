import re
from collections import defaultdict
from datetime import datetime

from django import forms
from django.db import transaction

from invoicer.models.models import Invoice, Task, TaskItem


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = "__all__"

    def save(self, project, *args, **kwargs):
        import ipdb ; ipdb.set_trace()
        invoice = super().save(*args, **kwargs)

        data = self.data.dict()
        task_names_to_update = {int(k.lstrip('task_name_')): v for k, v in data.items()
                                if 'task_name_' in k}

        taskitems_to_update = defaultdict(dict)

        for k, v in data.items():
            if 'taskitem_' in k:
                pattern = r'taskitem_([a-z0-9_]*)_([0-9]*)'
                taskitem = re.match(pattern, k)
                if taskitem:
                    key, taskitem_id = taskitem.groups()
                    taskitems_to_update[int(taskitem_id)][key] = v

        taskitem_ids_to_invoice = [int(k.lstrip('invoice_')) for k in data.keys()
                                   if 'invoice_' in k]

        with transaction.atomic():
            for task_id, task_name in task_names_to_update.items():
                task = Task.objects.get(pk=task_id)
                if task:
                    task.name = task_name
                    task.save()

            for taskitem_id, taskitem_kvs in taskitems_to_update.items():
                taskitem = TaskItem.objects.get(pk=taskitem_id)
                if taskitem:
                    for k, v in taskitem_kvs.items():
                        if hasattr(taskitem, k):
                            setattr(taskitem, k, v)
                taskitem.save()

            TaskItem.objects.filter(pk__in=taskitem_ids_to_invoice).update(invoice_id=invoice.id)

        return invoice
