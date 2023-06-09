# Generated by Django 4.2.1 on 2023-06-04 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(1, 'masculine'), (2, 'feminine')], default=1, verbose_name='gender')),
                ('mark', models.CharField(max_length=30, verbose_name='shoes mark')),
                ('size', models.PositiveIntegerField(default=35, verbose_name='size')),
                ('color', models.CharField(max_length=30, verbose_name='color')),
                ('isAvailable', models.BooleanField(default=True, verbose_name='is available')),
                ('price', models.PositiveBigIntegerField(default=100000, verbose_name='price')),
                ('discpunt', models.CharField(max_length=10, verbose_name='discount')),
                ('count', models.PositiveIntegerField(blank=True, null=True, verbose_name='count')),
                ('discription', models.TextField(blank=True, max_length=500)),
                ('categoryImage', models.ImageField(upload_to='shoes/', verbose_name='image')),
                ('createdTime', models.DateTimeField(auto_now=True, verbose_name='created time')),
                ('updatedTime', models.DateTimeField(auto_now_add=True, verbose_name='updated time')),
            ],
            options={
                'verbose_name': 'shoes',
                'verbose_name_plural': 'shoes',
                'db_table': 'shoes',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('text', models.TextField(max_length=700, verbose_name='text')),
                ('like', models.BooleanField(help_text='true means you liked the shoes and false means you did not lik the shoes.', null=True)),
                ('createdTime', models.DateTimeField(auto_now=True, verbose_name='created time')),
                ('updatedTime', models.DateTimeField(auto_now_add=True, verbose_name='updated time')),
                ('shoes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shoes', to='shoesMarket.shoesmodel')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'db_table': 'comments',
            },
        ),
    ]
