# Generated by Django 5.0 on 2024-01-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_add'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='index/img')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
