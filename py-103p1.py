class Bike:
    def __init__(self, sold, description, cost, sale_price, condition):
        self.sold = False
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
    
    def sell(self):
        if self.sold == True:
            print("Action not allowed, Bike has already been sold")
        else:
            self.sale_price= sale_price
            def update(self):
                if self.sold == True:
                    print("Action not allowed, Bike has already been sold")
                else:
                    print("you are lucky today we have discount")
                    self.cost= 350
                    print("the price goes from 500\n"+self.cost)

    def sell(self):
           
        if self.sold:
            print('Bike has already sold ')
        else:
            print ('Bike is available ')

#creat new bike
bike1=Bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
        

print(dir(bike1))
            
