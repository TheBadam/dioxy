from machine import Pin, I2C

import bme280
import ens160

i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)    #initializing the I2C method 

def read_sensor():
    ens=ens160.ENS160(i2c)
    bme = bme280.BME280(i2c=i2c)

    readings = bme.readings
    readings['tvoc'] = {"value": ens.getTVOC(), "unit": None}
    readings['aqi'] = {"value": ens.getAQI(), "unit": None}
    readings['eco2'] = {"value": ens.getECO2(), "unit": None}
    return readings
