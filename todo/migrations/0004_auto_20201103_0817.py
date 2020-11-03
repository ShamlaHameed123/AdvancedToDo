# Generated by Django 3.1.2 on 2020-11-03 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20201103_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='content',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(default='hi this is a task', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]