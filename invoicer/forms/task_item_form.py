from django import forms

from invoicer.models.models import TaskItem


class TaskItemForm(forms.ModelForm):

  class Meta:
    model = TaskItem
    fields = "__all__"
