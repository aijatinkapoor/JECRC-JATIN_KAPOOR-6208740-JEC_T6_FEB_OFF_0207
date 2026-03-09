class Car:
    ## Below variables are known as "Properties/States/Members"
    wheelers=4
    engine='Petrol'
    base_speed='40Kmph'
    max_speed='120Kmph'
    gears=4

##Balow instances are called as objects.
TATA=Car()

##By follwing approach, we can also add new properities inside the objects
TATA.air_bags= True
TATA.security='Level 4'

## For accesing the properties,we have to follow the below syntax:
print('Prperties of TATA ------')
print(f'No of wheelers:{TATA.wheelers}')
print(f'engine:{TATA.engine}')
print(f'Bae_SPEED :{TATA.base_speed}')
print(f'Max_Speed:{TATA.max_speed}')
print(f'Air Bags:{TATA.air_bags}')
print(f'Security:{TATA.security}')
print()

mahindra=Car()

print('Prperties of mahindra ------')
print(f'No of wheelers:{mahindra.wheelers}')
print(f'engine:{mahindra.engine}')
print(f'Bae_SPEED :{mahindra.base_speed}')
print(f'Max_Speed:{mahindra.max_speed}')
print()

suziki=Car()
MG=Car()