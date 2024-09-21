WeatherApp
A Django-based web application that allows users to search for any city and retrieve current weather information along with a 5-day forecast.

Features
Search for weather by city name
Display current weather conditions
Show a 5-day weather forecast
Responsive design for both desktop and mobile

Technologies Used
Django
Python
HTML/CSS
JavaScript
OpenWeather API for weather data

Installation
Prerequisites
Make sure you have the following installed:

Python 3.x
Django
Git

Clone the Repository

git clone 
cd weatherapp
Create a Virtual Environment

python -m venv myenv
source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`

Install Dependencies
pip install -r requirements.txt
Set Up Environment Variables

Create a .env file in the root directory and add your OpenWeather API key:

API_KEY=your_api_key_here
SECRET_KEY=your_secret_key_here
DEBUG=True
Database Migrations

Run the following commands to set up the database:


python manage.py makemigrations
python manage.py migrate

Run the Development Server

python manage.py runserver
Navigate to http://127.0.0.1:8000 in your web browser to access the app.

Usage
Enter the name of the city you want to check the weather for in the search bar.
Click the "Search" button.
View the current weather and the 5-day forecast displayed on the screen.
