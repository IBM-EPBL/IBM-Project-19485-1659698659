import wiotp.sdk.device
import time
from random import randint as ri

organization = "epmoec"
deviceType = "testDevice"
deviceID = "device0"
authMethod = "token"
authToken = "?-KDXUPMvDo_TK2&b1"

myConfig = {
    "identity" : {
        "orgId" : organization,
        "typeId" : deviceType,
        "deviceId" : deviceID
    },
    "auth" : {
        "token" : authToken
    }
}

def myCommandCallback(cmd):
    print("recieved cmd : ",cmd)


client = wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
client.connect()

while True:
    client.publishEvent(eventId="status",msgFormat="json",data={
        "temperature" : ri(28,35),
        "visibility" : ri(56,78),
        "location" : "Chennai,IN"
    },qos=0,onPublish=None)
    client.commandCallback = myCommandCallback
    time.sleep(1)

client.disconnect()
