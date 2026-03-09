class Car:
    ## Below variables are known as "Properties/States/Members"
    # wheelers=4
    # engine='Petrol'
    # base_speed='40Kmph'
    # max_speed='120Kmph'
    # gears=4

## constructor
    def __init__(self,air_bags,security,base_budget,varient,total_sale):
        self.air_bags=air_bags
        self.security=security
        self.base_budget=base_budget
        self.varientt=varient
        self.toatl_sale=total_sale


TATA=Car(True,'Level 5','2L',12,100000)
mahindra=Car(True,'Level 4','4L',20,250000)
print(TATA.security)