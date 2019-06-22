from django.shortcuts import render
from django.http import HttpResponse
from .models import complaints,completed
import datetime
from twilio.rest import Client
from siteapp.credentials import account_side,auth_token,my_cell,my_twilio
from siteapp.lookup import is_valid_number

def home_view(request):
    return render (request,'siteapp/home.html')
def info_view(request):
    print('THE VIEW')
    return render (request,'siteapp/info.html')

def services_view(request):
    return render(request,'siteapp/services.html')
def help_view(request):
    return render(request,'siteapp/help.html')
def register_veiw(request):

    return render(request,'siteapp/register.html')


def regconf_view(request):
    if request.method=='POST':
        print('this view is working')

        name=request.POST.get('name')
        service=request.POST.get('service')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        date=datetime.datetime.now()
        status='not completed'
        my_dict = {'name': name, 'service': service, 'phone': phone, 'address': address}
        phone='+91'+phone
        phvalid=str(is_valid_number(phone))
        print(phvalid)


        if  phvalid=='True' and len(name)!=0 and service!='-------select-------' and len(address)!=0  :
             print('name is the not type of string')
             table=complaints()
             table.name=name
             table.service=service
             table.phone=phone
             table.address=address
             table.regdate=date
             table.donedate=date
             table.status=status
             table.save()
             stre = 'siteapp/regconf.html'
             client = Client(account_side, auth_token)
             my_msg=service+' request received, \n '+name+' ,\n '+phone+' ,\n '+address
             message = client.messages.create(from_=my_twilio, to=my_cell, body=my_msg)


        else:
            stre ='siteapp/regfail.html'

    return render(request, stre,my_dict)

def update_view(request):

   transfer=complaints.objects.filter(status='completed')
   n=complaints.objects.filter(status='completed').count()


   com = completed()
   print(n)
   str = 'siteapp/noupdate.html'

   if n==1:
     for i in range(n):

        com.name=transfer[i].name
        com.service=transfer[i].service
        com.phone=transfer[i].phone
        com.address=transfer[i].address
        com.regdate=transfer[i].regdate
        com.donedate=transfer[i].donedate
        com.status=transfer[i].status
        com.save()
        trans2=completed.objects.all()
        print(trans2)
        print(n)
        print(i)
        transfer.delete()
        str='siteapp/transfer.html'
   elif n>1:
       str='siteapp/mulselect.html'

   return render(request,str)



