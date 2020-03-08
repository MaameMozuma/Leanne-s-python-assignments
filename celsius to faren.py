class Temperature:
    def __init__(self,value):
        self.temperature = value
    def celsius_to_faren(self):
        print((self.temperature-32)*5/9)

    def faren_to_celsius(self):
        print((self.temperature*9/5)+32)
        
c=Temperature(80)
print(c.temperature)
c.celsius_to_faren()






