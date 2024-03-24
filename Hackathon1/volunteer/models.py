#here we need to create Django models (classes) based on our backend code
from django.db import models
import psycopg2
from sheets_api import get_google_sheet_values

# the class is the column in DB
class AddUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

# the class is the column in DB
class Records():
    def __init__(self, user_city):
        self.values = self.get_google_sheet_values()
        self.matching_opportunities = []
        self.user_city = user_city

    def get_google_sheet_values(self):
        # Call the function from sheets_api module to fetch values from Google Sheets
        return get_google_sheet_values()

#here we have to put all the logic :)
    def find_matching_opportunities(self):
        for value in self.values:
            if value[1] == self.user_city:
                self.matching_opportunities.append(value)









# class addUser:
#     def __init__(self,first_name, last_name, email, phone, city):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.phone = phone
#         self.city = city 
#         self.conn = psycopg2.connect(
#             dbname = test_config.DATABASE,
#             user = test_config.USERNAME, 
#             password = test_config.PASSWORD,
#             host = test_config.HOSTNAME, 
#             port = test_config.PORT
#         )
#     def add_user_to_db(self):
#         cursor = self.conn.cursor()
#         query = """
# INSERT INTO users(first_name, last_name, email, phone, city) Values (%s,%s,%s,%s,%s)"""
#         cursor.execute(query,(self.first_name, self.last_name, self.email, self.phone, self.city))
#         self.conn.commit()
#         cursor.close()
#         self.conn.close()
    
#     def get_user_info(self):
#         conn = psycopg2.connect(
#             dbname=test_config.DATABASE,
#             user=test_config.USERNAME, 
#             password=test_config.PASSWORD,
#             host=test_config.HOSTNAME, 
#             port=test_config.PORT
#         )
#         cursor = conn.cursor()
#         query = """
#         SELECT * FROM users ORDER BY timestamp DESC LIMIT 1;
#         """
#         cursor.execute(query)
#         user_info_list = []
#         for row in cursor.fetchall():
#             for item in row:
#                 user_info_list.append(item)  # Append each item to the list
#         cursor.close()
#         conn.close()
#         return user_info_list



    # def get_user():
    #     name_pattern = r'^[A-Za-z\'\- ]+$'
    #     email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    #     phone_pattern = r'^\d{10}$'
    #     city_pattern = r'^[A-Za-z\'\- ]+$'

    #     print('Welcome volunteer, please follow the following prombpts to get your volunteer matches:')

    #     first_name = get_valid_input("Please enter your first name: ", name_pattern)
    #     last_name = get_valid_input("Please enter your last name: ", name_pattern)
    #     email = get_valid_input("Please enter your email: ", email_pattern)
    #     phone = get_valid_input("Please enter your phone number: ", phone_pattern)
    #     city = get_valid_input("Please enter your city: ", city_pattern)
        
    #     new_user = addUser(first_name, last_name, email, phone, city)
    #     new_user.add_user_to_db()
    #     user_info = new_user.get_user_info()

    #     # print(user_info)

    #     values = get_google_sheet_values()
    #     matching_opportunities = []
    #     user_city = user_info[5]
    #     correct_case_city = string.capwords(user_city)

    #     for value in values:
    #         if value[1] == correct_case_city:
    #             matching_opportunities.append(value)

    #     if matching_opportunities:
    #         print("We found some matches in your city:")
    #         for index, opportunity in enumerate(matching_opportunities, start=1):
    #             print(f"{index}. {opportunity}")
            
    #         # Prompt user for choosing opportunity
    #         while True:
    #             try:
    #                 selected_index = int(input("Please select the number of the opportunity you want to choose: "))
    #                 if 1 <= selected_index <= len(matching_opportunities): #checks if user selected greater than 1 and less than the amount of choices
    #                     selected_opportunity = matching_opportunities[selected_index - 1]
    #                     print(f"You selected: {selected_opportunity}")
                        
    #                     conn = psycopg2.connect(
    #                         dbname=test_config.DATABASE,
    #                         user=test_config.USERNAME, 
    #                         password=test_config.PASSWORD,
    #                         host=test_config.HOSTNAME, 
    #                         port=test_config.PORT
    #                     )
    #                     cursor = conn.cursor()
                        
    #                     # Insert selected opportunity name into the records table
    #                     opportunity_name = selected_opportunity[0]
    #                     opportunity_description = selected_opportunity[2]

    #                     query ='''INSERT INTO records (user_id, organization_chosen, description) VALUES(%s, %s, %s)''' #modify this querry
    #                     cursor.execute(query, (user_info[0], opportunity_name, opportunity_description))
                        
    #                     conn.commit()
    #                     cursor.close()
    #                     conn.close()
                        
    #                     break
    #                 else:
    #                     print("Invalid input. Please enter a valid number.")
    #             except ValueError:
    #                 print("Invalid input. Please enter a number.")
    #     else:
    #         print("No matching opportunities found in your city.")



    # if __name__ == "__main__":

    #     get_user()
