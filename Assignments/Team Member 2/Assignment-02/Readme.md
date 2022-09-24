# Assignment 02

## Team Member 2 - Yuvashree R

## Python Program to Simulate Sensor Values

#### [Link to Python Code](./randomSensorValues.py)

### Program Code :
```python
# Python code
# use Python3.8 or higher (F-strings used for formatting)

import random
import time

while(True):
    t = random.randint(-50,50)
    print("Temperature : "+str(t))
    h = random.randint(0,100)
    print("Humidity : "+str(h)+"\n")
    
    print("Ideal Temperature" if (t > 10 and t < 30) else "Not Ideal Temperature")
    print("Ideal Humidity" if (h > 25 and h < 75) else "Not Ideal Humidity\n")

    time.sleep(1)
```

### Thank You