from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Initialize the database
def initialize_database():
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_name TEXT NOT NULL,
        available_till DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ingredient_inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer_suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        suggestion TEXT,
        allergy_concern TEXT
    )
    """)

    connection.commit()
    connection.close()

# Add data to seasonal flavors
def add_seasonal_flavor(flavor_name, available_till):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO seasonal_flavors (flavor_name, available_till) VALUES (?, ?)", 
                   (flavor_name, available_till))
    connection.commit()
    connection.close()

# Add data to ingredient inventory
def add_ingredient(ingredient_name, quantity):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, quantity) VALUES (?, ?)", 
                   (ingredient_name, quantity))
    connection.commit()
    connection.close()

# Add customer suggestions and allergy concerns
def add_customer_suggestion(customer_name, suggestion, allergy_concern):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customer_suggestions (customer_name, suggestion, allergy_concern) VALUES (?, ?, ?)", 
                   (customer_name, suggestion, allergy_concern))
    connection.commit()
    connection.close()

# Fetch all data from a given table
def fetch_table_data(table_name):
    connection = sqlite3.connect("chocolate_house.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()
    connection.close()
    return data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_seasonal_flavor', methods=['POST'])
def add_seasonal_flavor_web():
    flavor = request.form['flavor_name']
    available_till = request.form['available_till']
    add_seasonal_flavor(flavor, available_till)
    return redirect(url_for('view_seasonal_flavors'))

@app.route('/add_ingredient', methods=['POST'])
def add_ingredient_web():
    ingredient = request.form['ingredient_name']
    quantity = request.form['quantity']
    add_ingredient(ingredient, quantity)
    return redirect(url_for('view_ingredient_inventory'))

@app.route('/add_customer_suggestion', methods=['POST'])
def add_customer_suggestion_web():
    name = request.form['customer_name']
    suggestion = request.form['suggestion']
    allergy = request.form['allergy_concern']
    add_customer_suggestion(name, suggestion, allergy)
    return redirect(url_for('view_customer_suggestions'))

@app.route('/view_seasonal_flavors')
def view_seasonal_flavors():
    data = fetch_table_data("seasonal_flavors")
    return render_template('view_seasonal_flavors.html', data=data)

@app.route('/view_ingredient_inventory')
def view_ingredient_inventory():
    data = fetch_table_data("ingredient_inventory")
    return render_template('view_ingredient_inventory.html', data=data)

@app.route('/view_customer_suggestions')
def view_customer_suggestions():
    data = fetch_table_data("customer_suggestions")
    return render_template('view_customer_suggestions.html', data=data)

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)
