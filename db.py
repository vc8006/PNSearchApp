import csv
import requests
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PNSearchApp.settings')
django.setup()

from searchApp.models import Dish

def populate_database():
    csv_url = 'https://python-exercise.s3.ap-south-1.amazonaws.com/restaurants_small.csv'
    response = requests.get(csv_url)
    lines = response.text.splitlines()
    csv_reader = csv.reader(lines)
    next(csv_reader)  # Skip header row
    
    for row in csv_reader:
        name = row[1]
        location = row[2]
        items = row[3]
        lat_long = row[4]
        full_details = row[5]
        
        # Create Dish instance and save to database
        dish = Dish(name=name, location=location, items=items, lat_long=lat_long, full_details=full_details)
        dish.save()

if __name__ == '__main__':
    populate_database()
