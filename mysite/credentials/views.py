from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contactform,internshipform,languageform,projectform,postgradform,undergradform,srsecform,secform,DocumentForm,photoform,overviewform,statisticsform,jobprofileform,benefitsform,logoform,mediaform,headofficeform,Workform,Sales_officeform
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from cs243.view import piconce

# Create your views here.
global field1,field2,field3,yopp,spip,email,mob,Position,per,temp,cpip,branch,yopu,spiu,cpiu,board,school,perc,boardsc,schoolsc,percsc,yopsc,yopsr,l,pr1,pr2,pr3,f1,f2,f3,desc,Branches,url,description,Area,Areas,Areaw,plot_number,plot_numbers,plot_numberw,email,emails,emailw,City,Citys,Cityw,Pincode,Pincodes,Pincodew,Country,Countrys,Countryw,Phone,Phones,Phonew,log

def search(request):
    context={}
    template="search.html"
    return render(request,template,context)

def studentsearch(request):
    data = contact.objects.filter(username=request.POST['studentsearch'])
    if len(data)>0:
        email=data[0].email
        mob=data[0].mobile
        temp=data[0].temporary_address
        per=data[0].permanent_address
    else:
        email=''
        mob=''
        temp=''
        per=''
        
    p=photo.objects.filter(username=request.POST['studentsearch'])
    if len(p)>0:
        pic=p[0].imagename
    else:
        pic=''
        
    i=internship.objects.filter(username=request.POST['studentsearch'])
    if len(i)>0:
        f1=i[0].field1
        f2=i[0].field2
        f3=i[0].field3
    else:
        f1=''
        f2=''
        f3=''
    post=postgrad.objects.filter(username=request.POST['studentsearch'])
    if len(post)>0:
        yopp=post[0].year_of_passing
        spip=post[0].Last_spi
        cpip=post[0].Cpi
        branch=post[0].Branch_of_study
    else:
        yopp=''
        spip=''
        cpip=''
        branch=''
    under=undergrad.objects.filter(username=request.POST['studentsearch'])
    if len(under)>0:
        yopu=under[0].year_of_passing
        spiu=under[0].Last_spi
        cpiu=under[0].Cpi
             
    else:
        yopu=''
        spiu=''
        cpiu=''
    sr=srsec.objects.filter(username=request.POST['studentsearch'])
    if len(sr)>0:
        yopsr=sr[0].year_of_passing
        perc=sr[0].percentage_obtained
        school=sr[0].school
        board=sr[0].Board
    else:
        yopsr=''
        perc=''
        school=''
        board=''   
    sc=sec.objects.filter(username=request.POST['studentsearch'])
    if len(sc)>0:
        yopsc=sc[0].year_of_passing
        percsc=sc[0].percentage_or_cpi
        schoolsc=sc[0].school
        boardsc=sc[0].Board
    else:
        yopsc=''
        percsc=''
        schoolsc=''
        boardsc=''
        
    lan=planguage.objects.filter(username=request.POST['studentsearch'])
    if len(lan)>0:
        l=lan[0].languages_known
    else:
        l=''
    
    pr=project.objects.filter(username=request.POST['studentsearch'])
    if len(pr)>0:
        pr1=pr[0].project1
        pr2=pr[0].project2
        pr3=pr[0].project3
    else:
        pr1=''
        pr2=''
        pr3=''
            
            
        #context={'name':request.POST['studentsearch'],'l':l,'picname':p[0].imagename,'pr1':pr1,'pr2':pr2,'pr3':pr3,'yopsr':yopsr,'yopsc':yopsc,'percsc':percsc,'perc':perc,'schoolsc':schoolsc,'boardsc':boardsc,'school':school,'board':board,'yopu':yopu,'cpiu':cpiu,'spiu':spiu,'yopp':yopp,'cpip':cpip,'spip':spip,'branch':branch,'f1':field1,'f2':field2,'f3':field3,'email':data[0].email,'mob':data[0].mobile,'temp':data[0].temporary_address,'per':data[0].permanent_address}
    context={'name':request.POST['studentsearch'],'pr1':pr1,'pr2':pr2,'pr3':pr3,'l':l,'yopsr':yopsr,'yopsc':yopsc,'percsc':percsc,'perc':perc,'schoolsc':schoolsc,'boardsc':boardsc,'school':school,'board':board,'yopu':yopu,'cpiu':cpiu,'spiu':spiu,'yopp':yopp,'cpip':cpip,'spip':spip,'branch':branch,'picname':pic,'f1':f1,'f2':f2,'f3':f3,'email':email,'mob':mob,'temp':temp,'per':per}
    template="studentsearch.html"
    return render(request,template,context)

