import numpy as np
import time
from Annotation6DAPI.cameras.collect_data_sdk import CameraControlToolSDK
from Annotation6DAPI.pose_transform.sphere_tools import generate_tcp_poses,sort_tcp_poses


if __name__ == "__main__":

    tcp_pose_origin = [0.11134947762180022, -0.5802636738170122, 0.8110019118301632, 179.99925090519804, 0.00018667220889616093, 47.29232025782583]

    # 创建并启动双相机可视化
    # 'mecheye', 'orbbec'
    tool = CameraControlToolSDK(
        camera_list=['mecheye','orbbec'],
        mech_ip="",

        orb_ip="",
        start_visualization=True,
        visualization_delay=0.04,

        interval_time = 2,

        root_dir = '/data',     
        scene_id = 0,
        saved_idx = 0,
        check_conf_idx = 0,  
    )

    tcp_poses = generate_tcp_poses(tcp_pose_origin, num_views=450,min_z=500, max_angle=60) 
    sphere_center = np.array([tcp_pose_origin[0], tcp_pose_origin[1], 0])
    tcp_poses = sort_tcp_poses(tcp_poses, sphere_center)

    print('start_collect scene data...')
    for i, pose in enumerate(tcp_poses):
        if tool.sceneTool.count_files_in_directory():
            print("文件数已达标，停止采集")       
            break
        print(f"TCP Pose {i+1}:\n{pose}\n")

        time.sleep(2)
        
        tool.save_rgbs(pose)  # 保存当前帧

    print("所有位姿采集完成！")

