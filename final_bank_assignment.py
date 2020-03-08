
class Account:
    max_withdrawal = 5000  
    all_accounts = [
        {'account_number': 100, 'name': 'Leanne', 'balance': 983.93,
         'pin': 100},
        {'account_number': 101, 'name': 'Joshua', 'balance': 788.02,
         'pin': 101},
        {'account_number': 102, 'name': 'Awurama', 'balance': 45229.88,
         'pin': 102},
        {'account_number': 103, 'name': 'Akosua', 'balance': 94.01,
         'pin': 103},
        {'account_number': 104, 'name': 'Abena', 'balance': 20199.61,
         'pin': 104}
    ]

    
    @classmethod
    def find_account(cls, account):
        return cls.all_accounts.index(account)

    
    @classmethod
    def getAccount(cls, account_number, pin):
        for account in cls.all_accounts:
            if(account['account_number'] == account_number and account['pin'] == pin):
                return account
        return None

    
    def get_balance(self, account):
        index = self.find_account(account)
        print('*' * 50)
        print('Your balance is :\n')
        print(self.all_accounts[index]['balance'])
        print('*' * 50)
        input("Press enter key to continue")

    def withdraw(self, active_account):
        can_withdraw = True
        amount = int(input('Enter amount here:\n'))
        if amount > self.max_withdrawal:
            can_withdraw = False
            print('Your amount ({}) is greater than the maximum withdrawals for the day ({})\n'.format(
                amount, self.max_withdrawal
            ))

        elif can_withdraw:
            index = self.find_account(active_account)
            # now update active account in main list
            self.all_accounts[index]['withdrawals_today'] += 1
            self.all_accounts[index]['amount_today'] += amount
            bal_after = active_account['balance'] - amount
            self.all_accounts[index]['balance'] = bal_after
            print('Withdrawal successful.\nYour new balance is {}.'.format(bal_after))

        
        input("Press enter key to continue")

    def deposit(self, active_account):
        amount = int(input('Enter the amount you want to deposit here\n'))
        bal_after = active_account['balance'] + amount
        self.all_accounts[self.find_account(
            active_account)]['balance'] = bal_after
        print('Deposit successful.\nYour new balance is {}'.format(bal_after))
        input("Press enter key to continue")


def displayMenu(active_account):
    print('*' * 50)
    print('\nWelcome to MY ATM, {}'.format(active_account['name']))
    print('\nChoose an option')
    print('\nPress 1 to withdraw')
    print('\nPress 2 to deposit')
    print('\nPress 3 to check balance')
    print('\nPress 4 to quit\n')
    print('*' * 50)


def withdraw():
    print('*' * 50)
    print('\nEnter Amount to withdraw')
    print('*' * 50)
    userOption = int(input(''))


def bank_accnt(active_account):
    keepOn = True
    while keepOn:

        displayMenu(active_account)
        userOption = int(input('Enter an option\n'))
        a = Account()
        if userOption == 1:
            a.withdraw(active_account)
        elif userOption == 2:
            a.deposit(active_account)
        elif userOption == 3:
            a.get_balance(active_account)
        else:
            keepOn = False
            print('*' * 50)
            print('\nGoodbye\n')
            print('*' * 50)




login_attempts = 3


def requestPIN():
    logged_in = False
    for i in range(login_attempts):
        try:  
            account_number = int(input('enter your account number:\n'))
            pin = int(input('enter pin here:\n'))
            account = Account.getAccount(account_number, pin)
            if account is not None:
                return account
            else:
                print("Sorry wrong account number or PIN\n")
        except Exception as e:
            print("Invalid number entered\n")

    print("Sorry. Too many PIN tries, exiting program......")
    exit()

active_account = requestPIN()  

bank_accnt(active_account)
