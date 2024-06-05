Travel Website with Django and Rasa Chatbot
Overview
This project is a comprehensive travel website built using Django, integrated with a Rasa chatbot to provide users with an interactive and personalized experience. The website allows users to explore travel destinations, book trips, and get real-time assistance from the chatbot.

Features
Django Backend: Robust and scalable backend using Django, a high-level Python web framework.
Rasa Chatbot: Integrated Rasa chatbot for personalized user interactions and travel assistance.
User Authentication: Secure user login and registration system.
Travel Listings: Browse and search for various travel destinations and packages.
Booking System: Easy and intuitive booking process for travel plans.
Admin Panel: Manage travel listings, bookings, and user data through a Django admin interface.
Responsive Design: Mobile-friendly design to ensure a great user experience on all devices.
Technologies Used
Django: For backend development and web framework.
Rasa: For the chatbot and natural language processing.
HTML/CSS/JavaScript: For frontend development.
SQLite/PostgreSQL: For database management.

How to use the website 
open chatbot folder in cmd
cmd 1
rasa run actions
cmd 2
rasa run -m models --enable-api --cors "*" --debug

open website folder in cmd
cmd 3 
py manage.py runserver
