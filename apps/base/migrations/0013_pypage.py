# Generated by Django 2.2.4 on 2019-09-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_pycompany_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Nombre')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('keywords', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
