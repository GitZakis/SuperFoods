import os
from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from django.template.defaulttags import comment
from .models import  Products,Categories,Manufacturers
from django.utils import timezone
from django.db.models import Q
import random

# Create your views here.
def post_list(request):
    cat = request.GET.get('cat')
    txt = request.GET.get('txt')

    if cat is None:
        if txt:
            product = Products.objects.filter(
                (Q(description__contains=txt) | Q(description__contains=txt)) & Q(published_date__lte=timezone.now())).order_by(
                'published_date')
        else:
            product = Products.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    elif cat.isdigit():
        cat = int(cat)
        product = Products.objects.filter(published_date__lte=timezone.now()).filter(category=cat).order_by('published_date')
    else:
        product = Products.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    # φορτωνουμε τους κατασκευαστες
    suppliers = Manufacturers.objects.all()

    # Επιλέγουμε 3 τυχαια προιοντα για προσφορα shop
    all_products = list(Products.objects.filter(published_date__lte=timezone.now()))
    random_products = random.sample(all_products,min(3, len(all_products)))


    # # Επιλογή προϊόντων σε πολλαπλάσια του 3 για το carousel
    all_products = list(Products.objects.filter(published_date__lte=timezone.now()))
    num_products = min(9, len(all_products))  # Μέγιστο 9 προϊόντα
    num_products -= num_products % 3  # Στρογγυλοποίηση σε πολλαπλάσιο του 3
    random_carousel_products = random.sample(all_products, num_products) if num_products > 0 else []

    return render(request, 'blog/post_list.html',
                  {'products': product, 'suppliers': suppliers, 'random_products': random_products,
                   'random_carousel_products': random_carousel_products })

def post_detail(request, pk):
    products_detail = get_object_or_404(Products, pk=pk)
    return render(request, 'blog/post_detail.html', {'products_detail': products_detail})

def about_us(request):
    return render(request, 'blog/about_us.html')

def manufacturer_products(request, manufacturer_id):
    manufacturer = get_object_or_404(Manufacturers, pk=manufacturer_id)
    products = Products.objects.filter(manufacturer=manufacturer)

    return render(request, 'blog/post_list.html', {
        'products': products,
        'selected_manufacturer': manufacturer
    })

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Θέμα και περιεχόμενο του email
        subject = f"Νέο μήνυμα από {name} ({email})"
        body = f"Όνομα: {name}\nEmail: {email}\n\nΜήνυμα:\n{message}"

        # Αποστολή email
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, ['zakisgm@gmail.com'])

        return redirect('contact_success')  # Σελίδα επιτυχίας

    return render(request, 'blog/contact.html')
def contact_success(request):
    return render(request, 'blog/contact_success.html')
