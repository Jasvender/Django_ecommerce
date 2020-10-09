from django.urls import path
from .views import (
                        BlogListView,
                        BlogDetailSlugView,
                    )
app_name = "blogs"
urlpatterns = [
    path('', BlogListView.as_view(), name="list"),
    path('<slug:slug>/', BlogDetailSlugView.as_view(), name="detail" ),

]
