from django import forms

from invoicer.models.models import Project


class ProjectForm(forms.ModelForm):

  class Meta:
    model = Project
    fields = "__all__"

    
