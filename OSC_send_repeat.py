
#Modified from https://osc4py3.readthedocs.io/en/latest/userdoc.html#examples

#sends OSC message to BitFocus Companion

# Import needed modules from osc4py3
from osc4py3.as_eventloop import *
from osc4py3 import oscbuildparse
import time


# Start the system.
osc_startup()

# Make client channels to send packets.
osc_udp_client("192.168.0.92", 12321, "aclientname")

# Make a message
msg1 = oscbuildparse.OSCMessage("/press/bank/1/8", None, [1, 5, 3]) #presses putton 1.8. Not sure what the rest does

#send message every second
while True:
    osc_process()
    osc_send(msg1, "aclientname")
    time.sleep(1)
    
#probibly dont need this
osc_terminate()
