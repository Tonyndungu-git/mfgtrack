from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from .models import Supplier

def home_view(request):
    return render(request, 'manufacturing/home.html')

class SupplyPageView(TemplateView):
    template_name = 'manufacturing/supply.html'

class ProductsPageView(TemplateView):
    template_name = 'manufacturing/products.html'

class QualityPageView(TemplateView):
    template_name = 'manufacturing/quality.html'

class PackagingPageView(TemplateView):
    template_name = 'manufacturing/packaging.html'

def save_supplier(request):
    if request.method == 'POST':
        supplier_name = request.POST.get('supplierName')
        contact_email = request.POST.get('contactEmail')
        phone_number = request.POST.get('phoneNumber')

        # Validate input data (you might want to add more validation)

        if supplier_name and contact_email and phone_number:
            try:
                # Create a new Supplier instance and save to database
                supplier = Supplier.objects.create(
                    name=supplier_name,
                    email=contact_email,
                    phone_number=phone_number
                )
                return JsonResponse({'success': True})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)}, status=500)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid data provided'}, status=400)

    # Handle invalid requests (should not reach here for POST requests)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
