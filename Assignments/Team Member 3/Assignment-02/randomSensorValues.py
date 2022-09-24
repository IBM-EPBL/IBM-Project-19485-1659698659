from random import randint
from time import sleep

while(True):
    temp = randint(-50,50)
    print("Temperature : "+str(temp))
    humidity = randint(0,100)
    print("Humidity : "+str(humidity)+"\n")
    
    if(temp > 10 and temp < 30):
        print("Ideal Temperature")
    else:
        print("Not Ideal Temperature")

    if(humidity > 25 and humidity < 75):
        print("Ideal Humidity")
    else:
        print("Not Ideal Humidity")

    print("\n")

    sleep(1)