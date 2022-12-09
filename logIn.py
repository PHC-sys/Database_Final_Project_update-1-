from dbModule import Database
import pymysql
import sys
import pandas as pd
from deleteData import delete_data
from everyday_update import everyday_update

db = Database()

everyday_update(db)

def log_in(db):
    while True:
        new_welcome = 'Welcome to Yonsei Buffet!\n' \
                      '=========================\n' \
                      'Service\n' \
                      '1. Log In\n' \
                      '2. Sign UP\n' \
                      '3. Exit\n' \
                      '=========================\n'
        print(new_welcome)
        answer = input('Select (1/2/3) : ')


        if answer == '1':
            id = input('ID: ')
            pw = input('PW: ')
            result = db.logcheck(id,pw)
            #print(result)
            if result is False:
                print('\nWrong Information. Please check again.\n')
            else:
                print('\n',result[1])
                break

        elif answer == '2':
            PhoneNumber = input('Enter your Phone Number: ')
            SchoolMail = input('Enter your Email: ')
            new_id = input('Your New ID: ')
            new_pw = input('Password: ')

            #Insert Database
            try:
                db.sign_up(PhoneNumber, new_id, new_pw, SchoolMail)
                print('\nComplete! Enjoy our Service!\n')

            except pymysql.err.OperationalError as e:
                print('\nOperationError: Enter correct value\n')

        elif answer == '3':
            print('Have a nice day!')
            db.close()
            sys.exit()
        else:
            print('\nYou put wrong input data. Please enter correct number.\n')

    customer_service(db)

def customer_service(db):
    while True:
        service_page = 'How can I help you?\n' \
                       '===================\n' \
                       '1. Announcement\n' \
                       '2. Demand Survey\n' \
                       '3. Menu Evaluation\n' \
                       '4. Withdrawal\n' \
                       '5. Go Back\n' \
                       '===================\n'
        print(service_page)

        choice = input('Select (1/2/3/4/5): ')
        if choice == '1':
            title = 'Announcement\n' \
                    '==============================================================================\n'
            announcement = db.get_list('announcement','*')
            recent_day = announcement[-1]['days']
            announcement = pd.DataFrame(announcement)
            #print(announcement)

            today_announcement = announcement.iloc[-2:]
            pd.set_option('display.max_columns', None)
            print(title)
            print(today_announcement,'\n')
            print('==============================================================================\n')
            break

        elif choice =='2':
            #Demand Survey
            break

        elif choice =='3':
            #Menu Evaluation
            break

        elif choice =='4':
            result = delete_data(db, 'customer')
            if result is False:
                print('Please enter correct information\n')
                customer_service(db)
            else:
                print(f'Thank you for your use, {result}.')
            db.close()
            sys.exit()

        elif choice =='5':
            log_in(db)

        else:
            print('\nYou put wrong input data. Please enter correct number.\n')

log_in(db)
customer_service(db)
db.close()
