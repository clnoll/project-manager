from django import forms

from invoicer.models import Invoice, TaskItem


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = "__all__"

    def save(self, project, *args, **kwargs):
        invoice = super().save(*args, **kwargs)
        task_item_ids = [int(k.lstrip('task_item_')) for k in self.data.dict().keys() if 'task_item_' in k]
        TaskItem.objects.filter(pk__in=task_item_ids).update(invoice_id=invoice.id)
        return invoice
