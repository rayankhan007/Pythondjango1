from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.hello, name='hello'),
    path('index/', views.index, name='index'),
    path('data/', views.data, name='data'),
    # path('test/', views.test, name='test'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('my_login/', views.my_login, name='my_login'),
    path('my_logout/', views.my_logout, name='my_logout'),
    path('admin_panel/', views.admin_panel, name='admin'),
    path('', views.main, name='main'),
    path('signup/', views.signup, name='signup'),
]
