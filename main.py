
class PasswordChecker:
    def take_input(self):
        #Take full user name, year of birth. as user what option (generate, check, or exit).
        user_choice = None
        while True:
            options_choices = input('please enter one of the following options: check password(1), generate password(2) or exit()3 ')

            if options_choices in ('1', '2', '3'):
                user_choice = options_choices
                break
            else:
                print('Please choose a valid option')

        if user_choice == '3':
            exit(0)

        first_name = input('Enter your first name:')
        last_name = input('Enter your last name:')
        birth_year = input('Enter your year of birth:')

        if user_choice == '1':
            password = input('Please input password to check: ')
        elif user_choice == '2':
            pass


password_checker = PasswordChecker()
password_checker.take_input()

