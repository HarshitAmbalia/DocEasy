# Generated by Django 3.1.5 on 2022-03-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploaded_DocDetails',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('fileName', models.CharField(max_length=1000)),
                ('filePath', models.CharField(max_length=4000)),
                ('typrOfFile', models.CharField(max_length=500)),
                ('uploadedTime', models.DateTimeField(auto_now_add=True)),
                ('UserName', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
