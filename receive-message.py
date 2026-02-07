"""
    Source: https://www.ardusub.com/developers/pymavlink.html#run-pymavlink-on-the-surface-computer
            https://mavlink.io/en/messages/common.html

    To receive a message from MAVLink stream, recv_match() is used
        type: used for filtering a specific message, ex: SYSTEM_TIME
        blocking: used for this function blocks the execution or not
        timeout: used for defining maximum blocking time

    pymavlink.dialects contains all the MAVLink message dialects
    pymavlink.dialects.v20 contains all the MAVLink2 message dialects
    pymavlink.dialects.v20.all contains all the MAVLink2 message types and definitions
"""

import time
import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# connect to vehicle
vehicle = utility.mavlink_connection(device="tcp:127.0.0.1:5762")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)

# infinite loop
while True:

    try:
        #to catch messages form mavlink(vehicle)
        # not a good idea to use type="string" and thus we will use dialect packages
        #message = vehicle.recv_match(type="SYSTEM_TIME", blocking=True, timeout=0.010)
        #message = vehicle.recv_match(type=dialect.MAVLink_system_time_message, blocking=True, timeout=0.010)
        #to get message name
        message = vehicle.recv_match(type=dialect.MAVLink_system_time_message.msgname, blocking=True)

        #print(message)
        message= (message.to_dict())
        for fieldname in dialect.MAVLink_system_time_message.fieldnames:
            if fieldname=="time_boot_ms":
                print(fieldname, message[fieldname])


    except:
        print("no message received from vehicle")


    time.sleep(0.010)

