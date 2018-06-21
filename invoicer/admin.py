from django.contrib import admin

from .models import (Client,
                     ClientGroup,
                     Invoice,
                     Project,
                     ProjectStatus,
                     ProjectType,
                     Task,
                     TaskItem,
                     TaskStatus,
                     TaskType)


admin.site.register(Client)
admin.site.register(ClientGroup)
admin.site.register(Invoice)
admin.site.register(Project)
admin.site.register(ProjectStatus)
admin.site.register(ProjectType)
admin.site.register(Task)
admin.site.register(TaskItem)
admin.site.register(TaskStatus)
admin.site.register(TaskType)
