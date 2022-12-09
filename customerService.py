from logIn import log_in
import pandas as pd
from datetime import datetime

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

        choice = input('Select (1/2/3/4): ')
        if choice == '1':
            title = 'Announcement\n' \
                    '============\n'
            announcement = db.get_list('announcement','*')
            announcement = pd.DataFrame(announcement)
            today_announcement = announcement[announcement['days']==datetime.now().date()]
            pd.set_option('display.max_columns', None)
            print(title)
            print(today_announcement)
            break

        elif choice =='2':
            break
        elif choice =='3':
            break
        elif choice =='4':
            break
        elif choice =='5':
            log_in()
        else:
            print('\nYou put wrong input data. Please enter correct number.\n')