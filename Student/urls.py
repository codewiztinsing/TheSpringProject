from django.urls import path,include
from .views import StudentView,UserViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('students', StudentView, basename='students')
router.register('users', UserViewSet)



urlpatterns = [

	path('api/', include(router.urls))
			
]