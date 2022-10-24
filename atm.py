print('Welcome to Fake Bank ATM')
restart = ('Y')
chances = 3
balance = 00.01
while chances >= 0:
    pin = int(input('Please Enter Your 4 Digit PIN: '))
    if pin == (1234):
        print('You entered your pin correctly\n')
        while restart not in ('n', 'NO', 'no', 'N'):
            print('Please Press 1 For Your Balance\n')
            print('Please Press 2 To Make a Withdrawl\n')
            print('Please Press 3 To Make a Deposit\n')
            print('Please Press 4 To Return Card\n')
            option = int(input('Choice: '))
            if option == 1:
                print('Your Balance is, $', balance, '\n')
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 2:
                option2 = ('Y')
                withdrawl = float(input('How Much Would You Like to Withdraw? \n $10/$20/$40/$60/$80/$100, for other enter 1: '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print('\nYour Balance is now, $', balance)
                    restart = input('Would You Like to Go Back? ')
                    if restart in ('n', 'NO', 'no', 'N'):
                        print('Thank You')
                        break
                    elif withdrawl != [10, 20, 40, 60, 80, 100]:
                        print('Invalid Amount, Please Retry\n')
                        restart = ('Y')
                    elif withdrawl == 1:
                        withdrawl = float(input('Please Enter Withdrawl Amount: '))
            elif option == 3:
                deposit = float(input('How Much Would You Like to Deposit?'))
                balance = balance + deposit
                print('\nYour Balance is now, $', balance)
                restart = input('Would You Like to Go Back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please Wait While Your Card Is Returned...\n')
                print('Thank you for your patronage')
                break
            else:
                print('Please Enter a Correct Number. \n')
                restart = ('Y')
    elif pin != ('1234'):
        print('Incorrect PIN')
        chances = chances - 1
        if chances == 0:
            print('\nMaximum Access Attempts Allowed, Goodbye')
            break
