import pypot.dynamixel
import time

ports = pypot.dynamixel.get_available_ports()
if not ports :
	raise RuntimeError("No motors")

print "connecting to port",ports[0]
dxl=pypot.dynamixel.DxlIO(ports[0])

ids=dxl.scan(range(30))
#print ids

dxl.enable_torque(ids)
ids = tuple(ids)
print ids

def initial_pos():
	dxl.set_moving_speed({1:60, 2:60,3:60,4:60,5:60,6:60,7:60,8:60,9:60,10:60})

	dxl.set_goal_position({1:0, 2:0, 3:0, 4:0, 5:45, 6:-45, 7:0, 8:0, 9:0, 10:0})
	raw_input("Step 1 done")
	
	dxl.set_goal_position({1:-25, 2:25,3:0,4:0,5:-25,6:25,7:55,8:-55,9:0,10:0})
	#time.sleep(2)
	raw_input("Step 2 done")
	#dxl.set_goal_position({8:10})
def left_weight_shift():
	

	#dxl.set_goal_position({1:15, 2:27,3:-25,4:25,5:-25,6:25,7:-35,8:35,9:5,10:-5,1:0})
	#raw_input("Step 3 done")
	#time.sleep(1)
	
	#dxl.set_goal_position({1:15, 2:27,3:-25,4:25,5:-25,6:25,7:-55,8:55,9:5,10:-5})
	#raw_input("Step 4 done")
	#time.sleep(1)
	dxl.set_goal_position({1:-25, 2:27,3:-25,4:25,5:0,6:25,7:75,8:-55,9:0,10:0})
	raw_input("Step 2.5 done ")
	#time.sleep(1)
	dxl.set_goal_position({1:-25, 2:27,3:0,4:25,5:-45,6:25,7:100,8:-60,9:0,10:0})
	#time.sleep(0.3)
	raw_input("step 3 done")
	#time.sleep(0.3)
	#dxl.set_goal_position({1:15, 2:27,3:-20,4:25,5:10,6:10,7:-55,8:55,9:5,10:-5})
	dxl.set_goal_position({1:-25, 2:27,3:0,4:25,5:-5,6:25,7:75,8:-60,9:0,10:0})
	raw_input("step 4 done")
	#time.sleep(0.5)
	dxl.set_goal_position({1:0, 2:27,3:-15,4:20,5:-5,6:25,7:55,8:-60,9:0,10:0})
	raw_input("step 5 done")
	#time.sleep(0.5)
	dxl.set_goal_position({1:10, 2:27,3:-15,4:15,5:5,6:25,7:55,8:-60,9:0,10:0})
	#time.sleep(0.1)
	raw_input("")
	#dxl.set_goal_position({1:10, 2:0,3:-20,4:45,5:0,6:10,7:55,8:-80,9:0,10:0})


def right_weight_shift():
	dxl.set_goal_position({1:-5, 2:0,3:0,4:-20,5:45,6:-20,7:55,8:-80,9:0,10:0})
	#rime.sleep(1)
	#dxl.set_goal_position({1:-5, 2:5,3:-35,4:45,5:-36,6:-20,7:15,8:50,9:10,10:-5})
	#raw_input(" ;llk")
	#dxl.set_goal_position({1:-5, 2:0,3:0,4:20,5:35,6:-20,7:-50,8:65,9:5,10:-5})
	#time.sleep(0.5)
	#dxl.set_goal_position({1:-5, 2:0,3:0,4:20,5:35,6:-20,7:-60,8:70,9:5,10:-5})
initial_pos()

left_weight_shift()

#right_weight_shift()


