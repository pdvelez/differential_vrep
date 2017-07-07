"""
Script that controls the differential robot set in the V-rep scene.

Author: Pedro D. Velez
"""
import sys
import vrep

vrep.simxFinish(-1)  # just in case, close all opened connections
clientID = vrep.simxStart('127.0.0.1', 19999, True, True, 5000, 5)  # Connect to V-REP

if clientID != -1:
    print ('Connected to remote API server')

else:
    print ('Failed to connect to the server')
    sys.exit()
