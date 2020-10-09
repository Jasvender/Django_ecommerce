from django.urls import path
from .views import (
                    AccountHomeView,
                    )
app_name = "carts"
urlpatterns = [
    path('', AccountHomeView.as_view(), name="home"),

]
