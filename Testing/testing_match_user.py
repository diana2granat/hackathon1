import config
import psycopg2

opportunities = [['tomer farm', 'Jerusalem', 'pick oranges on tomers farm'], ['tel aviv farm', 'Tel Aviv', 'pick oranges in tel aviv']]
user = ['Jeremy','Gross', '0555555555', 'email@email.com', 'Jerusalem']

def match_user():
    for opportunity in opportunities:
        for index,item in enumerate(opportunity):
            if index == 1 and item == user[4]:
                print("We found some matches in your city: ")
                print(f'{opportunity[0]} in {opportunity[1]} where you can {opportunity[2]}')
                
