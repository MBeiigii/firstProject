from django.urls import path, register_converter
from . import views
from myare.converters import FloatConverter
app_name = 'myare'


register_converter(FloatConverter, 'float')

urlpatterns = [
    path('myare/',views.home,name= 'home'),    
    path('crt/',views.get_location,name= 'crt'),    
    path('crt/crt/send_req/<float:o_lat>/<float:o_lng>/<float:d_lat>/<float:d_lng>/<int:price>',views.send_req,name= 'crt'),       
    path('crt2/',views.get_locations,name= 'crt'),    
    path('crt2/crt2/send_order/', views.send_order, name='send_order'), 
    path('acpt/acpt_req/',views.acpt_req,name= 'cpt_req'),    
    path('acpt/acpt/accept/<int:orderId>',views.accept,name= 'accept'),    
    path('acpt/',views.acpt,name= 'cpt'),    

]