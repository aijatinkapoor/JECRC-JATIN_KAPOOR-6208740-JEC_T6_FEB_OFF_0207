class Car:
    ## Below variables are known as "Properties/States/Members"
    wheelers=4
    engine='Petrol'
    base_speed='40Kmph'
    max_speed='120Kmph'
    gears=4


    def __init__(self,air_bags,security,base_budget,varient,total_sale):
        self.air_bags=air_bags
        self.security=security
        self.base_budget=base_budget
        self.varientt=varient
        self.toatl_sale=total_sale

    

    def display_properties(self):
        print({
            'wheelers':self.wheelers,
            'engine':self.engine,
            'base_speed':self.base_speed,
            'max_speed':self.max_speed,
            'gears':self.gears,
            'air_bags':self.air_bags,
            'varient':self.varientt,
            'total_sales':self.toatl_sale
            

        })
    
    def update_base_speed(self,new_speed):
       self.base_speed = new_speed
       print(f'New Base Speed: {self.base_speed}')

    def update_max_speed(self,new_speed):
        self.max_speed = new_speed
        print(f'New Base Speed: {self.max_speed}')

    @classmethod
    def update_gears(cls,new_gears):
        cls.gears=new_gears
        print(f'No of gears: {cls.gears}')

# TATA=Car()
# TATA.engine=['Petrol','Diesel','EV']
# TATA.air_bags=True
# TATA.no_of_air_bags='2L'
# TATA.no_of_varient=12

## constructor (__init__)

'''
class ClassName:
    properties
    
    def __init__(self,arg1,arg2,arg3,...,argn):
        self.arg1=arg1
        self.arg2=arg2
        self.arg3=arg3
        ...
        self.argn=argn
        '''
# TATA.Car()
# mahindra.Car()

    

TATA=Car(True,'Level 5','2L',12,100000)
mahindra=Car(True,'Level 4','4L',20,250000)



TATA.display_properties()
print()

print('Properties after updation')
TATA.update_max_speed(160)
TATA.update_base_speed(60)
TATA.update_gears(9)

print('Mahindra:  ')
mahindra.display_properties()
# print(TATA.security)

# TATA.air_bags=True