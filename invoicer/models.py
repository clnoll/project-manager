from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    def __str__(self):
        return str(self.__dict__)


class Client(BaseModel):
    email = models.CharField(max_length=200)
    is_primary = models.BooleanField()
    name = models.CharField(max_length=200)
    primary_phone = models.CharField(max_length=50, default='', blank=True)
    secondary_phone = models.CharField(max_length=50, default='', blank=True)


class ClientGroup(BaseModel):
    clients = models.ManyToManyField(Client)

    description = models.CharField(max_length=1000, default='')
    name = models.CharField(max_length=200, default='')

    
class ProjectStatus(BaseModel):
    description = models.CharField(max_length=1000, default='')


class ProjectType(BaseModel):
    description = models.CharField(max_length=1000, default='')

    
class Project(BaseModel):
    client_group = models.ForeignKey(ClientGroup, on_delete=models.CASCADE)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=200)
    start = models.DateTimeField(null=True, blank=True)


class TaskStatus(BaseModel):
    description = models.CharField(max_length=1000, default='')


class TaskType(BaseModel):
    default_cost = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=1000, default='')


class Task(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, null=True, blank=True)
    type = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=True, blank=True)

    description = models.CharField(max_length=1000, default='')
    name = models.CharField(max_length=200)
    start = models.DateTimeField(null=True, blank=True)


class InvoiceStatus(BaseModel):
    description = models.CharField(max_length=1000)


class Invoice(BaseModel):
    status = models.ForeignKey(InvoiceStatus, on_delete=models.CASCADE, null=True, blank=True)

    amount_paid = models.FloatField(null=True, blank=True)
    date_sent = models.DateTimeField(null=True, blank=True)
    date_paid = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=1000, default='')
    total = models.FloatField(null=True, blank=True)


class TaskItem(BaseModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    description = models.CharField(max_length=1000, default='')
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    minutes_billed = models.IntegerField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
