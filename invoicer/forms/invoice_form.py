from django import forms

from invoicer.models import Invoice


class InvoiceForm(forms.ModelForm):

  class Meta:
    model = Invoice
    fields = "__all__"
