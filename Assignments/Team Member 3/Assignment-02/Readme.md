# Assignment 02

## Team Member 3 - Yuvasri M

## Python Program to Simulate Sensor Values

#### [Link to Python Code](./randomSensorValues.py)

### Program Code :
```python
# Python code
# use Python3.8 or higher (F-strings used for formatting)

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
```

### Thank You