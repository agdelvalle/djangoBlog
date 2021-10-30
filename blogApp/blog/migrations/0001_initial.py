# Generated by Django 2.2 on 2021-10-10 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=200, verbose_name='Title')),
                ('blogBody', models.CharField(max_length=10000, verbose_name='Body Text')),
                ('publishDate', models.CharField(max_length=20, verbose_name='Body Text')),
            ],
        ),
    ]
