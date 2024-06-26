# Generated by Django 5.0.6 on 2024-05-15 09:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myare', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='safar',
            options={'verbose_name_plural': 'جدول سفرهای تک'},
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.CharField(max_length=20, verbose_name='زمان شروع درخواست')),
                ('accept', models.CharField(default='', max_length=20, verbose_name='زمان قبول درخواست')),
                ('end_time', models.CharField(max_length=20, verbose_name='زمان پایان درخواست')),
                ('origin_location_lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='عرض جغرافیایی مبدا')),
                ('origin_location_lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='طول جغرافیایی مبدا')),
                ('navgan_type', models.CharField(choices=[('motor', 'موتور'), ('vanet', 'وانت'), ('kamion', 'کامیون')], max_length=60, verbose_name='نوع ناوگان')),
                ('first_cost', models.IntegerField(verbose_name='کرایه پایه')),
                ('final_cost', models.IntegerField(verbose_name='کرایه نهایی')),
                ('state', models.CharField(choices=[('start', 'شروع'), ('moatl', 'معطل'), ('cancel', 'باطل'), ('rej', 'رد شده'), ('conf', 'تایید شده'), ('success', 'موفق'), ('laghv', 'لغو'), ('done', 'پرداخت شده')], default='-', max_length=30, verbose_name='وضعیت سفر')),
                ('description', models.CharField(max_length=60, verbose_name='توضیحات')),
                ('peik_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myare.peik', verbose_name='ناوگان')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'جدول سفرهای ترکیبی',
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='نام گیرنده')),
                ('phone', models.IntegerField(verbose_name='تلفن گیرنده')),
                ('packagecode', models.CharField(default='-', max_length=30, verbose_name='کدبار')),
                ('state', models.CharField(choices=[('start', 'شروع شده'), ('deliv', 'تحویل شده'), ('return', 'برگشته'), ('cancel', 'باطل'), ('other', 'سایر')], default='-', max_length=30, verbose_name='وضعیت تحویل')),
                ('delivery_v_code', models.IntegerField()),
                ('location_lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='عرض جغرافیایی مقصد')),
                ('location_lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='طول جغرافیایی مقصد')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='توضیحات مقصد')),
                ('safar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='myare.delivery', verbose_name='سفر')),
            ],
            options={
                'verbose_name': 'مقصد',
                'verbose_name_plural': 'مقاصد ترکیبی',
            },
        ),
    ]
