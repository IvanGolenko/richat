from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>/', views.buy_item, name='get_stripe_session_id'),
    path('item/<int:id>/', views.item_detail, name='get_item_info'),
]
