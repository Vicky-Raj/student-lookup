from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('student/<int:pk>/detail/',views.detail_page,name='detail'),
    path('student/<int:pk>/edit/',views.student_edit,name='student-edit'),
    path('student/<int:pk>/delete/',views.student_delete,name='student-delete'),
    path('student/create/',views.stduent_create,name='student-create')
]