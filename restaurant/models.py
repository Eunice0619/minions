from django.db import models
from django.db.models import Avg

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    user_type = models.CharField(max_length=15)  # "식당", "관리자"

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=20)
    location = models.CharField(max_length=120)
    event = models.CharField(max_length=100)

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=500)
    date = models.DateField()

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
    rating = models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])

def calculate_average_rating():
    average_rating = Food.objects.aggregate(Avg('rating')) ['rating_avg']
    return average_rating

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    review_text = models.TextField()

class SuggestionBoard(models.Model):
    post_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    post_content = models.TextField()