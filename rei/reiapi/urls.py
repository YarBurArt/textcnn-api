from django.urls import include, path
from rest_framework import routers

from . import views  # relative import

# add class question as function
router = routers.DefaultRouter()
router.register(r'question', views.QuestionViewSet)

# app url router
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
