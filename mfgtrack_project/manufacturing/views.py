from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Product, Supplier

def home_view(request):
    return render(request, 'manufacturing/home.html')

def supply_page_view(request):
    return render(request, 'manufacturing/supply.html')

def products_page_view(request):
    suppliers = Supplier.objects.all()
    return render(request, 'manufacturing/products.html', {'suppliers': suppliers})

def quality_page_view(request):
    return render(request, 'manufacturing/quality.html')

def packaging_page_view(request):
    return render(request, 'manufacturing/packaging.html')

def save_supplier(request):
    if request.method == 'POST':
        supplier_name = request.POST.get('supplierName')
        contact_person = request.POST.get('contactPerson')
        contact_email = request.POST.get('contactEmail')
        phone_number = request.POST.get('phoneNumber')
        address = request.POST.get('address')

        if supplier_name and contact_person and contact_email and phone_number and address:
            try:
                supplier = Supplier.objects.create(
                    name=supplier_name,
                    contact_person=contact_person,
                    email=contact_email,
                    phone_number=phone_number,
                    address=address
                )
                suppliers = list(Supplier.objects.values())
                return JsonResponse({'success': True, 'suppliers': suppliers})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)}, status=500)
        else:
            return JsonResponse({'success': False, 'error': 'Invalid data provided'}, status=400)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)

def product_create(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        product_name = request.POST.get('productName')
        description = request.POST.get('productDescription')
        unit_price = request.POST.get('unitPrice')
        supplier_id = request.POST.get('supplier')

        # Get the selected supplier from the database
        supplier = Supplier.objects.get(pk=supplier_id)

        # Create and save the new Product instance
        new_product = Product.objects.create(
            name=product_name,
            description=description,
            unit_price=unit_price,
            supplier=supplier
        )

        # Optionally, you can add additional fields or validation logic here

        # Redirect to the product list page after saving the product
        return redirect('product_list')

    else:
        # Retrieve all suppliers from the database to populate the dropdown
        suppliers = Supplier.objects.all()
        return render(request, 'manufacturing/products.html', {'suppliers': suppliers})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'manufacturing/product_list.html', {'products': products})

def save_product(request):
    if request.method == 'POST':
        # Extract data from POST request
        product_name = request.POST.get('productName')
        description = request.POST.get('productDescription')
        unit_price = request.POST.get('unitPrice')
        supplier_id = request.POST.get('supplier')

        # Validate input data
        if not product_name or not description or not unit_price or not supplier_id:
            return JsonResponse({'success': False, 'error': 'All fields are required.'}, status=400)

        try:
            # Convert supplier_id to an integer
            supplier_id = int(supplier_id)
            # Retrieve the Supplier object
            supplier = Supplier.objects.get(pk=supplier_id)
        except (ValueError, Supplier.DoesNotExist):
            return JsonResponse({'success': False, 'error': 'Invalid supplier.'}, status=400)

        try:
            # Create a new Product instance and save to database
            product = Product.objects.create(
                name=product_name,
                description=description,
                unit_price=unit_price,
                supplier=supplier
            )
            return JsonResponse({'success': True, 'product_id': product.id})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)
def get_suppliers(request):
    if request.method == 'GET':
        try:
            suppliers = Supplier.objects.all()
            return render(request, 'manufacturing/supplier_list.html', {'suppliers': suppliers})
        except Exception as e:
            return render(request, 'manufacturing/supplier_list.html', {'error': str(e)})

    return render(request, 'manufacturing/supplier_list.html', {'error': 'Invalid request method'})
