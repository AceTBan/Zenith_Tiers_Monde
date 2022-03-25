# Generated by Django 3.2.12 on 2022-03-25 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.CharField(max_length=50)),
                ('name_contact', models.CharField(max_length=50)),
                ('mail_contact', models.CharField(max_length=50)),
                ('pub_date', models.DateField(verbose_name='Date de publication')),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='firstname_user',
        ),
        migrations.RemoveField(
            model_name='users',
            name='mail_user',
        ),
        migrations.RemoveField(
            model_name='users',
            name='name_user',
        ),
        migrations.RemoveField(
            model_name='users',
            name='pwd_user',
        ),
        migrations.AddField(
            model_name='users',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
