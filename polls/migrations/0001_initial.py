# Generated by Django 5.0.4 on 2024-04-21 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ToDoListText', models.CharField(max_length=200)),
                ('ToDoListDeadLine', models.DateTimeField()),
                ('ToDoListCheckedOut', models.BooleanField(default=False)),
            ],
        ),
    ]
