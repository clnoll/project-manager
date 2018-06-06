from django import forms

from invoicer.models import Work


class WorkForm(forms.ModelForm):

  class Meta:
    model = Work
    fields = "__all__"
