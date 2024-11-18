from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomLoginView, dashboard, graph1, graph2,graph3

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('graph1/', views.graph1, name='graph1'),
    path('graph2/', views.graph2, name='graph2'),
    path('graph3/', views.graph3, name='graph3'),
    path('map/', views.map, name='map'),
    path('save-sensor-data/', views.save_sensor_data, name='save_sensor_data'),
    path('fetch-sensor-data/', views.fetch_sensor_data, name='fetch_sensor_data'),
    path('save-ambient-sensor-data/', views.save_ambient_sensor_data, name='save_ambient_sensor_data'),
    path('fetch-ambient-sensor-data/', views.fetch_ambient_sensor_data, name='fetch_ambient_sensor_data'),
    path('save-soil-sensor-data/', views.save_soil_sensor_data, name='save_soil_sensor_data'),
    path('fetch-soil-sensor-data/', views.fetch_soil_sensor_data, name='fetch_soil_sensor_data'),
    path('generate-report/', views.generate_report, name='generate_report'),
    path('adminDashboard/', views.admin_dashboard, name='admin'),
    path('toggle-fetching/', views.toggle_fetching, name='toggle_fetching'),
    path('report/', views.report, name='report'),
]
