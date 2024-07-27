from django.urls import path
from .views import studentz,studentttt
from .views import studentclass,StudentDetail,class_simpleway,class_simpleway_Detail
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views


# viewset router

router = DefaultRouter()
router.register(r'view1', views.studentViewSet, basename='view1'),
router.register(r'modelviewset', views.student_model_ViewSet, basename='modelviewset')


urlpatterns = [

# function views 
    path('index',studentz,name='index'),
    path('home/<pk>',studentttt,name='home'),

# class views
    path('class_student',studentclass.as_view(),name='class_student'),
    path('student_details/<pk>',StudentDetail.as_view(),name='studentdetails'),
    path('class_simple',class_simpleway.as_view(),name='class_simple'),
    path('simpleway_details/<pk>',class_simpleway_Detail.as_view(),name='simpleway_details'),

#  view set
    path('api_view/', include(router.urls)),

]
