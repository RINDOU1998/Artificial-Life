import dm_control.mujoco 
import mujoco.viewer 
import time
import numpy as np

def run_model(model_file):
    m = dm_control.mujoco.MjModel.from_xml_path(model_file)
    d = dm_control.mujoco.MjData(m)
    total_distance=0
    max_height = 0
    min_height = float('inf')
#open viewer
    viewer=mujoco.viewer.launch_passive(m, d)
    initial_position = np.copy(d.qpos)

    for j in range(len(d.ctrl)):
        d.ctrl[j] = 2
    time.sleep(1)

    for i in range(20):
    # Step the simulation
    #flip
        for j in range(len(d.ctrl)):
            d.ctrl[j] = -d.ctrl[j]
    
        for j in range(30):
            dm_control.mujoco.mj_step(m, d)
            distance_moved = np.linalg.norm(d.qpos[:3] - initial_position[:3])
            total_distance += distance_moved
            initial_position = np.copy(d.qpos[:3])
    #sync the viewer
            current_position = d.qpos[:3]
            current_height = current_position[2]
            if current_height > max_height:
                max_height = current_height
            if current_height < min_height:
                min_height = current_height
        
            viewer.sync()
   
            time.sleep(0.01)
#close viewer
    viewer.close()
    return total_distance,max_height,min_height
