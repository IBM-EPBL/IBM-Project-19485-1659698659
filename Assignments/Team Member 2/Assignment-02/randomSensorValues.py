import random
import time

while(1):
    t = random.randint(0,50)
    print("Temperature : "+str(t))
    h = random.randint(0,100)
    print("Humidity : "+str(h)+"\n")
    
    print("Ideal Temperature" if (t > 10 and t < 30) else "Not Ideal Temperature")
    print("Ideal Humidity\n" if (h > 25 and h < 75) else "Not Ideal Humidity\n")

    time.sleep(1)