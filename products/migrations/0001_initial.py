# Generated by Django 2.0.3 on 2018-03-17 12:19

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(choices=[('YE', 'Yellow'), ('GR', 'Green'), ('BL', 'Black'), ('WH', 'White')], default='BL', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('in_stock', models.IntegerField(default=0)),
                ('description', models.CharField(choices=[(models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Color'), 'color'), (models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Weight'), 'Weight')], default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Color'), max_length=300)),
                ('COLOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Color')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight_name', models.CharField(choices=[('1K', '1kg'), ('2K', '2kg'), ('3K', '3kg'), ('4K', '4kg')], default='1K', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='WEIGHT',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Weight'),
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
