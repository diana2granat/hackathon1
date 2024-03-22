import psycopg2
import test_config as test_config
from test_config_copy import api_key
from testing_add_user import addUser
import re 
from sheets_api_testing import get_google_sheet_values
import string 



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

    # print(user_info)

    values = get_google_sheet_values()
    matching_opportunities = []
    user_city = user_info[5]
    correct_case_city = string.capwords(user_city)

    for value in values:
        if value[1] == correct_case_city:
            matching_opportunities.append(value)

    if matching_opportunities:
        print("We found some matches in your city:")
        for index, opportunity in enumerate(matching_opportunities, start=1):
            print(f"{index}. {opportunity}")
        
        # Prompt user for choosing opportunity
        while True:
            try:
                selected_index = int(input("Please select the number of the opportunity you want to choose: "))
                if 1 <= selected_index <= len(matching_opportunities): #checks if user selected greater than 1 and less than the amount of choices
                    selected_opportunity = matching_opportunities[selected_index - 1]
                    print(f"You selected: {selected_opportunity}")
                    
                    conn = psycopg2.connect(
                        dbname=test_config.DATABASE,
                        user=test_config.USERNAME, 
                        password=test_config.PASSWORD,
                        host=test_config.HOSTNAME, 
                        port=test_config.PORT
                    )
                    cursor = conn.cursor()
                    
                    # Insert selected opportunity name into the records table
                    opportunity_name = selected_opportunity[0]
                    opportunity_description = selected_opportunity[2]


                    query ='''INSERT INTO records (user_id, organization_chosen, description) VALUES(%s, %s, %s)''' #modify this querry
                    cursor.execute(query, (user_info[0], opportunity_name, opportunity_description))
                    
                    conn.commit()
                    cursor.close()
                    conn.close()
                      
                    break
                else:
                    print("Invalid input. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        print("No matching opportunities found in your city.")



if __name__ == "__main__":

    get_user()
