# Restaurant Application

## Overview

The Restaurant Application is designed to facilitate the management of restaurant listings and enhance the user dining experience, similar to platforms like Zomato. This application features two user roles: **Administrators** and **Regular Users**.

## Features

### Administrator Functionality
- **Manage Restaurant Listings**: Create, modify, and remove restaurant listings.
- **View All Restaurants**: Access a comprehensive list of all registered restaurants in a convenient list view.
- **User Account Management**: View and manage all user accounts, primarily for customers.

### User Functionality
- **Explore Restaurants**: Browse a paginated list of restaurants with search filters, including ratings greater than 3.5 stars.
- **Bookmark Favorites**: Bookmark favorite restaurants for easy access later.
- **Rate and Review**: Rate restaurants and provide reviews based on personal experiences.
- **Edit/Delete Ratings**: Edit and delete previously submitted ratings and reviews.

## API Endpoints

### Administrator Endpoints (Example)
- **GET /api/restaurants/**: Retrieve all restaurants.
- **POST /api/restaurants/**: Create a new restaurant.
- **PUT /api/restaurants/{id}/**: Update a restaurant.
- **DELETE /api/restaurants/{id}/**: Remove a restaurant.
- **GET /api/users/**: Retrieve all users.
- **PUT /api/users/{id}/**: Update user information.
- **DELETE /api/users/{id}/**: Remove a user account.

### User Endpoints (Example)
- **GET /api/restaurants/**: Retrieve a paginated list of restaurants (with filters).
- **GET /api/restaurants/{id}/**: Get details of a specific restaurant.
- **POST /api/restaurants/{id}/rate/**: Rate a restaurant.
- **POST /api/restaurants/{id}/review/**: Submit a review for a restaurant.
- **PUT /api/reviews/{id}/**: Edit a review.
- **DELETE /api/reviews/{id}/**: Delete a review.
- **POST /api/bookmarks/{id}/**: Bookmark a restaurant.
- **GET /api/bookmarks/**: Retrieve a list of bookmarked restaurants.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant_application.git
   cd restaurant_application
