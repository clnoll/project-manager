from django import forms

from invoicer.models.models import Client


class ClientForm(forms.ModelForm):

  class Meta:
    model = Client
    fields = "__all__"
