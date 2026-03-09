class Car:
    ## Below variables are known as "Properties/States/Members"
    wheelers=4
    engine='Petrol'
    base_speed='40Kmph'
    max_speed='120Kmph'
    gears=4

    @classmethod
    def update_gears(cls,new_gears):
        cls.gears=new_gears
        print(f'No of gears: {cls.gears}')

        