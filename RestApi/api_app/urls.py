from django.urls import path
from .views import studentz,studentttt
from .views import studentclass,StudentDetail,class_simpleway,class_simpleway_Detail
from rest_framework.routers import DefaultRouter
from django.urls import path, include

from . import views

router = DefaultRouter()
router.register(r'viewset', views.studentViewSet, basename='viewset'),
router.register(r'modelviewset', views.student_model_ViewSet, basename='modelviewset')



urlpatterns = [
    path('index',studentz,name='index'),
    path('home/<pk>',studentttt,name='home'),
    path('class_student',studentclass.as_view(),name='class_student'),
    path('student_details/<pk>',StudentDetail.as_view(),name='studentdetails'),
    path('class_simple',class_simpleway.as_view(),name='class_simple'),
    path('simpleway_details/<pk>',class_simpleway_Detail.as_view(),name='simpleway_details'),
    path('viewset', include(router.urls)),



]
