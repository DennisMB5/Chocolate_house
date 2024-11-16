# Chocolate House System

This is a simple Python application for managing a chocolate house. It helps you manage seasonal flavors, ingredient inventory, and customer suggestions.

## Features

 **Add Seasonal Flavors**: Add new seasonal chocolate flavors.
 **Add Ingredients**: Manage ingredients and their quantities.
 **Customer Suggestions**: Collect customer flavor suggestions and allergy concerns.
 **View Data**: View seasonal flavors, ingredient inventory, and customer suggestions.

## Prerequisites

 Python 3.x installed.
 Flask installed (`pip install flask`).

## Installation

1. Clone the repository:
   
   git clone https://github.com/DennisMB5/Chocolate_house.git

   cd chocolate-house

2. Run the application: Start the Flask application:

   python app.py

3. Access the app: Open a web browser and go to:

   http://127.0.0.1:5000/
   
## Docker Setup

1. Build the Docker image: 

   docker build -t chocolate-house .

2. Run the Docker container:
   
   docker run -p 5000:5000 chocolate-house

3. Access the app: 
   
   http://127.0.0.1:5000/
   