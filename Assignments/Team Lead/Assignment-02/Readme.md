# Assignment 02

## Team Lead - Sayad Pervez B

## Python Program to Simulate Sensor Values

#### [Link to Python Code](./randomSensorValues.py)

### Program Code :
```python
# Python code
# use Python3.8 or higher (F-strings used for formatting)

from random import randint as ri
from time import sleep as delay
from os import system as cmd

temperatureThresholdRange = range(20,31)
humidityThresholdRange = range(35,75)

def clrscr():
    try:
        cmd("cls")   # for WINDOWS
    except Exception as e:
        cmd("clear") # for LINUX

def getHumidity():
    return(ri(0,100)) # returns moisture in %

def getTemperature():
    return(ri(0,45)) # returns temperature in °C

# Recursion is safer than while(True)
# Coz python has a built-in exception to stop the execution of code after about a 1000 recursive calls

def myRecursiveLoop():
    clrscr()
    t,h = getTemperature(),getHumidity()
    
    print(f"\n\nCurrent Temperature : {t} °C\nCurrent Humidity : {h} %\n")
    print(f"{'Dangerous levels of Humidity' if (h not in humidityThresholdRange) else ''}\n{'Dangerous levels of Temperature' if t not in temperatureThresholdRange else ''}\n\n")

    # 1 sec delay before next execution
    delay(1)
    myRecursiveLoop()

try:
    myRecursiveLoop()
except RecursionError:
    print("Python safely terminated after about a 1000 recursive calls")
    exit()
```

### Thank You