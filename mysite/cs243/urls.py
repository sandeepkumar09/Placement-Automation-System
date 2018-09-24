"""cs243 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,patterns,include
from django.contrib import admin
from cs243.view import login,index2,studentprofile,ex
from credentials.views import companysearch,internshipview,contactview,languageview,projectview,postgradview,undergradview,srsecview,secview,language,overview,photoview,search,studentsearch,statistics,jobprofile,logoview,media,headoffice,work,salesoffice,benefits#,companysearch
from django.conf import settings
from django.conf.urls.static import static


   
urlpatterns = patterns('',
     (r'^', include('credentials.urls')),(r'^admin/', admin.site.urls),
     (r'^login/$', login),
      (r'^index2/$', 'cs243.view.loggedin'),
       (r'^studentprofile/$', studentprofile),
       (r'^photo/$', photoview),
       (r'^profile_photo/$', 'cs243.view.profile_photo'),
          (r'^postgrad/$', postgradview),
          (r'^undergrad/$', undergradview),
          (r'^srsec/$', srsecview),
          (r'^sec/$', secview),
          (r'^internships/$', internshipview),
          (r'^languages/$', languageview),
          (r'^contact/$', contactview),
          (r'^projects/$', projectview),
          (r'^language/(?P<language>[a-z\-]+)/$', language),
          (r'^auth/$', 'cs243.view.auth_view'),
          (r'^cauth/$', 'cs243.view.c_auth_view'),
          (r'^invalid/$', 'cs243.view.invalid_login'),
          (r'^loggedin/$', 'cs243.view.loggedin'),
          (r'^cloggedin/$', 'cs243.view.c_loggedin'),
          (r'^register/$', 'cs243.view.register_user'),
          (r'^register_success/$', 'cs243.view.register_success'),
          (r'^profile_contact/$', 'cs243.view.profile_contact'),
          (r'^search/$', search),
          (r'^studentsearch/$', studentsearch),
          (r'^companysearch/$', companysearch),
          (r'^overview/$',overview ),
          (r'^logo/$', logoview),
          (r'^statistics/$', statistics),
          (r'^job/$', jobprofile),
          (r'^salesoffice/$', salesoffice),
          (r'^headoffice/$', headoffice),
          (r'^media/$', media),
          (r'^works/$', work),
          (r'^benefits/$', benefits),
          (r'file:///C:/Users/Sagar Roy Prodhan/Desktop/cs243/mysite/credentials/media/uploaded_files/1460525607_91_CV_Sagar_Roy_Prodhan.pdf$', ex),
 ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)