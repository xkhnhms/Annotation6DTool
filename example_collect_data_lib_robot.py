import numpy as np
import time
from Annotation6DAPI.cameras.collect_data_lib import CameraControlToolLib
from Annotation6DAPI.pose_transform.sphere_tools import generate_tcp_poses,sort_tcp_poses
from Annotation6DAPI.robots.AUBO import AuboRobot
import math

if __name__ == "__main__":

    robot=AuboRobot('169.254.4.70')
    tcp_pose=robot.getTcpAnglePose()
    print('tcp_pose: ',tcp_pose)

    tcp_pose_origin = [0.11134947762180022, -0.5802636738170122, 0.8110019118301632, 179.99925090519804, 0.00018667220889616093, 47.29232025782583]

    # 创建并启动双相机可视化
    # 'mecheye', 'orbbec'
    tool = CameraControlToolLib(
        camera_list=['mecheye','orbbec'],
        mech_ip="",
        orbbec_lib_path= '/home/ls/fs/codes/object-grasp-annotation/camera/OrbbecSDK/lib_arm/',
        
        orb_ip="",
        start_visualization=True,
        visualization_delay=0.04,

        interval_time = 2,  # seconds

        root_dir = '/home/ls/Videos/data',     
        scene_id = 0,
        saved_idx = 0,
        check_conf_idx = 0,  
    )

    tcp_poses = generate_tcp_poses(tcp_pose_origin, num_views=450,min_z=500, max_angle=60) 
    sphere_center = np.array([tcp_pose_origin[0], tcp_pose_origin[1], 0])
    tcp_poses = sort_tcp_poses(tcp_poses, sphere_center)

    robot.example_movel_angle(tcp_pose_origin.copy(),acc=0.6,speed=0.35,radius=0,time=1) # 0.6  0.15
    time.sleep(2)
    tool.save_rgbs(tcp_pose_origin)
    time.sleep(2)

    print('start_collect scene data...')
    for i, pose in enumerate(tcp_poses):
        if tool.sceneTool.count_files_in_directory():
            print("文件数已达标，停止采集")       
            break
        print(f"TCP Pose {i+1}:\n{pose}\n")
        tmp = pose.copy()
        move_pose = pose.copy()

        # 2. 判断轨迹点是否可达
        for i in range(3,len(tmp)):
            tmp[i] = tmp[i] / 180.0 * math.pi

        ref_joints = robot.getJointPositionsRad()
        joint_pose,ret_ik = robot.exampleInverseK(tmp,ref_joints)
        print('ret_ik: ',ret_ik)
        if ret_ik == 0 :
            # ret = robot.example_movej(joint_pose)
            # 0.5  0.05  0.65
            try:
                ret = robot.example_movel_angle(move_pose,acc=0.8,speed=0.65,radius=0,time=1) 
                print('ret: ',ret)
                if ret == 0:
                    time.sleep(2.5)
                    # sceneTool.save_rgbs(pose)
                    current_pose = robot.getTcpAnglePose()
                    tool.save_rgbs(current_pose)
                    time.sleep(1)
                    print('saved.')
                    ret = -1
                time.sleep(2)
            except Exception as e:
                print('e: ',e)



    robot.example_movel_angle(tcp_pose_origin.copy(),acc=0.6,speed=0.6,radius=0,time=1) # 0.6  0.15
    robot.dis_connect()

    

