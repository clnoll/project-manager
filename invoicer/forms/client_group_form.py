from django import forms

from invoicer.models.models import ClientGroup


class ClientGroupForm(forms.ModelForm):

  class Meta:
    model = ClientGroup
    fields = "__all__"
