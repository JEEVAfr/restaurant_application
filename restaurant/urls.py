from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'reviews', views.ReviewViewSet, basename='review')
router.register(r'bookmarks', views.BookmarkViewSet)

urlpatterns = router.urls