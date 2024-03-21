import psycopg2
from config_copy import api_key
from testing_add_user import addUser
import re 
from sheets_api_testing import get_google_sheet_values

# global_user_info = None  # Initialize global_user_info

def get_valid_input(prompt, pattern):
    while True:
        user_input = input(prompt)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def get_user():
    name_pattern = r'^[A-Za-z\'\- ]+$'
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    phone_pattern = r'^\d{10}$'
    city_pattern = r'^[A-Za-z\'\- ]+$'

    print('Welcome volunteer, please follow the following prombpts to get your volunteer matches:')

    first_name = get_valid_input("Please enter your first name: ", name_pattern)
    last_name = get_valid_input("Please enter your last name: ", name_pattern)
    email = get_valid_input("Please enter your email: ", email_pattern)
    phone = get_valid_input("Please enter your phone number: ", phone_pattern)
    city = get_valid_input("Please enter your city: ", city_pattern)
    
    new_user = addUser(first_name, last_name, email, phone, city)
    new_user.add_user_to_db()
    user_info = new_user.get_user_info()

    # print(global_user_info)

    # if global_user_info is None:
    #     print("User info is not available. Please run show_user_menu() first.")
    #     return

    values = get_google_sheet_values()
    matching_opportunities = []
    user_city = user_info[5]

    for value in values:
        if value[1] == user_city:
            matching_opportunities.append(value)

    if matching_opportunities:
        print("We found some matches in your city:")
        for index, opportunity in enumerate(matching_opportunities, start=1):
            print(f"{index}. {opportunity}")
        
        # Prompt user for choosing opportunity
        while True:
            try:
                selected_index = int(input("Please select the number of the opportunity you want to choose: "))
                if 1 <= selected_index <= len(matching_opportunities):
                    selected_opportunity = matching_opportunities[selected_index - 1]
                    print(f"You selected: {selected_opportunity}")
                    break
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("No matching opportunities found in your city.")



if __name__ == "__main__":

    get_user()
