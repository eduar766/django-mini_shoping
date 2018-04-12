# Generated by Django 2.0.3 on 2018-03-18 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('in_stock', models.IntegerField(default=0)),
                ('color_name', models.CharField(choices=[('YE', 'Yellow'), ('GR', 'Green'), ('BL', 'Black'), ('WH', 'White')], default='BL', max_length=50)),
                ('weight_name', models.CharField(choices=[('1K', '1kg'), ('2K', '2kg'), ('3K', '3kg'), ('4K', '4kg')], default='1K', max_length=50)),
                ('description', models.TextField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='products',
            name='COLOR',
        ),
        migrations.RemoveField(
            model_name='products',
            name='WEIGHT',
        ),
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.DeleteModel(
            name='Color',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='Weight',
        ),
    ]
