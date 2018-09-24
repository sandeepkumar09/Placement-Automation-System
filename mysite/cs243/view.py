from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from credentials.forms import MyRegistrationForm,overviewform
from django.core.mail import send_mail
from credentials.models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User


global piconce,flag
piconce=''

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html',c,context_instance=RequestContext(request))



def auth_view(request):
    username=request.POST.get('username', '')
    password=request.POST.get('password', '')
    user_type=request.POST.get('user_type','')
    user=auth.authenticate(username=username,password=password)
    obj=User.objects.filter(username=user)
    
    if user is not None and user_type==obj[0].user_type:
        auth.login(request,user)
        flag=0
        return HttpResponseRedirect('/loggedin/')
    else:
        return HttpResponseRedirect('/invalid/')
    
def c_auth_view(request):
    username=request.POST.get('username', '')
    password=request.POST.get('password', '')
    user_type=request.POST.get('user_type','')
    user=auth.authenticate(username=username,password=password)
    obj = User.objects.filter(username=user)

    if user is not None and user_type == obj[0].user_type:
        auth.login(request,user)
        return HttpResponseRedirect('/cloggedin/')
    else:
        return HttpResponseRedirect('/invalid/')    

def invalid_login(request):
    return render_to_response('invalid_login.html',context_instance=RequestContext(request))

def loggedin(request):
    p=photo.objects.filter(username=request.user.username)
    obj=PLACEMENTS_DATA.objects.filter()
    if len(p)>0:
        piconce = p[0].imagename
        return render_to_response('index2.html',{'fullname':request.user.username,'picname':p[0].imagename,'total':obj[0].totalpercentageplaced,'ugplaced':obj[0].undergradplaced,'pgplaced':obj[0].postgradplaced},context_instance=RequestContext(request))
    else:
        piconce=''
        return render_to_response('index2.html',{'fullname':request.user.username,'picname':'','total':obj[0].totalpercentageplaced,'ugplaced':obj[0].undergradplaced,'pgplaced':obj[0].postgradplaced},context_instance=RequestContext(request))
        
def c_loggedin(request):
    f2=overviewform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    return render_to_response('overview.html',{"fullname":request.user.username,"form2":f2},context_instance=RequestContext(request))

def register_user(request):
    if request.method=="POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success/')
        else:
            print "register unsuccessful"
    else:
        form = MyRegistrationForm()
        
    args = {}
    args.update(csrf(request))
    args['form']=MyRegistrationForm(request.POST)
    print args
    return render_to_response('register.html',args,context_instance=RequestContext(request))

def register_success(request):
    return render_to_response('login.html',context_instance=RequestContext(request))

def index2(request):
    
    obj=PLACEMENTS_DATA.objects.filter()
    t=get_template("index2.html")
    
    p=t.render(Context({'fullname':request.user.username,'total':obj[0].totalpercentageplaced,'ugplaced':obj[0].undergradplaced,'pgplaced':obj[0].postgradplaced}))
    return HttpResponse(p)

def studentprofile(request):
    return render_to_response('studentprofile.html',{'fullname':request.user.username,'picname':piconce},context_instance=RequestContext(request))
    
def profile_contact(request):
    t=get_template("profile_contact.html")
    data = contact.objects.filter(username=request.user.username)
    p=t.render(Context({'fullname':request.user.username,'email':request.user.email,'mobile':data[0].mobile,'temp':data[0].temporary_address,'perm':data[0].permanent_address,'website':data[0].website}))
    return HttpResponse(p)

def profile_photo(request):
    t=get_template("profile_photo.html")
    data = photo.objects.filter(username=request.user.username)
    p=t.render(Context({'fullname':request.user.username,'picname':data[0].imagename}))
    return HttpResponse(p)

def ex(request):
    t=get_template("blank.html")
    p=t.render(Context({}))
    return HttpResponse(p)

