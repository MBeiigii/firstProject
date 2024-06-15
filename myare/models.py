from django.db import models
from datetime import datetime
from jdatetime import datetime as jdatetime_datetime
from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.contrib.auth import get_user_model
import jdatetime

# 
User = get_user_model()

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         CustomerProfile.objects.create(user=instance)

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    phone_number = models.CharField(max_length=15)
    national_code = models.CharField(max_length=10)
    address = models.TextField()
    # سایر اطلاعات مورد نیاز کاربر
    class Meta:
        verbose_name_plural = "جدول پروفایل"



# Create your models here.

mabda=(('shahrvand','فروشگاه شهروند '),('anbar','انبار محصول'),('home','خانه'))
nav=(('motor','موتور'),('vanet','وانت'),('kamion','کامیون'))
tran_state = (('success','موفق'),('cancel','باطل'),('rej','رد شده'),('Current','جاری'),('movg','معوق'),('laghv','لغو'),('conf','تایید شده'),('done','پرداخت شده'))
safar_state = (('start','شروع'),('moatl','معطل'),('cancel','باطل'),('rej','رد شده'),('conf','تایید شده'),('success','موفق'),('laghv','لغو'),('done','پرداخت شده'))
nav_qual = (("خوب","خوب"),("متوسط","متوسط"),("بد","بد"))
delivery_state=(("start","شروع شده"),("deliv","تحویل شده"),("return","برگشته"),("cancel","باطل"),("other","سایر"))
class Location(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=60,verbose_name="نام مکان")
    type = models.CharField(default='-', max_length=30, choices=mabda,verbose_name="نوع مکان") 
    lon =  models.DecimalField(max_digits=9, decimal_places=6,verbose_name="عرض جغرافیایی")
    lat =  models.DecimalField(max_digits=9, decimal_places=6,verbose_name="طول جغرافیایی")
    address  = models.CharField(max_length=60,verbose_name="آدرس")
    phone1 =  models.IntegerField(verbose_name="شماره تلفن 1")
    phone2 =  models.IntegerField(verbose_name="شماره تلفن 2")
    operator  = models.CharField(max_length=60,verbose_name="نام مسئول")
    code_melli =  models.IntegerField(verbose_name="کد ملی")
    description  = models.CharField(max_length=60,verbose_name="توضیحات")
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "جدول انبارها"


class Peik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    center =  models.ForeignKey(Location, on_delete=models.CASCADE,verbose_name = "محل ماموریت") #مبدا ماموریت
    keyfiat = models.CharField(max_length=60,verbose_name="کیفیت ناوگان",choices=nav_qual) # شرایط ناوگان
    navgan = models.CharField(max_length=60 , choices= nav,verbose_name="نوع ناوگان") #
    name  = models.CharField(max_length=60,verbose_name="نام راننده")
    code_melli =  models.IntegerField(verbose_name="کد ملی")
    pelak  = models.CharField(max_length=60,verbose_name="پلاک")
    phone =  models.IntegerField(verbose_name="شماره تلفن")
    hesab_banki =  models.CharField(max_length=60,verbose_name="حساب بانکی")
    sum_demands =  models.IntegerField(verbose_name="جمع مطالبات",default = 0)
    sum_income =  models.IntegerField(verbose_name="جمع درآمد",default = 0)
    description  = models.CharField(max_length=60,verbose_name="توضیحات", null=True,blank=True)
    def __str__(self):
        return self.pelak
    class Meta:
        verbose_name_plural = "جدول ناوگان"

