# Generated by Django 4.0.6 on 2022-07-15 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('catDesc', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('manDesc', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('proDesc', models.TextField(max_length=128)),
                ('price', models.PositiveBigIntegerField()),
                ('rating', models.PositiveSmallIntegerField()),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('man', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('Bought_on', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='users.profile')),
            ],
        ),
    ]
