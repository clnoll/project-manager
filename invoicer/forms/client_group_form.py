from django import forms

from invoicer.models import ClientGroup


class ClientGroupForm(forms.ModelForm):

  class Meta:
    model = ClientGroup
    fields = "__all__"
