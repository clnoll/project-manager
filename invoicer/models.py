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
    primary_phone = models.CharField(max_length=50)
    secondary_phone = models.CharField(max_length=50, null=True)


class ClientGroup(BaseModel):
    clients = models.ManyToManyField(Client)

    description = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=200, null=True)

    
class ProjectStatus(BaseModel):
    description = models.CharField(max_length=1000)


class ProjectType(BaseModel):
    description = models.CharField(max_length=1000)

    
class Project(BaseModel):
    client_group = models.ForeignKey(ClientGroup, on_delete=models.CASCADE)
    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=200)
    start = models.DateTimeField(null=True)


class TaskStatus(BaseModel):
    description = models.CharField(max_length=1000)


class TaskType(BaseModel):
    default_cost = models.FloatField(null=True)
    description = models.CharField(max_length=1000)


class Task(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(TaskType, on_delete=models.CASCADE, null=True)

    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    start = models.DateTimeField(null=True)


class InvoiceStatus(BaseModel):
    description = models.CharField(max_length=1000)


class Invoice(BaseModel):
    status = models.ForeignKey(InvoiceStatus, on_delete=models.CASCADE, null=True)

    amount_paid = models.FloatField(null=True)
    date_sent = models.DateTimeField(null=True)
    date_paid = models.DateTimeField(null=True)
    description = models.CharField(max_length=1000, null=True)
    total = models.FloatField(null=True)


class Work(BaseModel):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)

    description = models.CharField(max_length=1000)
    end_time = models.DateTimeField(null=True)
    minutes_billed = models.IntegerField(null=True)
    rate = models.FloatField(null=True)
    start_time = models.DateTimeField(null=True)
