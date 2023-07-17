"""
URL configuration for Airline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from home import views

urlpatterns = [
    #Customer URLs
    path("", views.index, name='home'),  
    path('book', views.initialBook, name='Booking Details'),  
    path("booking/<int:flightno>/<NoOfPassengers>/", views.finalBook, name='Final Booking'),  
    path("cancel", views.cancel, name='cancel booking'),  
    path("change", views.change, name='change booking'),  
    path("track", views.track, name='track reservation'), 
    path("about", views.about, name='about us'),  
    path('registration', views.registration_request, name='registration'),
    path("faq", views.faq, name='faq'),
    
    #Employee URLs
    path("EmpHome", views.EmpIndex, name='EmpIndex'),
    path("EmpProfile", views.EmpProfile, name='EmpProfile'),
    path("EmpFlights", views.EmpFlights, name='EmpFlights'),
    path("EmpPolicy", views.EmpPolicy, name='EmpPolicy'),
    path("travel", views.travel, name='travel'),
    path("health", views.health, name='health'),
    path("assist", views.assist, name='assist'),
    path("bonus", views.bonus, name='bonus'),
    path("discount", views.discount, name='discount'),
    path("life", views.life, name='life'),
    path("retire", views.retire, name='retire'),
    path("train", views.train, name='train'),
    path("wellness", views.wellness, name='wellness'),

    #Authentication
    path("logout", views.logout_request, name='logout'),
    path("login", views.login_request, name='login'),
]  