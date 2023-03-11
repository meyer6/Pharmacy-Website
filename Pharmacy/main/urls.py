from django.urls import path
from main import views
urlpatterns = [
]
for menu in views.allMenus:
    urlpatterns.append(path(menu.name.replace(" ", "")+"/", views.main))
