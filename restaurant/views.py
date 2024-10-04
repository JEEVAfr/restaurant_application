from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Restaurant, CustomUser, Review, Bookmark
from .serializers import RestaurantSerializer, UserSerializer, ReviewSerializer, BookmarkSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework as django_filters
from django.http import HttpResponse

# Create your views here.

# admin
class RestaurantPagination(PageNumberPagination):
    page_size = 10 

class RestaurantFilter(django_filters.FilterSet):
    rating = django_filters.NumberFilter(field_name='rating', lookup_expr='gte')

    class Meta:
        model = Restaurant
        fields = ['rating']

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and hasattr(request.user, 'is_admin') and request.user.is_admin
    

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all().order_by('name')
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated] 
    pagination_class = RestaurantPagination
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = RestaurantFilter

    def get_permissions(self):
        if self.action in ['create', 'update', 'destroy']:
            return [IsAdmin()]
        return super().get_permissions()

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] 

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all() 
    serializer_class = ReviewSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated and hasattr(self.request.user, 'is_admin') and self.request.user.is_admin:
            return Review.objects.all()
        return Review.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user != request.user:
            return Response({'detail': 'You do not have permission to edit this review.'}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        review = self.get_object()
        if review.user != request.user:
            return Response({'detail': 'You do not have permission to delete this review.'}, status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, *args, **kwargs)

class BookmarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmark.objects.all()

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

def home(request):
    return render(request, 'restaurant/home.html')





