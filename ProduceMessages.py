from redistimeseries.client import Client
import random, time

# our dataset will be for 4 patients
# each patient will be monitored by 2 devices and we will generate 1000 random sample values
numOfPatients = 4
numOfDevices = 2
numOfSamples = 1000
currentTime = int(time.time()*1000.0)

redisClient = Client(decode_responses=True)

# create a sample with the patient and device type label so we can query by label
def prodcueData(patient, deviceType, s):
    key = "patient:{0}:{1}".format(patient, deviceType)
    # the key also labled with the patient ID and the device type
    # this will allow us to query and filter in our dashboards
    redisClient.add(key, s + currentTime, random.uniform(1, 30), 
        labels={'__name__':'patient', 'patient': patient, 'deviceType':deviceType})

for p in range(numOfPatients):
    for d in range(numOfDevices):
        for s in range(numOfSamples):
            prodcueData(p, d, s)
