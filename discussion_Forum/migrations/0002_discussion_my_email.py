# Generated by Django 3.1.5 on 2021-01-10 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussion_Forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='my_email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]