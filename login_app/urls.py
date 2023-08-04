from django.urls import path
from login_app import views

urlpatterns =[
    path("",views.render_login,name="render_login"),
    path("perform_login",views.perform_login, name="perform_login"),
    path("perform_logout",views.perform_logout, name="perform_logout"),
    path("admin_dashboard",views.admin_dashboard, name="admin_dashboard")
]