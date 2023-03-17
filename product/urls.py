from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductView

router = DefaultRouter()
router.register('', ProductView)
# router.register('category', CategoryView)

urlpatterns = []

urlpatterns += router.urls
