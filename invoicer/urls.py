from django.urls import path

from . import views

app_name = 'invoicer'


urlpatterns = [
    # ex: /invoicer/
    path('', views.index, name='index'),

    # ex: /invoicer/client/5/
    path('client/<int:client_id>/', views.client, name='client'),

    # ex: /invoicer/client_group/5/
    path('client_group/<int:client_group_id>/', views.client_group, name='client_group'),

    # ex: /invoicer/project/5/
    path('project/<int:project_id>/', views.project, name='project'),

    # ex: /invoicer/task/5/
    path('task/<int:task_id>/', views.task, name='task'),

    # ex: /invoicer/invoice/5/
    path('invoice/<int:invoice_id>/', views.invoice, name='invoice'),

    # ex: /invoicer/work/5/
    path('work/<int:work_id>/', views.work, name='work'),
]
