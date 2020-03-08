'''correct_pin="12345"
pin=input("Enter your pin")
attempts=0
balance=30000
while pin:
       if attempts<3 and pin!=correct_pin:
            attempts+=1
            print("wrong pin.")
            pin=input('enter pin again')
            if attempts==3:
                print("sorry, you have reached your limit")
       else:
            if pin==correct_pin:
               print('welcome!')
               amount=float(input("how much would you like to deposit?"))
               balance+=amount
               print("Your account balance is now {}".format(balance+amount))
               pin=False
'''
def bank_acct():
       balance=30000
       pin=input("enter pin")
       correct_pin="12345"
       min_balance=15000
       attempts=0
       while pin:
              if pin==correct_pin:
                  amount=float(input("how much would you like to withdraw?"))
                  if amount>min_balance:
                          print("You cannot withdraw such an amount.")
                          amount=float(input("Input another amount: "))
                          balance-amount
                          print("your balance is now {}".format(balance-amount))
                          continue
                  else:
                       balance-amount
                       print("your balance is now {}".format(balance-amount))  
                       pin=False
              else:
                     #while pin:
                     if pin!=correct_pin and attempts<4:
                            attempts+=1
                            print("wrong pin")
                            pin=input("Please enter pin again")
                            if pin!=correct_pin and attempts==3:
                                   print("Sorry.You've exceeded your limit")
                                   break
##                                          amount=float(input("how much would you like to withdraw?"))
##                                          if amount>min_balance:
##                                               print("You cannot withdraw such an amount.")
##                                               amount=float(input("Input another amount: "))
##                                               balance-amount
##                                               print("your balance is now {}".format(balance-amount))
##                                               pin=False
##                                   else:
##                                          balance-amount
##                                          print("your balance is now{}".format(balance-amount))
##                                          pin=False

bank_acct()









                                   
       
            
         
        
        
