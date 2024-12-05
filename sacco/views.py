from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from sacco.app_forms import CustomerForm, LoginForm
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

@login_required
def customers(request):
    data = Customer.objects.all().order_by('id').values()# ORM select * from customers
    paginator = Paginator(data, 15)
    page = request.GET.get('page', 1)
    try:
      paginated_data = paginator.page(page)
    except  EmptyPage:
        paginated_data = paginator.page(1)
    return render(request, "customers.html", {"data": paginated_data})

@login_required
def delete_customer(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    customer.delete()
    # messages.info(request,f"Customer {customer.first_name} was deleted!!")
    return redirect('customers')  # Redirects back to customers page and will load again

@login_required
def customer_details(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    deposits = Deposit.objects.filter(customer_id=customer_id)

    return render(request, "details.html",{"deposits":deposits},{"customer":customer})

@login_required
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, "Customer added successfully")
            return redirect('customers')

    return render(request , 'customer_form.html',{"form":form} )


#pip install django-crispy-forms
#pip install crispy-bootstrap5


def login_user(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request , 'login.html',{'form':form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)  #stores this data as sessions in the server and on the broswer as cookies
                return redirect('customers')
        # messages.error(request,"Invalid username or password")
        return render(request , 'login.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


