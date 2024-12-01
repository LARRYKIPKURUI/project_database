from django.http import HttpResponse
from django.shortcuts import render

from sacco.models import Customer, Deposit


# Create your views here.
def test(request):
    # save a customer
    # c1 = Customer(first_name='John', last_name='Smith',
    #               email='smithjo@gmail.com', dob='2004-5-18',
    #               gender='Male')
    # c1.save()
    # c2 = Customer(first_name='Jane', last_name='whammy',
    #               email='wamejane@gmail.com', dob='2002-3-18',
    #               gender='Female')
    # c2.save()
    customers = Customer.objects.count()

    #Fetching one customer
    c1 = Customer.objects.get(id=1) #select * from customers where id =1
    print(c1)

    d1 = Deposit(amount=1000,status=True,customer=c1)
    d1.save()
    deposit_count = Deposit.objects.count()

    return HttpResponse(f"Successfully saved {customers} customers and {deposit_count} deposits")
