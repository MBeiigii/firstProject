# Generated by Django 5.0.4 on 2024-04-30 08:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('national_code', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'جدول پروفایل',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='نام مکان')),
                ('type', models.CharField(choices=[('shahrvand', 'فروشگاه شهروند '), ('anbar', 'انبار محصول'), ('home', 'خانه')], default='-', max_length=30, verbose_name='نوع مکان')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='عرض جغرافیایی')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='طول جغرافیایی')),
                ('address', models.CharField(max_length=60, verbose_name='آدرس')),
                ('phone1', models.IntegerField(verbose_name='شماره تلفن 1')),
                ('phone2', models.IntegerField(verbose_name='شماره تلفن 2')),
                ('operator', models.CharField(max_length=60, verbose_name='نام مسئول')),
                ('code_melli', models.IntegerField(verbose_name='کد ملی')),
                ('description', models.CharField(max_length=60, verbose_name='توضیحات')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'جدول انبارها',
            },
        ),
        migrations.CreateModel(
            name='Cargo_fare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount1', models.IntegerField(verbose_name=' مبلغ کرایه حداقلی')),
                ('amount2', models.IntegerField(verbose_name=' مبلغ کرایه پایه')),
                ('amount3', models.IntegerField(verbose_name=' مبلغ کرایه شلوغ')),
                ('amount4', models.IntegerField(verbose_name=' مبلغ کرایه حداکثری ')),
                ('destination_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maghsad_s', to='myare.location', verbose_name='مقصد سفر')),
                ('origin_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mabda_s', to='myare.location', verbose_name='مبدا سفر')),
            ],
            options={
                'verbose_name_plural': 'جدول کرایه ها',
            },
        ),
        migrations.CreateModel(
            name='Peik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyfiat', models.CharField(choices=[('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=60, verbose_name='کیفیت ناوگان')),
                ('navgan', models.CharField(choices=[('motor', 'موتور'), ('vanet', 'وانت'), ('kamion', 'کامیون')], max_length=60, verbose_name='نوع ناوگان')),
                ('name', models.CharField(max_length=60, verbose_name='نام راننده')),
                ('code_melli', models.IntegerField(verbose_name='کد ملی')),
                ('pelak', models.CharField(max_length=60, verbose_name='پلاک')),
                ('phone', models.IntegerField(verbose_name='شماره تلفن')),
                ('hesab_banki', models.CharField(max_length=60, verbose_name='حساب بانکی')),
                ('sum_demands', models.IntegerField(default=0, verbose_name='جمع مطالبات')),
                ('sum_income', models.IntegerField(default=0, verbose_name='جمع درآمد')),
                ('description', models.CharField(blank=True, max_length=60, null=True, verbose_name='توضیحات')),
                ('center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myare.location', verbose_name='محل ماموریت')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'جدول ناوگان',
            },
        ),
        migrations.CreateModel(
            name='Safar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.CharField(max_length=20, verbose_name=' زمان شروع درخواست ')),
                ('accept', models.CharField(max_length=20, verbose_name=' زمان قبول درخواست ')),
                ('end_time', models.CharField(max_length=20, verbose_name=' زمان پایان درخواست ')),
                ('origin_location_lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='عرض جغرافیایی مبدا')),
                ('origin_location_lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='طول جغرافیایی مبدا')),
                ('destination_location_lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='عرض جغرافیایی مقصد')),
                ('destination_location_lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='طول جغرافیایی مقصد')),
                ('navgan_type', models.CharField(choices=[('motor', 'موتور'), ('vanet', 'وانت'), ('kamion', 'کامیون')], max_length=60, verbose_name='نوع ناوگان')),
                ('first_cost', models.IntegerField(verbose_name='کرایه پایه')),
                ('final_cost', models.IntegerField(verbose_name='کرایه نهایی')),
                ('state', models.CharField(choices=[('start', 'شروع'), ('moatl', 'معطل'), ('cancel', 'باطل'), ('rej', 'رد شده'), ('conf', 'تایید شده'), ('success', 'موفق'), ('laghv', 'لغو'), ('done', 'پرداخت شده')], default='-', max_length=30, verbose_name='وضعیت سفر')),
                ('description', models.CharField(max_length=60, verbose_name='توضیحات')),
                ('peik_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myare.peik', verbose_name='ناوگان')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'جدول سفرها',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.CharField(max_length=20, verbose_name=' زمان تراکنش ')),
                ('updated', models.CharField(max_length=20, verbose_name='آخرین زمان بروزرسانی')),
                ('amount', models.IntegerField(verbose_name='مبلغ تراکنش')),
                ('state', models.CharField(choices=[('success', 'موفق'), ('cancel', 'باطل'), ('rej', 'رد شده'), ('Current', 'جاری'), ('movg', 'معوق'), ('laghv', 'لغو'), ('conf', 'تایید شده'), ('done', 'پرداخت شده')], default='-', max_length=30, verbose_name='وضعیت تراکنش')),
                ('description', models.CharField(max_length=60, verbose_name='توضیحات')),
                ('peik_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myare.peik', verbose_name='ناوگان')),
                ('safar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myare.safar', verbose_name='کد سفر')),
            ],
            options={
                'verbose_name_plural': 'جدول تراکنش ها',
            },
        ),
    ]
