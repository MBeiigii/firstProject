from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import Safar,Peik, Delivery,Destination
from .forms import DeliveryRequestForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.



def home(request):
    return render(request, 'myare/home.html')

from .models import Safar  # اضافه کردن مدل Safar

@login_required(login_url='/account/login/')
def get_location(request):
    return render(request, 'myare/delivery_request_form.html')

@login_required(login_url='/account/login/')
def get_locations(request):
    return render(request, 'myare/delivery_request_form_mutual.html')


@login_required(login_url='/account/login/')
def send_req(request,o_lat,o_lng,d_lat,d_lng,price):
    safar = Safar.objects.create(
        user=request.user,accept="-",created='-',end_time='-',peik_id=Peik.objects.first(),navgan_type='motor',first_cost=price,final_cost=price,description='',
        origin_location_lat=o_lat,
        origin_location_lon=o_lng,
        destination_location_lat=d_lat,
        destination_location_lon=d_lng,
        state='start')
    return render(request, 'myare/waiting_customer.html')
    # return HttpResponse('درحال جست و جو برای  ناوگان')  # مثلاً به صفحه موفقیت منتقل شوید


@login_required(login_url='/account/login/')
def acpt(request):
    return render(request, 'myare/acpt.html')


# @login_required(login_url='/account/login/')
def acpt_req(request):
    max_distance_des = request.GET.get('max_distance_des')
    max_distance_org = request.GET.get('max_distance_org')
    min_mony = request.GET.get('min_mony')
    starts = Safar.objects.filter(state='start').values('id', 'final_cost', 'origin_location_lat', 'origin_location_lon', 'destination_location_lat', 'destination_location_lon').order_by('id')
    
    # تبدیل هر تاپل در starts به یک دیکشنری
    starts_req = []
    for start in starts:
        start_dict = {
            'id': start['id'],
            'final_cost': start['final_cost'],
            'origin_location_lat': float(start['origin_location_lat']),
            'origin_location_lon': float(start['origin_location_lon']),
            'destination_location_lat': float(start['destination_location_lat']),
            'destination_location_lon': float(start['destination_location_lon']),
        }
        starts_req.append(start_dict)
    return JsonResponse({'starts': starts_req}, safe=False)



@login_required(login_url='/account/login/')
def accept(request,orderId):
    accept = Safar.objects.get(id=orderId)
    peik= Peik.objects.get(user=request.user)
    accept.peik_id = peik
    accept.state = 'conf'
    accept.save()
    return HttpResponse('Delivery Order started.')


@csrf_exempt
def send_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        delivery_data = data.get('delivery', {})
        destinations_data = data.get('destination', [])

        # Save Delivery data
        delivery = Delivery.objects.create(
            user=request.user,
            accept='-',
            end_time='-',
            peik_id=Peik.objects.first(),
            origin_location_lat=delivery_data.get('lat'),
            origin_location_lon=delivery_data.get('lng'),
            navgan_type='-',
            first_cost='0',
            final_cost='0',
            state='start',
            description='-'
        )

        # Save each Destination data
        for destination in destinations_data:
            coord = destination.get('coord', {})
            Destination.objects.create(
                safar=delivery,
                name=destination.get('name'),
                phone=destination.get('phone'),  # Assuming this was meant to be another field
                packagecode=destination.get('packagecode'),  
                state='start',
                delivery_v_code=0,
                location_lat=coord.get('lat'),
                location_lon=coord.get('lng'),
                description='-'
            )

        return JsonResponse({'status': 'success'}, status=201)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)



@login_required(login_url='/account/login/')
def accept_req(request,orderId):
    accept = Safar.objects.get(id=orderId)
    peik= Peik.objects.get(user=request.user)
    accept.peik_id = peik
    accept.state = 'conf'
    accept.save()
    return HttpResponse('Delivery Order started.')
