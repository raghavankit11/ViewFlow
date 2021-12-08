from django.conf.urls import url, include
from django.urls import path
from viewflow.flow.viewset import FlowViewSet
from .flows import ResponseSubmissionFlow


customflow_urls = FlowViewSet(ResponseSubmissionFlow).urls

app_name = 'parcel'
urlpatterns = [
     # url(r'^delivery/', include((delivery_urls, 'delivery')))
     path('customflow/', include((customflow_urls, 'customflow')))
]