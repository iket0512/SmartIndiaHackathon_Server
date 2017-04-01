"""SmartIndiaHackathon_Server URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from search.views import search,tab_titles
from list_data.views import list1
from surveys.views import *
from login.views import *
from list_data import *
from user_datas.views import *
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search/', search),
    url(r'^list/', list1),
    url(r'^inst_signup/', prof_signup),
    url(r'^user_login/', student_login),
    url(r'^get_tabs/', tab_titles),
    url(r'^inst_login/', prof_login),
    url(r'^survey_upload/',survey_upload),
    url(r'^pro_upload/', add_details),
    url(r'^filter/', list1),
]
from django.conf import settings
from django.conf.urls.static import static
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

