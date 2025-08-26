from item import Item

class Phone(Item):
    def __init__(self, name, price:float, quantity=0,broken_phone= 0):
        super().__init__(name, price, quantity)
        #validations
        assert broken_phone >= 0, f"broken phones {broken_phone} should not be less than 0"
        #assign self to object
        self.broken_phones = broken_phone
        
        # actions to execute
        # Phone.all.append(self)
        

# phone1 = Phone("itel", 300,4,0)
# # phone2 = Phone("jasper", 600,3,8)
# phone1.apply_discount()
# print(phone1.calculate_total_price())

# print(Item.all)
# print(Phone.all)