def companysearch(request):
    
    c = overviewm.objects.filter(username=request.POST['companysearch'])
    if len(c)>0:
        description=c[0].description
        url=c[0].url
    else:
        description=''
        url=''
        
    p=jobprofilem.objects.filter(username=request.POST['companysearch'])
    if len(p)>0:
        Position=p[0].position
        CPI_cut_off=p[0].CPI_cut_off
        Branches=p[0].Branches
        desc=p[0].description
    else:
        Position=''
        CPI_cut_off=''
        Branches=''
        desc=''
        
    i=logom.objects.filter(username=request.POST['companysearch'])
    if len(i)>0:
        log=i[0].imagename
    else:
        log=''

    post=headofficem.objects.filter(username=request.POST['companysearch'])
    if len(post)>0:
        plot_number=post[0].plot_number
        Area=post[0].Area
        City=post[0].City
        Pincode=post[0].Pincode
        Country=post[0].Country
        Phone=post[0].Phone
        email=post[0].email
    else:
        plot_number=''
        Area=''
        City=''
        Pincode=''
        Country=''
        Phone=''
        email=''
        
    post=Workm.objects.filter(username=request.POST['companysearch'])
    if len(post)>0:
        plot_numberw=post[0].plot_number
        Areaw=post[0].Area
        Cityw=post[0].City
        Pincodew=post[0].Pincode
        Countryw=post[0].Country
        Phonew=post[0].Phone
        emailw=post[0].email
    else:
        plot_numberw=''
        Areaw=''
        Cityw=''
        Pincodew=''
        Countryw=''
        Phonew=''
        emailw=''
        
    post=Sales_officem.objects.filter(username=request.POST['companysearch'])
    if len(post)>0:
        plot_numbers=post[0].plot_number
        Areas=post[0].Area
        Citys=post[0].City
        Pincodes=post[0].Pincode
        Countrys=post[0].Country
        Phones=post[0].Phone
        emails=post[0].email
    else:
        plot_numbers=''
        Areas=''
        Citys=''
        Pincodes=''
        Countrys=''
        Phones=''
        emails=''
        

    
    context={'name':request.POST['companysearch'],'logo':log,'picname':piconce,'description':description,'url':url,'plot_number':plot_number,'Area':Area, 'City':City,'Pincode':Pincode, 'Country':Country,'Phone':Phone,'email':email,'plot_numberw':plot_numberw,'Areaw':Areaw, 'Cityw':Cityw,'Pincodew':Pincodew, 'Countryw':Countryw,'Phonew':Phonew,'emailw':emailw,'plot_numbers':plot_numbers,'Areas':Areas, 'Citys':Citys,'Pincodes':Pincodes, 'Countrys':Countrys,'Phones':Phones,'emails':emails,'Position':Position, 'CPI_cut_off':CPI_cut_off, 'Branches':Branches, 'desc':desc}
    template="companysearch.html"
    return render(request,template,context)


def contactview(request):
    language='en-gb'
    session_language= 'en-gb'
    
    if 'lang' in request.COOKIES:
        language=request.COOKIES['lang']
        
    if 'lang' in request.session:
        session_language = request.session['lang']
            
    data = contact.objects.filter(username=request.user.username)
    if len(data)==0:
         # Handle file upload
        if request.method == 'POST':
            
            f=contactform(request.POST,request.FILES)
            if f.is_valid():
                newdoc=f.save(commit=False)
                newdoc.upload_cv=request.FILES['upload_cv']
                newdoc.username = request.user.username
                #newdoc = contact(upload_cv = request.FILES['upload_cv'])
                #newdoc = contact(username = request.user.username)
                newdoc.save()

            context={"form":f,"language":language,"session_language":session_language,'picname':piconce}
            template="contact.html"
            return render(request,template,context,context_instance=RequestContext(request))
        else:
            f=contactform()
            return render(request,"contact.html",{"form":f,"language":language,"session_language":session_language,'picname':piconce},context_instance=RequestContext(request))
    else:
        obj=contact.objects.filter(username=request.user.username)
        t=get_template("profile_contact.html")
        p=t.render(Context({"fullname":(request.user.first_name + " " + request.user.last_name),'obj':obj[0],'picname':piconce,'email':request.user.email,'mobile':data[0].mobile,'temp':data[0].temporary_address,'perm':data[0].permanent_address,'website':data[0].website}))
        return HttpResponse(p)
    

