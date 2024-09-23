from django.urls import path
from .views import CourseFormListCreateView,index

urlpatterns = [
    path('courses/', CourseFormListCreateView.as_view(), name='course-form-list-create'),
    path('',index,name="index")
]
