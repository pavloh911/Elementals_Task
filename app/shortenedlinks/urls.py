from django.urls import path, include
from .views import \
    SLinkCreateView, \
    SLinkView, \
    SLinkCreateViewAdmin, \
    SLinkViewAdmin, \
    UserCreateView, \
    redirecto

urlpatterns = [
    path('admin/<int:pk>/', SLinkViewAdmin.as_view()),
    path('admin/create/', SLinkCreateViewAdmin.as_view()),
    path('user/<int:pk>/', SLinkView.as_view()),
    path('user/create/', SLinkCreateView.as_view()),
    path('register/', UserCreateView.as_view()),
    path('<int:into>/', redirecto),
]