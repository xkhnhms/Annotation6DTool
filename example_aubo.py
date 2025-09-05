from Annotation6DAPI.robots.AUBO import AuboRobot


if __name__ == '__main__':
    robot=AuboRobot("169.254.4.70")
    angle_cert_pose=robot.getTcpAnglePose()
    angle_joint_pose=robot.getJointPositionsAngle()


