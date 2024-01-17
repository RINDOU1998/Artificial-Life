import dm_control.mujoco 
import mujoco.viewer 
import time

m = dm_control.mujoco.MjModel.from_xml_path('example.xml')
d = dm_control.mujoco.MjData(m)
#open viewer
viewer=mujoco.viewer.launch_passive(m, d)

for i in range(1000):
    # Step the simulation
    dm_control.mujoco.mj_step(m, d)
    #sync the viewer
    viewer.sync()
   
    time.sleep(0.01)
#close viewer
viewer.close()