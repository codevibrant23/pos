# Generated by Django 4.2.5 on 2024-12-08 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0013_stockrequest_outlet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='v1.order'),
        ),
    ]