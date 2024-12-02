from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect

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
    customer_count = Customer.objects.count()

    # Fetching one customer
    c1 = Customer.objects.get(id=1)  # select * from customers where id =1
    print(c1)

    d1 = Deposit(amount=1000, status=True, customer=c1)
    d1.save()
    deposit_count = Deposit.objects.count()

    return HttpResponse(f"Successfully saved {customer_count} customers and {deposit_count} deposits")


def customers(request):
    data = Customer.objects.all().order_by('id').values()# ORM select * from customers
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
      paginated_data = paginator.page(page)
    except  EmptyPage:
        paginated_data = paginator.page(1)
    return render(request, "customers.html", {"data": paginated_data})


def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()

    return redirect('customers')  # Redirects back to customers page and will load again


def customer_details(request,customer_id):
    customer = Customer.objects.get(id=customer_id)
    deposits = Deposit.objects.filter(customer_id=customer_id)

    return render(request, 'details.html',{"deposits":deposits},{"customer":customer})