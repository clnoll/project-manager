from django import forms

from invoicer.models import Invoice, Work


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = "__all__"

    def save(self, project, *args, **kwargs):
        invoice = super().save(*args, **kwargs)
        work_ids = [int(k.lstrip('work_')) for k in self.data.dict().keys() if 'work_' in k]
        Work.objects.filter(pk__in=work_ids).update(invoice_id=invoice.id)
        return invoice
