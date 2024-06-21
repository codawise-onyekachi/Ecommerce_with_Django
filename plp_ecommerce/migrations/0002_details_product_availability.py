# Generated by Django 5.0.6 on 2024-06-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plp_ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]