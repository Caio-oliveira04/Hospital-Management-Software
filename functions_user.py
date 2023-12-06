from User import User
import os

user1 = User()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    print('1 - Sign Up')
    print('2 - Login')
    print('3 - Schedule Appointment')
    print('4 - Reschedule Appointment')
    print('5 - Cancel Appointment')
    print('6 - Exit')

    choice = input('Enter the desired option: ')

    clear_screen()  # Clear the screen after the user makes a choice

    if choice == '1':
        name = input('Enter your name: ')
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        user1.set_name(name)
        user1.set_email(email)
        user1.set_password(password)
        user1.register_user(name, email, password)

    elif choice == '2':
        email = input('Enter your email: ')
        password = input('Enter your password: ')
        user1.set_email(email)
        user1.set_password(password)
        user1.login_user(email, password)

    elif choice == '3':
        user1.schedule_appointment()

    elif choice == '6':
        break
