from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('signup', views.register, name='signup'),
    path('login', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dash'),
    path('course/<int:course_id>', views.buy_course, name='buy_course'),
    path('enrolled', views.enrolled_courses, name='enrolled'),
    path('logout', views.logout_view, name='logout'),
    path('buy', views.buy, name='buy'),
]
