import csv

# from django.db import connection
from django.apps import apps
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from invoicer.forms import (client_form,
                            client_group_form,
                            project_form,
                            task_form,
                            invoice_form,
                            work_form)
from invoicer.models import (Client,
                             ClientGroup,
                             Project,
                             Task,
                             Invoice,
                             Work)
from invoicer.utils import sqlite_utils


def _get_object(request, object_cls, object_id):
    try:
        obj = object_cls.objects.get(pk=object_id)
    except object_cls.DoesNotExist:
        raise Http404("{} does not exist".format(obj_cls.__name__))
    else:
        return obj


def _post_form(request, form_cls, redirect_fn_name, form_name):
    if request.method == 'POST':
        form = form_cls(request.POST)
        if form.is_valid():
            obj = form.save()
            HttpResponseRedirect(reverse('invoicer:{}'.format(redirect_fn_name), args=(obj.id,)))

    else:
        form = form_cls()

    return render(request, 'invoicer/{}.html'.format(form_name), {'form': form})


def index(request):
    latest_project_list = Project.objects.all()[:5]
    context = {
        'latest_project_list': latest_project_list,
    }
    return render(request, 'invoicer/index.html', context)


def get_client(request, client_id):
    return render(request,
                  'invoicer/client.html',
                  {'client': _get_object(request, Client, client_id)})


def create_client(request):
    return _post_form(request, client_form.ClientForm, 'get_client', 'client_form')


def get_client_group(request, client_group_id):
    return render(request,
                  'invoicer/client_group.html',
                  {'client_group': _get_object(request, ClientGroup, client_group_id)})


def create_client_group(request):
    return _post_form(request, client_group_form.ClientGroupForm, 'get_client_group', 'client_group_form')


def get_project(request, project_id):
    return render(request,
                  'invoicer/project.html',
                  {'project': _get_object(request, Project, project_id)})


def create_project(request):
    return _post_form(request, project_form.ProjectForm, 'get_project', 'project_form')


def get_task(request, task_id):
    return render(request,
                  'invoicer/task.html',
                  {'task': _get_object(request, Task, task_id)})


def create_task(request):
    return _post_form(request, task_form.TaskForm, 'get_task', 'task_form')


def get_invoice(request, invoice_id):
    return render(request,
                  'invoicer/invoice.html',
                  {'invoice': _get_object(request, Invoice, invoice_id)})


def create_invoice(request, project_id):
    [project] = Project.objects.filter(id=project_id)
    tasks = Task.objects.filter(project_id=project_id)
    works = Work.objects.filter(task_id__project_id=project_id)

    if request.method == 'POST':
        form = invoice_form.InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(works)
        return render(request,
                      'invoicer/printable_invoice.html',
                      {'invoice': invoice, 'project': project, 'tasks': tasks})

    else:
        return render(request,
                      'invoicer/invoice_form.html',
                      {'project': project, 'tasks': tasks})


def get_work(request, work_id):
    return render(request,
                  'invoicer/work.html',
                  {'work': _get_object(request, Work, work_id)})


def create_work(request):
    return _post_form(request, work_form.WorkForm, 'get_work', 'work_form')


def export_db(request):
    import ipdb ; ipdb.set_trace()
    models = apps.all_models['invoicer']
    for model in models.values():
        filename = "{}_{}".format(datetime.now().strftime("%Y%m%d_%H%M%S"))
        objs = model.objects.all()
        
    # with connection.cursor() as cursor:
    #     tables = cursor.execute(sqlite_utils.LIST_TABLES);
    #     # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
    #     # cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
    #     # row = cursor.fetchone()

    # return render(request, 'invoicer/backup_complete.html')
