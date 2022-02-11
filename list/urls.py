from django.urls import path

from list.api.views.list import ListView
app_name = "list"
urlpatterns = [
    path("", ListView.as_view(), name="index")
]
