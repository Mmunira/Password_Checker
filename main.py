
class PasswordChecker:
    def take_input(self):
        #Take full user name, year of birth. as user what option (generate, check, or exit).
        while True:
            options_choices = input('please enter one of the following options: check password(1), generate password(2) or exit()3 ')

            if options_choices == ('3'):
                password = input('exit password')
                break
            first_name = input('Enter your first name:')
            last_name = input('Enter your last name:')
            birth_year = input('Enter your year of birth:')
            # options_choices = input('please enter one of the following options: check password, generate password or exit ')
            if options_choices == ('1'):
                password = input('Please input password to check: ')
            elif options_choices == ('2'):
                continue
            else:
                print ('Please choose a valid option')
password_checker = PasswordChecker()
password_checker.take_input()
