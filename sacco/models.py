from django.db import models


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)  # when was the record created
    updated_at = models.DateTimeField(auto_now=True)  # when was the last time the record was updated

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = 'customers'

class Deposit(models.Model):
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.first_name} {self.amount}"

    class Meta:
        db_table = 'deposits'





# run the migrations (this will create the tables)
# python manage.py makemigrations
# python manage.py migrate

#python manage.py populate