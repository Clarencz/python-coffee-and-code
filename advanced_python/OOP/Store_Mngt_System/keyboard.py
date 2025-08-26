from item import Item

class Keyboard(Item):
    def __init__(self, name, price:float, quantity=0):
        #super function
        super().__init__(
            name,price,quantity
        )
        