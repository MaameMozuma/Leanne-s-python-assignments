
entry={}
product={}
product_type={}
empty=[]
class product_1:
    
    def __init__ (self,product_id,name):
        self.product_id=product_id
        self.product_name=name
        
class product_type:
    def __init__ (self,name,pid):
        self.type_name=name
        self.type_pid=pid



class inventory:
    def __init__ (self,product_id,qty):
        self.product_id=product_id
        self.quantity=qty


def add_product(product):
    
        if not entry.get(product.product_id):
           entry[product.product_id]=1
        else:
            entry[product.product_id]+=1


'''product=inventory('123',1)
add_product(product)
print(entry)'''




ent={}
a=inventory(234,1)
b=inventory(555,1)
entry['pid']=a.product_id
entry['qty']=a.quantity

print(entry)
ent[33]=entry
print(ent)

entry['pid']=b.product_id
entry['qty']=b.quantity
ent[22]=entry
print(ent)

#entry['pid','qty']=b.product_id
#print(


print(ent[22])

'''product=inventory('778',1)
add_product(product)
print(entry)

product=inventory('986',1)
add_product(product)
print(entry)

product=inventory('554',1)
add_product(product)
print(entry)

product=inventory('567',1)
add_product(product)
print(entry)'''




           
class entries:
    def __init__ (self,entry_details):
        self.entry_details= entry_details




