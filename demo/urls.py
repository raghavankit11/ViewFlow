"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.views import generic
from material.frontend import urls as frontend_urls
from viewflow.flow.viewset import FlowViewSet
from helloworld.flows import ResponseSubmissionProcess

urlpatterns = [
    path(r'', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
    path(r'', include(frontend_urls)),
    path('admin/', admin.site.urls),
    path('helloworld/', include('helloworld.urls')),
    path('field_response/', admin.site.urls, name='field-response'),
]