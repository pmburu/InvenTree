# Generated by Django 3.0.5 on 2020-05-12 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0033_auto_20200512_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseorderattachment',
            name='upload_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='salesorderattachment',
            name='upload_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]