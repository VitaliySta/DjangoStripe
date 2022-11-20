from django.urls import path
from django.views.generic import TemplateView

from .views import BuyView, ItemDetailView

app_name = 'api'


urlpatterns = [
    path('item/<int:id>/', ItemDetailView.as_view(), name='item'),
    path('buy/<int:id>/', BuyView.as_view(), name='buy'),
    path('success/',
         TemplateView.as_view(template_name='items/success.html'),
         name='success'),
]
