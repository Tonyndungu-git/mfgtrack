from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('supply/', views.supply_page_view, name='supply'),
    path('products/', views.products_page_view, name='products'),
    path('quality/', views.quality_page_view, name='quality'),
    path('packaging/', views.packaging_page_view, name='packaging'),
    path('save-supplier/', views.save_supplier, name='save_supplier'),
    path('get-suppliers/', views.get_suppliers, name='get_suppliers'),
    path('supplier-list/', views.get_suppliers, name='supplier_list'),  # Assuming this is the same view as get_suppliers
    path('product-list/', views.product_list, name='product_list'),
    path('save-product/', views.save_product, name='save_product'),
     path('product-create/', views.product_create, name='product_create'),
]
