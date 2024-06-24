from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = 'index'),
    path('colection/',views.colection, name = 'colection'),
    path('blogs/',views.blogs, name = 'blogs'),
    path('about/',views.about, name = 'about'),
    path('carro_compras/',views.carro_compras, name = 'carro_compras'),
    path('login/',views.login_valida, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('pago/',views.pago, name = 'pago'),
    path('detalle_producto/',views.detalle_producto, name = 'detalle_producto'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
