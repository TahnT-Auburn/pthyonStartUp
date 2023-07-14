### OBJECT-ORIENTED PROGRAMMING PRACTICE ###

import csv

# source 1: realpython.com/python3-object-oriented-programming/

# --- define parent Shinobi class ---
class Shinobi:

    # define class attributes that represent the same values for each class instance
    anime = 'Naruto'

    # define instances that can vary among each class instance
    def __init__(self, name:str, age:int, origin:str, special_skill:str, rank:float):

        # define assertions
        assert age >= 0, f"{name}'s age [{age}] is not a valid age"
        assert rank >= 0, f"{name}'s rank [{rank}] is not a valid rank"

        # define self objects
        self.name = name
        self.age = age
        self.origin = origin
        self.special_skill = special_skill
        self.rank = rank
        
    # define instance string - allows coherrent display for each instance
    def __str__(self):
        return f"{self.name} | Age: {self.age} | Origin: {self.origin} | Rank: {self.rank} | Special Skill: {self.special_skill}"

    # define power level method
    def powerLevel(self):

        global ssPower, pL  # make skill power and power levels global variables

        if self.special_skill == 'Jinchuriki':
            ssPower = 9
        elif self.special_skill == 'Sharingan':
            ssPower = 9
        elif self.special_skill == 'Strength':
            ssPower = 6

        pL = self.rank + ssPower
        return pL

# source 2: freeCodeCamp.org - youtube.com/watch?v=Ej_02ICOIgs

# --- define shop class ---
class MajikShop:

    # define discounts
    discount = 20 # (%)

    # define array to store all items
    all = []
    all_price = []

    def __init__(self, name:str, price:float, quantity=0):

        # define assertions
        assert price >= 0, f"{name}'s price [{price}] is not a valid price"
        assert quantity >= 0, f"{name}'s quanitiy [{quantity}] is not a valid quantity"

        # define self objects
        self.name = name
        self.price = price
        self.quantity = quantity
        
        # define actions to execute
        #MajikShop.all.append(self)
        #MajikShop.applyDiscount(self)
        #MajikShop.all_price.append(self.calculateTotalPrice())

    def __str__(self):
        return f"{self.name} | Price: {self.price} | Quantity: {self.quantity}"
    
    # output method when using print(MajikShop.all)
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}, {self.price}, {self.quantity}')"
    
    def calculateTotalPrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.pay_rate = 1 - (self.discount/100)
        self.price = self.price * self.pay_rate

    # define a class method - since this method is responsible for instantiating
    #            from a csv, it cannot take in 'self' since it is creating 'self'
    @classmethod
    def instantiateFromCsv(cls):
        with open('items.csv', 'r') as f: # call respective csv file as 'f'
            reader = csv.DictReader(f)  # read from csv using DictReader
            items = list(reader)    # create a list called items from csv
        
        for item in items:
            MajikShop(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    # define a static method
    @staticmethod
    def isInteger(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

# deine a boots child class
class Boots(MajikShop):

    # define array to store all boots
    all_boots = []
    all_boots_price = []

    def __init__(self, name:str, price:float, quantity=0, damaged_boots=0):

        # call to super function to have access to all attributes/methods from MajikShop
        super().__init__(
            name, price, quantity
        )
        # define assertions
        assert price >= 0, f"{name}'s price [{price}] is not a valid price"
        assert quantity >= 0, f"{name}'s quantity [{quantity}] is not a valid price"
        assert damaged_boots >= 0, f"{name}'s damaged boots [{damaged_boots}] is not a valid price"

        # define self object
        self.damaged_boots = damaged_boots

        # actions to execute
        Boots.all_boots.append(self)
        Boots.discount = 30
        Boots.applyDiscount(self)
        Boots.saleItems(self)
        Boots.all_boots_price.append(self.calculateTotalPrice())

    # define method to calculate number sale items
    def saleItems(self):
        self.quantity = self.quantity - self.damaged_boots

# define a swords child class
class Swords(MajikShop):

    # define array to store all swords
    all_swords = []
    all_swords_price = []

    def __init__(self, name:str, price:float, quantity=0, damaged_swords=0):

        # call to super function to have access to all attributes/methods from MajikShop
        super().__init__(
            name, price, quantity
        )
        # define assertions
        assert price >= 0, f"{name}'s price [{price}] is not a valid price"
        assert quantity >= 0, f"{name}'s quantity [{quantity}] is not a valid price"
        assert damaged_swords >= 0, f"{name}'s damaged boots [{damaged_swords}] is not a valid price"

        # define self object
        self.damaged_swords = damaged_swords

        # actions to execute
        Swords.all_swords.append(self)
        Swords.saleItems(self)
        Swords.applyDiscount(self)
        Swords.all_swords_price.append(self.calculateTotalPrice())

        # define method to calculate number sale items
    def saleItems(self):
        self.quantity = self.quantity - self.damaged_swords



        

        
    
