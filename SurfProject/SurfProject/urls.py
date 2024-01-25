
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from SurfProject.SPOT import views


router = DefaultRouter()

router.register(r"Session",views.SessionView)

router.register(r"Surfer",views.SurferView)

router.register(r"CreateSufer",views.CreateSurfView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include(router.urls))
]
