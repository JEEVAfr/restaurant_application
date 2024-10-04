from rest_framework import serializers
from .models import Restaurant, CustomUser, Review, Bookmark

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser 
        fields = ['id', 'username', 'email', 'first_name', 'last_name']  # Specify fields to include

    def validate_email(self, value):
        """Ensure email is unique."""
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'location', 'cuisine_type'] 

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  

    class Meta:
        model = Review
        fields = ['id', 'user', 'restaurant', 'review_text', 'rating']

class BookmarkSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username') 

    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'restaurant'] 