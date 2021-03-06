# Generated by Django 4.0.2 on 2022-02-01 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pro_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('softwareUsed', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
                ('imageSS1', models.ImageField(blank=True, default='', null=True, upload_to='image/')),
                ('imageSS2', models.ImageField(blank=True, default='', null=True, upload_to='image/')),
                ('imageSS3', models.ImageField(blank=True, default='', null=True, upload_to='image/')),
                ('imageSS4', models.ImageField(blank=True, default='', null=True, upload_to='image/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.category')),
            ],
        ),
    ]
