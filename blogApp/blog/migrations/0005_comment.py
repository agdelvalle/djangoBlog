# Generated by Django 2.2 on 2021-10-24 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogentry_publishdate'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500, verbose_name='Comment')),
                ('userCom', models.CharField(max_length=500, verbose_name='commenterName')),
                ('commDate', models.DateField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogEntry', verbose_name='blogEntry')),
            ],
        ),
    ]
