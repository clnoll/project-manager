# Generated by Django 2.0.5 on 2018-05-19 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BaseInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BaseProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='BaseTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='BaseWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('baseclient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseClient')),
                ('email', models.CharField(max_length=200)),
                ('is_primary', models.BooleanField()),
                ('name', models.CharField(max_length=200)),
                ('primary_phone', models.CharField(max_length=50)),
                ('secondary_phone', models.CharField(max_length=50)),
            ],
            bases=('invoicer.baseclient',),
        ),
        migrations.CreateModel(
            name='ClientGroup',
            fields=[
                ('baseclient_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseClient')),
                ('description', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('clients', models.ManyToManyField(to='invoicer.Client')),
            ],
            bases=('invoicer.baseclient',),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('baseinvoice_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseInvoice')),
                ('amount_paid', models.FloatField()),
                ('date_sent', models.DateTimeField()),
                ('date_paid', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('total', models.FloatField()),
            ],
            bases=('invoicer.baseinvoice',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('baseproject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseProject')),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateTimeField()),
                ('client_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicer.ClientGroup')),
            ],
            bases=('invoicer.baseproject',),
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('baseproject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseProject')),
            ],
            bases=('invoicer.baseproject',),
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('baseproject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseProject')),
            ],
            bases=('invoicer.baseproject',),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('basetask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseTask')),
                ('name', models.CharField(max_length=200)),
                ('start', models.DateTimeField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicer.Project')),
            ],
            bases=('invoicer.basetask',),
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('basetask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseTask')),
            ],
            bases=('invoicer.basetask',),
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('basetask_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseTask')),
                ('default_cost', models.FloatField()),
            ],
            bases=('invoicer.basetask',),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('basework_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invoicer.BaseWork')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('minutes_billed', models.IntegerField()),
                ('rate', models.FloatField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicer.Invoice')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicer.Task')),
            ],
            bases=('invoicer.basework',),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicer.TaskStatus'),
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicer.TaskType'),
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicer.ProjectStatus'),
        ),
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoicer.ProjectType'),
        ),
    ]
