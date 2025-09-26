from Annotation6DAPI.cameras.capture_orbbecSDK_image_robot import ImageCaptureSDKRobot

if __name__ == '__main__':

    orbbec_lib_path = 'OrbbecSDK/lib_arm/'
    camera_ip = "169.254.4.153"
    robot_ip = "169.254.4.70"
    root_dir = 'imgs'
    
    capture = ImageCaptureSDKRobot(camera_ip, robot_ip, root_dir,orbbec_lib_path)
    capture.run()
