"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from siteapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('home/',views.home_view),
    path('info/',views.info_view),
    path('services/',views.services_view),
    path('help/',views.help_view),
    path('register/',views.register_veiw),
    path('regconf/',views.regconf_view),
    path('transfer/',views.update_view),
    url(r'^$',views.home_view),

]

