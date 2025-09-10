from Annotation6DAPI.cameras.capture_orbbecNet_image import ImageCapture


if __name__ == '__main__':

    orbbec_lib_path = 'OrbbecSDK/lib_arm/'
    camera_ip = "169.254.4.153"
    robot_ip = "169.254.4.70"
    root_dir = 'imgs'
    
    capture = ImageCapture(camera_ip, robot_ip, root_dir,orbbec_lib_path)
    capture.run()
