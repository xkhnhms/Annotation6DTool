from Annotation6DAPI.pose_transform.sphere_tools import generate_tcp_poses,sort_tcp_poses
import numpy as np


if __name__ == "__main__":

    tcp_pose_origin = [-0.05200781630112538, -0.4365385510882652, 0.7779772091712384, 176.34211831737213, -0.5172254411868592, 132.29972778284557]

    tcp_poses = generate_tcp_poses(tcp_pose_origin, num_views=255, min_z=500, max_angle=65)
    sphere_center = np.array([tcp_pose_origin[0], tcp_pose_origin[1], 0])
    radius = tcp_pose_origin[2]

    tcp_poses = sort_tcp_poses(tcp_poses, sphere_center)
    print('tcp_poses lens: ',len(tcp_poses))
