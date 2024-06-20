from django.shortcuts import render, redirect
from django.contrib import messages
from apk1.models import Product, Cart
from django.http import JsonResponse

def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            try:
                product_check = Product.objects.get(id=prod_id)
            except Product.DoesNotExist:
                return JsonResponse({'status': "No such product found"})

            if Cart.objects.filter(user=request.user.id, product_id=prod_id).exists():
                return JsonResponse({'status': "Product Already in Cart"})
            else:
                prod_qty = int(request.POST.get('product_qty'))

                if product_check.quantity >= prod_qty:
                    Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty)
                    return JsonResponse({'status': "Product added successfully"})
                else:
                    return JsonResponse({'status': f"Only {product_check.quantity} quantity available"})
        else:
            return JsonResponse({'status': "Login to Continue"})
    
    return redirect('main')
