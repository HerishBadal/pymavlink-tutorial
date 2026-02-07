"""
    Source: https://mavlink.io/en/messages/common.html#COMMAND_LONG
            https://mavlink.io/en/messages/common.html#MAV_CMD
            https://mavlink.io/en/messages/ardupilotmega.html#MAV_CMD_DO_SEND_BANNER
            https://mavlink.io/en/messages/common.html#STATUSTEXT
            https://mavlink.io/en/messages/common.html#COMMAND_ACK

    To receive a message from MAVLink stream, recv_match() is used
    To send a message, mav.send() is used

    There are three ways to send commands to vehicle:
        COMMAND_LONG (MAV_CMD_* command messages)
        COMMAND_INT (MAV_CMD_* command messages)
        CUSTOM (Like SET_POSITION_TARGET_LOCAL_NED, SET_POSITION_TARGET_GLOBAL_INT, ...)
"""

import pymavlink.mavutil as utility
import pymavlink.dialects.v20.all as dialect

# connect to vehicle
# tcp: 127.0.0.1:5762 connects the script to the mission planner
vehicle = utility.mavlink_connection(device="tcp:127.0.0.1:5762")

# wait for a heartbeat
vehicle.wait_heartbeat()

# inform user
print("Connected to system:", vehicle.target_system, ", component:", vehicle.target_component)
#to send a command you need to fist build them
# build up the command message
