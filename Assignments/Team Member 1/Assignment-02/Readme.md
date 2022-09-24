# Assignment 02

## Team Member 1 - Ulagaraja J

## Python Program to Simulate Sensor Values

#### [Link to Python Code](./randomSensorValues.py)

### Program Code :
```python
# Python code
# use Python3.8 or higher (F-strings used for formatting)

from random import randint
from time import sleep

iterator = 0

while(True):
    tmp = randint(0,75)
    print("Current Temperature : ",tmp,sep="\t")
    humdty = randint(0,100)
    print("Current Humidity : ",humdty,sep="\t",end="\n")
    
    if(not(10<tmp<42)):
        print("Unbearable Temperature")

    if(not(25<humdty<75)):
        print("Unbearable Humidity")

    sleep(1)
    iterator+=1

    if(iterator>100):
        break
```

### Thank You