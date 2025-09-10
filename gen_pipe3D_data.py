import copy
import math
import time
import cv2
import numpy as np
from Annotation6DAPI.pose_transform.sphere_tools import generate_tcp_poses,sort_tcp_poses
from Annotation6DAPI.robots.AUBO import AuboRobot
from Annotation6DAPI.cameras.mechEyeCamera import mechCamera

if __name__=='__main__':

    tcp_pose_origin=[0.10350602988582203, -0.4364249213805751, 0.7400088396263331, -179.9658342120211, 0.4121784570514573, -90.05758734672833]
    robot = AuboRobot('169.254.4.70')
    camera_mech = mechCamera()
    camera_mech.ConnectToCameraByDefault()

    robot.example_movel_angle(tcp_pose_origin.copy())

    time.sleep(1.5)
    file_name = '_'.join(map(str,tcp_pose_origin))

    rgb_mech = camera_mech.capture_2d_image()
    depth_mech = camera_mech.capture_depth_map()
    depth_mech = np.nan_to_num(depth_mech, copy=False, nan=0.0)
    depth_mech = depth_mech.astype(np.uint16)

    times=time.time()
    cv2.imwrite(f'pipe3D_data/rgb/{file_name}.png',rgb_mech)
    cv2.imwrite(f'pipe3D_data/depth/{file_name}.png',depth_mech)
    time.sleep(1)
    

    tcp_poses = generate_tcp_poses(tcp_pose_origin.copy(),num_views=100,min_z=450,max_angle=70)
    sphere_center = np.array([tcp_pose_origin[0], tcp_pose_origin[1], 0])
    radius = tcp_pose_origin[2]

    tcp_poses = sort_tcp_poses(tcp_poses, sphere_center)
    print('tcp_poses lens: ',len(tcp_poses))

    for tcp_pose in tcp_poses:
        tcp_tmp = copy.deepcopy(tcp_pose)
        for i in range(3,6):
            tcp_tmp[i]/=180.0*math.pi
    
        cur_joint_pose=robot.getJointPositionsRad()
        ans = robot.exampleInverseK(tcp_tmp,cur_joint_pose)
        if ans[1]==0:
            robot.example_movel_angle(tcp_pose.copy())
            time.sleep(1.5)
            file_name = '_'.join(map(str,tcp_pose))

            rgb_mech = camera_mech.capture_2d_image()
            depth_mech = camera_mech.capture_depth_map()
            depth_mech = np.nan_to_num(depth_mech, copy=False, nan=0.0)
            depth_mech = depth_mech.astype(np.uint16)

            times=time.time()
            cv2.imwrite(f'pipe3D_data/rgb/{file_name}.png',rgb_mech)
            cv2.imwrite(f'pipe3D_data/depth/{file_name}.png',depth_mech)
            time.sleep(1)
           




    



    pass


