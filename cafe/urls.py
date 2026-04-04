from django.contrib import admin
from django.urls import path, include
from cafe import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('delete_dish/<int:item_id>/', views.delete_dish, name='delete_dish'),
    path('offers', views.offers, name='offers'),
    path('reviews', views.reviews, name='reviews'),
    path('profile', views.profile, name='profile'),
    path('all_orders', views.all_orders, name='all_orders'),
    path('manage_menu', views.manage_menu, name='manage_menu'),
    path('cart', views.cart, name='cart'),
    path('my_orders', views.my_orders, name='my_orders'),
    path('login', views.Login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.Logout, name='logout'),
    path('generate_bill', views.generate_bill, name='generate_bill'),
    path('view_bills', views.view_bills, name='view_bills'),
    path('qr_code/<str:table_number>', views.generate_qr_code, name='generate_qr_code'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('reset_password', views.reset_password, name='reset_password'),
    path('qr_manager', views.qr_manager, name='qr_manager'),  # ✅ NEW
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)