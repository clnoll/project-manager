from django import forms

from invoicer.models.models import Task


class TaskForm(forms.ModelForm):

  class Meta:
    model = Task
    fields = "__all__"
