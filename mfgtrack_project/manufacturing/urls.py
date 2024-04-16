from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('supply/', views.SupplyPageView.as_view(), name='supply'),
    path('products/', views.ProductsPageView.as_view(), name='products'),
    path('quality/', views.QualityPageView.as_view(), name='quality'),
    path('packaging/', views.PackagingPageView.as_view(), name='packaging'),
    path('save-supplier/', views.save_supplier, name='save_supplier'),
]