class Safar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.CharField(max_length=20,verbose_name=' زمان شروع درخواست ')
    accept = models.CharField(max_length=20,verbose_name=' زمان قبول درخواست ')
    end_time = models.CharField(max_length=20,verbose_name=' زمان پایان درخواست ')
    # origin_location  = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='mabda',verbose_name = "مبدا سفر")
    peik_id = models.ForeignKey(Peik, on_delete=models.CASCADE,verbose_name="ناوگان")
    # destination_location  = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='maghsad', verbose_name= "مقصد سفر")
    origin_location_lat  =  models.DecimalField(max_digits=9, decimal_places=6,verbose_name="عرض جغرافیایی مبدا")
    origin_location_lon  =  models.DecimalField(max_digits=9, decimal_places=6,verbose_name="طول جغرافیایی مبدا")
    destination_location_lat  =  models.DecimalField(max_digits=9, decimal_places=6,verbose_name="عرض جغرافیایی مقصد")
    destination_location_lon =  models.DecimalField(max_digits=9, decimal_places=6,verbose_name="طول جغرافیایی مقصد")  
    navgan_type = models.CharField(max_length=60 , choices= nav,verbose_name="نوع ناوگان")
    first_cost =  models.IntegerField( verbose_name="کرایه پایه")
    final_cost  =  models.IntegerField( verbose_name="کرایه نهایی")
    state =  models.CharField(default='-', max_length=30, choices=safar_state,verbose_name="وضعیت سفر") 
    description  = models.CharField(max_length=60, verbose_name="توضیحات")
    def save(self, *args, **kwargs):
        current_datetime = datetime.now()
        jalali_datetime = jdatetime_datetime.fromgregorian(datetime=current_datetime).strftime('%Y/%m/%d-%H:%M:%S')
        self.created = jalali_datetime
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "جدول سفرهای تک"


class Delivery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.CharField(max_length=20, verbose_name='زمان شروع درخواست')
    accept = models.CharField(max_length=20, verbose_name='زمان قبول درخواست', default='')
    end_time = models.CharField(max_length=20, verbose_name='زمان پایان درخواست')
    peik_id = models.ForeignKey(Peik, on_delete=models.CASCADE, verbose_name="ناوگان")
    origin_location_lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="عرض جغرافیایی مبدا")
    origin_location_lon = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="طول جغرافیایی مبدا")
    navgan_type = models.CharField(max_length=60, choices=nav, verbose_name="نوع ناوگان")
    first_cost = models.IntegerField(verbose_name="کرایه پایه")
    final_cost = models.IntegerField(verbose_name="کرایه نهایی")
    state = models.CharField(default='-', max_length=30, choices=safar_state, verbose_name="وضعیت سفر")
    description = models.CharField(max_length=60, verbose_name="توضیحات")

    def save(self, *args, **kwargs):
        current_datetime = datetime.now()
        jalali_datetime = jdatetime.datetime.fromgregorian(datetime=current_datetime).strftime('%Y/%m/%d-%H:%M:%S')
        self.created = jalali_datetime
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "جدول سفرهای ترکیبی"



class Destination(models.Model):
    safar = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='destinations', verbose_name="سفر")
    name = models.CharField(max_length=200, blank=True, verbose_name="نام گیرنده")
    phone =  models.IntegerField(verbose_name="تلفن گیرنده")
    packagecode = models.CharField(default='-', max_length=30, verbose_name="کدبار")
    state = models.CharField(default='-', max_length=30, choices=delivery_state, verbose_name="وضعیت تحویل")
    delivery_v_code = models.IntegerField()
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="عرض جغرافیایی مقصد")
    location_lon = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="طول جغرافیایی مقصد")
    description = models.CharField(max_length=200, blank=True, verbose_name="توضیحات مقصد")

    class Meta:
        verbose_name = "مقصد"
        verbose_name_plural = "مقاصد ترکیبی"



class Transaction(models.Model):
    created = models.CharField(max_length=20,verbose_name=' زمان تراکنش ')
    updated = models.CharField(max_length=20,verbose_name='آخرین زمان بروزرسانی')
    safar_id  = models.ForeignKey(Safar, on_delete=models.CASCADE,verbose_name = "کد سفر")
    amount =  models.IntegerField(verbose_name="مبلغ تراکنش")
    peik_id = models.ForeignKey(Peik, on_delete=models.CASCADE,verbose_name="ناوگان")
    state =  models.CharField(default='-', max_length=30, choices=tran_state,verbose_name="وضعیت تراکنش") 
    description  = models.CharField(max_length=60, verbose_name="توضیحات")
    class Meta:
        verbose_name_plural = "جدول تراکنش ها"

class Cargo_fare(models.Model):
    origin_location  = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='mabda_s',verbose_name = "مبدا سفر")
    destination_location  = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='maghsad_s', verbose_name= "مقصد سفر")
    amount1 =  models.IntegerField(verbose_name=" مبلغ کرایه حداقلی")
    amount2 =  models.IntegerField(verbose_name=" مبلغ کرایه پایه")
    amount3 =  models.IntegerField(verbose_name=" مبلغ کرایه شلوغ")
    amount4 =  models.IntegerField(verbose_name=" مبلغ کرایه حداکثری ")
    class Meta:
        verbose_name_plural = "جدول کرایه ها"


