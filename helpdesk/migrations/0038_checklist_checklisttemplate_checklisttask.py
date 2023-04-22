# Generated by Django 4.2 on 2023-04-22 20:50

from django.db import migrations, models
import django.db.models.deletion
import helpdesk.models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0037_alter_queue_email_box_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checklists', to='helpdesk.ticket', verbose_name='Ticket')),
            ],
            options={
                'verbose_name': 'Checklist',
                'verbose_name_plural': 'Checklists',
            },
        ),
        migrations.CreateModel(
            name='ChecklistTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('task_list', models.JSONField(validators=[helpdesk.models.is_a_list_without_empty_element], verbose_name='Task List')),
            ],
            options={
                'verbose_name': 'Checklist Template',
                'verbose_name_plural': 'Checklist Templates',
            },
        ),
        migrations.CreateModel(
            name='ChecklistTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=250, verbose_name='Description')),
                ('completion_date', models.DateTimeField(blank=True, null=True, verbose_name='Completion Date')),
                ('checklist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='helpdesk.checklist', verbose_name='Checklist')),
            ],
            options={
                'verbose_name': 'Checklist Task',
                'verbose_name_plural': 'Checklist Tasks',
            },
        ),
    ]
