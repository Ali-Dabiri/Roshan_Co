from django.urls import path
from .views import News_View

urlpatterns = [
    path("api/News_Page/", News_View.as_view(), name="News-Page"),
]
