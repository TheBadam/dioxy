from machine import Pin, I2C        #importing relevant modules & classes
from time import sleep
import bme280     #importing BME280 library
import ens160

i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)    #initializing the I2C method 

while True:
  ens=ens160.ENS160(i2c)
  bme = bme280.BME280(i2c=i2c)
  TVOC=ens.getTVOC()
  AQI=ens.getAQI()
  ECO2=ens.getECO2()
  print(bme.values)
  print("AQI: ", AQI)
  print("TVOC: ", TVOC)
  print("ECO2: ", ECO2)
  sleep(10)           #delay of 10s