from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name='starting-page'),
    path("<slug:slug>", views.book_detail, name='book-detail-page'),
]