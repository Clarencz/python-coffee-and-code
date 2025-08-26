import csv

class Item:
    #class attributes
    pay_rate = 0.8 #pay_rate after 20% discount
    all=[]
    
    def __init__(self,name:str,price:float,quantity = 0):
        # Run validations to the recieved arguments
        assert price >= 0, f"Price {price} can not be less than 0"
        assert quantity >=0, f"Quantity  {quantity} can not be less than 0"
        
        #Assign to self object
        self.__name = name
        self.__price = price
        self.quantity= quantity
        
        #Actions to execute
        Item.all.append(self)
        
    def calculate_total_price(self):
        return self.__price * self.quantity
    
        
    @property
    def price(self):
        return self.__price
    
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price *  increment_value
    
    @property
    #Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
        
    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception ("Name is too long")
        else:
            self.__name = value
        
    @classmethod    
    def instantiate_from_csv(cls):
        with open('B:/96hrs-python-coffee-and-code/advanced_python/OOP/Store_Mngt_System/items.csv','r') as f:
            reader = csv.DictReader(f, skipinitialspace=True)
            # items = []
            # for row in reader:
            #     clean_row = {k.strip(): v.strip().strip("'") for k, v in row.items()}
            #     items.append(clean_row)
            items = list(reader)
        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )
            
    @staticmethod
    def is_integer(num):
        #We will count out the floats that are point zero
        if isinstance(num,float):
            #Count the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__} '{self.name}' {self.price} {self.quantity}"
    
    def __connect(self,smtp_server):
        pass
    
    def __prepare_body(self):
        return f"""
    Hello someone
    We have {self.name} {self.quantity} times.
    Regards, Amznio
    """
    def __send():
        pass
    
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
        
# item1 = Item("Phone",300,3)
# print(item1.name)
# item1.apply_discount()


# ====dynamically passed when when instantiated from the __init__ =====
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# print(item1.calculate_total_price(item1.price,item1.quantity))

# item2 = Item("Laptop",250,3)
# print(item2.price)
# item2.pay_rate=0.7
# item2.apply_discount()
# print(item2.price)

# ====dynamically passed when when instatiated from the __init__ =====
# item1.name = "Laptop"
# item1.price = 200
# item1.quantity = 7
# print(item1.calculate_total_price(item1.price,item1.quantity))

# ===to see the classes of the object create===
# print(type(item1))
# print(type(item1.name))

# item3 = Item("Cable",10,5)
# item4 = Item("Mouse", 50,4)
# item5 = Item("Keyboard", 75,8)

# print(Item.all)

# for instance in Item.all:
#     print(instance.name)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())

#accessing class attributes
# print(Item.pay_rate) 
# print(Item.__dict__)
# print(item1.pay_rate)
# print(item2.pay_rate)

#accessing instance attributes
# print(item1.__dict__)
# print(item2.__dict__)

# print(item1.price)

#calling a classmethod
# Item.instantiate_from_csv()
# print(Item.all)

#Accessing a staticmethod
# print(Item.is_integer(7.4))