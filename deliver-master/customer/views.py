from django.shortcuts import render
from django.views import View
from .models import OrderModel

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')

class Order(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order.html')
    
    def style(request):
        return render(request, 'customer/order.html')
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        reservation = request.POST.get('reservation')
        table_number = request.POST.get('table_number')

        order = OrderModel.objects.create(
            name=name,
            reservation = reservation,
            table_number=table_number
        )

        return render(request, 'customer/order_confirmation.html')