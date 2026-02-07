"""
    Source: https://mavlink.io/en/mavgen_python/#connection_string
    pymavlink is the library to communicate with ArduPilot firmware in Python using MAVLink
    MAVProxy and Dronekit Python are implemented using pymavlink library
    To connect to the vehicle pymavlink.mavutil.mavlink_connection() is used
    It uses the same connection string as MAVProxy and Dronekit Python
    For serial connection:
        device="COMX" for Windows
        device="/dev/ttyUSB0" for Linux
        Baud rate must be set using baud=X where X is the baud rate
    For UDP connection:
        device="udp:address:port" (legacy) or device="udpin:address:port" to connect to a stream
        device="udpout:address:port" to create a stream
        device="udpbcast:address:port" to broadcast a stream
    For TCP connection:
        device="tcp:address:port" to create a stream
        device="tcpin:address:port" to connect to a stream
"""
# to connect to the vehicle we use mavutil sub package
import pymavlink.mavutil
#create a connection between this script and the vehicle
# 'device' argument is the most important , 'connection string'
# to decide how to connect to the vehicle you set the device to that.e.g serrial,TCP,UDP
vehicle = pymavlink.mavutil.mavlink.connection(device="udpin:127.0.0.1:14550")

#to check if we connected to the vehicle or not
# it is a blocking fucntion and no time out if it reached to this line it means you
# connected to the vehicle sussefully
vehicle.wait_heartbeat()

print("connected to the vehicle")