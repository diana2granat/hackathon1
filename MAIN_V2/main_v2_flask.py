from flask import Flask, render_template, request, redirect, url_for
from add_user import addUser
from sheets_api import get_google_sheet_values
import config_file
from config_key import api_key
import psycopg2
import re

app = Flask(__name__)

import re

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Define regex patterns for validation
        name_pattern = r'^[A-Za-z\'\- ]+$'
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        phone_pattern = r'^\d{10}$'
        city_pattern = r'^[A-Za-z\'\- ]+$'

        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']

        # Validate input using regex patterns
        error_messages = []
        if not re.match(name_pattern, first_name):
            error_messages.append("First name: letters only")
        if not re.match(name_pattern, last_name):
            error_messages.append("Last name: letters only")
        if not re.match(email_pattern, email):
            error_messages.append("Email: use @ and .com")
        if not re.match(phone_pattern, phone):
            error_messages.append("Phone number: 10 numbers please, no special characters")
        if not re.match(city_pattern, city):
            error_messages.append("City: letters and spaces only")

        # If there are validation errors, render index.html with error messages and input values
        if error_messages:
            return render_template('index.html', error_messages=error_messages, first_name=first_name, last_name=last_name, email=email, phone=phone, city=city)

        # Add user to the database if input is valid
        new_user = addUser(first_name, last_name, email, phone, city)
        new_user.add_user_to_db()

        # Get user info and matching opportunities
        user_info = new_user.get_user_info()
        values = get_google_sheet_values()
        matching_opportunities = []
        user_city = user_info[5]
        correct_case_city = user_city.title()

        for value in values:
            if value[1] == correct_case_city:
                matching_opportunities.append(value)

        # Render the template with the required data
        return render_template('results.html', user_info=user_info, opportunities=matching_opportunities)

    return render_template('index.html')


@app.route('/record_selection', methods=['POST'])
def record_selection():
    if request.method == 'POST':
        user_id = request.form['user_id']
        opportunity_name = request.form['opportunity_name']
        opportunity_description = request.form['opportunity_description']
        
        # Connect to the database
        conn = psycopg2.connect(
            dbname=config_file.DATABASE,
            user=config_file.USERNAME, 
            password=config_file.PASSWORD,
            host=config_file.HOSTNAME, 
            port=config_file.PORT
        )
        cursor = conn.cursor()

        try:
            # Insert the user's selection into the records table
            query = 'INSERT INTO records (user_id, organization_chosen, description) VALUES (%s, %s, %s)'
            cursor.execute(query, (user_id, opportunity_name, opportunity_description))
            conn.commit()
            return "Selection recorded successfully!"
        except psycopg2.Error as e:
            # Handle any errors that occur during database insertion
            conn.rollback()
            return f"Error: {e}"

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

if __name__ == "__main__":
    app.run(debug=True)