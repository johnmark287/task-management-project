# Generated by Django 5.1.6 on 2025-03-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'To Do'), ('In Progress', 'IN_PROGRESS'), ('COMPLETED', 'Completed')], default='TODO', max_length=20),
        ),
    ]
