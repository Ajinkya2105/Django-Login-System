from django.shortcuts import render
from myApp.models import Customer
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        cust = Customer.objects.get(Email=username)
        if not cust:
            return render(request, 'index.html', {'status' : 'No user with the data'})
        else:
            if cust.pass1==password:
                from_mail = settings.EMAIL_HOST_USER
                # send_mail('About login to system', 'Recent new device tried to login in your system.', from_mail, [username])
                return render(request,'random.html')
    return render(request, 'index.html')

def signup(request):
    if request.method=='POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        for i in Customer.objects.all():
            if i.Email==email:
                return render(request, 'signup.html', {'status':'Email already used.'})
      
        if pass1 != pass2:
            return render(request, 'signup.html', {'status':'Both password must be same'})
        else:  
            if not any(char.islower() for char in pass1):
                return render(request, 'signup.html', {'status':'Password must contain small letter'})
            elif not any(char.isupper() for char in pass1):
                return render(request, 'signup.html', {'status':'Password must contain capital letter'})
            elif not any(char.isdigit() for char in pass1):
                return render(request, 'signup.html', {'status':'Password must contain numbers'})
                
            data = Customer(Email = email, pass1 = pass1, pass2 = pass2)
            data.save()
            return render(request, 'signup.html', {'status':'User registered successfully.'})

    return render(request, 'signup.html')
