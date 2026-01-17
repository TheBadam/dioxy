from logging import log_message
from machine import Pin, I2C

from sensor import read_sensor
from server import connect, open_socket, serve

i2c=I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)    #initializing the I2C method 

if __name__ == "__main__":
    filename = "error.log"
    log_message(filename, "Power ON")
    conn = None
    try:
        ip = connect()
        conn = open_socket(ip)
        serve(conn, read_sensor)
    except Exception as e:
        print(e)
        log_message(filename, e)  
    finally:
        print("Exit")
        if conn is not None:
            conn.close()
        log_message(filename, "Exit")
        