def language(request,language='en-gb'):
    response = HttpResponse("setting languages to %s" % language)
    
    response.set_cookie('lang',language)
    
    request.session['lang'] = language
    
    return response


def internshipview(request):
    f2=internshipform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()

    context={"form2":f2,'picname':''}
    template="internships.html"
    return render(request,template,context)

def postgradview(request):
    f2=postgradform(request.POST)
    
    if f2.is_valid():
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="postgrad.html"
    return render(request,template,context)

def undergradview(request):
    f2=undergradform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="undergrad.html"
    return render(request,template,context)

def srsecview(request):
    f2=srsecform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="srsec.html"
    return render(request,template,context)

def secview(request):
    f2=secform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="sec.html"
    return render(request,template,context)

def languageview(request):
    f2=languageform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="languages.html"
    return render(request,template,context)

def projectview(request):
    f2=projectform(request.POST)
    
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={"form2":f2,'picname':''}
    template="projects.html"
    return render(request,template,context)

def photoview(request):
    
    data = photo.objects.filter(username=request.user.username)
    if len(data)==0:
        
        f=photoform(request.POST,request.FILES)
        if f.is_valid():
        
            new=f.save(commit=False)
            new.username=request.user.username
            new.imagename=request.FILES['upload'].name
            print new.imagename
            new.save()
        context={"form":f,'picname':''}
        template="photo.html"
        return render(request,template,context)
    
    else:
        piconce=data[0].imagename
        t=get_template("profile_photo.html")
        p=t.render(Context({"fullname":(request.user.first_name + " " + request.user.last_name),"picname":data[0].imagename}))
        return HttpResponse(p)



def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('credentials.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()
    print ("url yeeee"+documents[0].docfile.url)
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form,'picname':piconce},
        context_instance=RequestContext(request)
    )

def clist(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('credentials.views.clist'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'clist.html',
        {'documents': documents, 'form': form,'picname':piconce},
        context_instance=RequestContext(request)
    )

##company views

def jobprofile(request):
    f2=jobprofileform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="jobprofile.html"
    return render(request,template,context)

def logoview(request):
    data = logom.objects.filter(username=request.user.username)
    print (request.user.username)
    if len(data)==0:
        print (request.user.username+" this one")
        f=logoform(request.POST,request.FILES)
        if f.is_valid():
            print ("validation")
            new=f.save(commit=False)
            new.username=request.user.username
            new.imagename=request.FILES['upload'].name
            new.save()
        print ("not validation")
        context={"fullname":request.user.username,"form2":f}
        template="logo.html"
        return render(request,template,context)
    
    else:
        t=get_template("logo_see.html")
        p=t.render(Context({"fullname":request.user.username,'logo':data[0].imagename}))
        return HttpResponse(p)


def headoffice(request):
    #if flag==1:
        
    f2=headofficeform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="headoffice.html"
    return render(request,template,context)

def statistics(request):
    f2=statisticsform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="statistics.html"
    return render(request,template,context)

def work(request):
    f2=Workform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="works.html"
    return render(request,template,context)

def media(request):
    f2=mediaform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="media.html"
    return render(request,template,context)

def salesoffice(request):
    f2=Sales_officeform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="salesoffice.html"
    return render(request,template,context)

def benefits(request):
    f2=benefitsform(request.POST)
     
    if f2.is_valid():
             
         
        
        new=f2.save(commit=False)
        new.username = request.user.username
        
        new.save()
    context={'fullname':request.user.username,"form2":f2}
    template="benefits.html"
    return render(request,template,context)


def overview(request):
    f2=overviewform(request.POST)
     
    ob=overviewm.objects.filter(username=request.user.username)
    if len(ob)==0:

        if f2.is_valid():
             
         
        
            new=f2.save(commit=False)
            new.username = request.user.username
        
            new.save()
        context={'fullname':request.user.username,"form2":f2}
        template="overview.html"
        return render(request,template,context)
    else:
        context = {'fullname': request.user.username,'dd':ob[0].description,'u':ob[0].url}
        template = "overview1.html"
        return render(request, template, context)
