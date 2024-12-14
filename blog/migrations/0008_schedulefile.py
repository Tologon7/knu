# Generated by Django 5.1.2 on 2024-12-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_delete_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='schedules/')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]