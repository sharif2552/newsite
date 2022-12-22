from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from products.models import paymentmaking
from products.form import CustomerForm , customerinfo
from products.models import info
# Create your views here.
def index(request):

    return render(request, "products/index.html")


def about(request):
    return render(request,"products/about.html")

def contact(request):
    return render(request,"products/contact.html")

def base(request):
    return render(request,"products/base.html")

def new(request):
    pay_meth = paymentmaking.objects.all()
    return render(request,"products/new.html", {'pay' : pay_meth})


def formtest(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CustomerForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/congrats/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomerForm()

    return render(request, 'products/new.html', {'form': form})



from django.shortcuts import render
from .models import info
from .form import customerinfo

def formtest2(request):
  if request.method == "POST":
    form = customerinfo(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = customerinfo()
  return render(request, 'products/new.html', {'form': form})


def success(request):
    return render(request,'products/congrats.html')