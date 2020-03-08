import random



class Account:
    def __init__(self,balance):
        self.balance=balance
        self.dictionary=[]
        
      
    def pin_N_id(self):
        self.pin=input('enter pin here')
        self.acc_id= random.randint(99,9999)
        print('Your pin is {}'.format(self.pin))
        print('Your account id is {}'.format(self.acc_id))
        self.dictionary.append(self.pin)
        self.dictionary.append(self.acc_id)
        print (self.dictionary)
    
    def getBalance(self):
        print( self.balance)
    
    def withdraw(self):
        amount=int(input('enter amount you want to withdraw here:'))
        min_bal=15000
        if amount<min_bal and amount<self.balance:
            self.balance -= amount
            print('Your new balance is {}.'.format(self.balance))
    
        else:
            print('Sorry, you cannot withdraw such an amount')
            amount=int(input('Please enter your amount again'))


    def deposit(self):
        amount=int(input('Enter the amount you want to deposit here'))
        self.balance += amount
        print('Your new balance is {}'.format(self.balance))

    def check(self):  
        print('call from savings')

class Savings(Account):
    def __init__(self,amount):
        self.amount=amount
        Account.__init__(self,500)

class Current(Account):
    def __init__(self,amount):
        self.amount=amount
        Account.__init__(self,500)

a=Account(5000)
a.pin_N_id()
a.withdraw()
a.deposit()

b=Savings(5000)
b.withdraw()

'''ent={}
a=pin()
b=pin()
entry['pin']=a.pin
entry['acc_id']=a.acc_id

print(entry)
ent[1]=entry
print(ent)

entry['pin']=b.pin
entry['acc_id']=b.acc_id
ent[2]=entry
print(ent)'''

     

