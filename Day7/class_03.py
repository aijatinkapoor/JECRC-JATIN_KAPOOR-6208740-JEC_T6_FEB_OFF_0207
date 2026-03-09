class Car:
    ## Below variables are known as "Properties/States/Members"
    wheelers=4
    engine='Petrol'
    base_speed='40Kmph'
    max_speed='120Kmph'
    gears=4

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


TATA=Car(True,'Level 5','2L',12,100000)
mahindra=Car(True,'Level 4','4L',20,250000)



TATA.display_properties()
print()