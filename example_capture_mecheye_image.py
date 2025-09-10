from Annotation6DAPI.cameras.capture_mecheye_image import Capture2DStream


if __name__ == '__main__':
    streamer = Capture2DStream(robot_ip = '169.254.4.70',save_directory = "./saved_images")
    streamer.main()

