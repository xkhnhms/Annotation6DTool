from Annotation6DAPI.cameras.capture_mecheye_image_robot import Capture2DStreamRobot


if __name__ == '__main__':
    streamer = Capture2DStreamRobot(robot_ip = '169.254.4.70',save_directory = "./saved_images",use_idx=False)
    streamer.main()

