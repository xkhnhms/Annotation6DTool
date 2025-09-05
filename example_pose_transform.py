import math
import numpy  as np
import json
from Annotation6DAPI.pose_transform.ggFilter import transform

if __name__=='__main__':

    net = get_net()

    with open("./conf/params.json", 'r') as load_f:
        load_dict = json.load(load_f)

    coneAngle = load_dict['coneAngle']
    calibMatrix = load_dict['CalibMatrix']
    cert_pose = load_dict['homePose']

    end_points, cloud = get_and_process_data_camera(color_img, depth)
    gg = get_grasps(net, end_points)
    gg = collision_detection(gg, np.array(cloud.points))
    gg = filter(gg,coneAngle)


    gripper_lens = load_dict["gripper_lens"]
    gripper_angle = load_dict["gripper_angle"]
    grasp_location, width=transform(gg, cert_pose, calibMatrix, gripper_lens,gripper_angle)

    tmp_pose = grasp_location.copy()
    for i in range(3,len(tmp_pose)):
        tmp_pose[i] = tmp_pose[i] / 180.0 * math.pi
    print('grasp_location: ',tmp_pose) 

