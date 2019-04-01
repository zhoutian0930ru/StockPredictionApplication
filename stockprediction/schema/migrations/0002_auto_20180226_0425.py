# Generated by Django 2.0.2 on 2018-02-26 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstockdata',
            name='stock_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schema.Stocks'),
        ),
        migrations.AlterField(
            model_name='password',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='schema.Users'),
        ),
        migrations.AlterField(
            model_name='recentstockdata',
            name='stock_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schema.Stocks'),
        ),
        migrations.AlterField(
            model_name='userstockdata',
            name='stock_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schema.Stocks'),
        ),
        migrations.AlterField(
            model_name='userstockdata',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schema.Users'),
        ),
    ]