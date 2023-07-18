"""
URL configuration for magazin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from asosiy.views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView

router = DefaultRouter()
router.register("suvlar", SuvModelViewSet)
router.register("mijozlar", MijozModelViewSet)
router.register("adminlar", AdminModelViewSet)
router.register("buyurtmalar", BuyurtmaModelViewSet)
router.register("haydovchilar", HaydovchiModelViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('token_ol/', TokenObtainPairView.as_view()),
    path('token_yangilash/', TokenRefreshView.as_view()),
    path('', include(router.urls)),
    path('apiview_docs/', SpectacularAPIView.as_view(), name="schema"),
    path('docs/', SpectacularSwaggerView.as_view(url_name="schema")),
    path('redoc/', SpectacularRedocView.as_view(url_name="schema")),
    # path('buyurtmalar/', BuyurtmaAPIView.as_view()),
    # path('adminlar/', AdminlarAPIView.as_view()),
    # path('haydovchilar/', HaydovchilarAPIView.as_view()),
    # path('admin_api/<int:pk>/', AdminDetalAPIView.as_view()),
    # path('haydovchi/<int:pk>/', HaydovchiDetalAPIView.as_view()),
]
