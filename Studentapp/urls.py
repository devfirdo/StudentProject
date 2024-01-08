from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('submit',views.submit,name='submit'),
    path('submission',views.submission,name='submission'),
    path('studentdetails',views.studentdetails,name='studentdetails'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('update/<int:pk>',views.update,name='update'),
    path('personal/<int:pk>',views.personal,name='personal'),  
]