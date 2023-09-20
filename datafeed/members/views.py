from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import CustomerForm
from django.shortcuts import render

def members(request):
    #mymembers = Member.objects.all().values()
    mymembers = Member()
    template = loader.get_template('form.html')#('all_members.html')
    if request.method=='POST':
        mymember = Member(request.POST)
        if mymember.is_valid():
            mymember.save()

    context = {
    'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))
  
def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
    }
    return HttpResponse(template.render(context, request))

def index(request):
    template = loader.get_template('form.html')
    form = CustomerForm()
    context = {'form':form}
    #return render(request, 'datafeed\members\templates\form.html', )
    return HttpResponse(template.render(context, request))