import psycopg2

class UserInterface:
    
    def show_user_menu():
        user_input = input(f' This program is used to help you find volunteering please enter your first name, last name, email, city, and phone number seperated by commas  (e.g., "John Doe, johndoe@gmail.com, Jerusalem, 0555555555")')
        first, last, email, city, phone = user_input.split(',')
        first = first.strip()
        last = last.strip()
        email = email.strip()
        city = city.strip()
        phone = phone.strip()
        return first, last, email, city, phone

    

# user1 = UserInterface(name, city, email, phonenumber)
