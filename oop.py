import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    # Defalut, firstly, instances will find the attribute from the instance level,if it is not there, it will find from class level
    all =[]
    def __init__(self,name:str,price:float,quantity=0):
        #Run validation to recieved arguments
        assert price>=0, f"Price {price} is not greater or equal to than zero!"
        assert quantity>=0, f"Quantity {quantity} is not greater or equal to than zero!"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity =quantity

        #Actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price* self.pay_rate
    
    #Class method
    @classmethod
    def instantiate_from_csv(cls):
        with open("item.csv","r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            cls(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

class Phone(Item):
    def __init__(self,name:str,price:float,quantity=0,broken_phone=0):
        super().__init__(
            name,price,quantity
        )
        assert broken_phone>=0, f"Broken phone is greater or equal than 0"
        self.broken_phone = broken_phone


phone1= Phone("jscphonev10",500,5)
phone2= Phone("jscphonev10",700,500)
print(phone1.all)