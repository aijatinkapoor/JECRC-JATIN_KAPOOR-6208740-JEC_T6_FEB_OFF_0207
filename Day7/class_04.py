class Car:
    ## Below variables are known as "Properties/States/Members"
    wheelers=4
    engine='Petrol'
    base_speed='40Kmph'
    max_speed='120Kmph'
    gears=4

    def update_base_speed(self,new_speed):
       self.base_speed = new_speed
       print(f'New Base Speed: {self.base_speed}')

    def update_max_speed(self,new_speed):
        self.max_speed = new_speed
        print(f'New Base Speed: {self.max_speed}')

TATA=Car
print('Properties after updation')
TATA.update_max_speed(160)
TATA.update_base_speed(60)
TATA.update_gears(9)