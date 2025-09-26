from Annotation6DAPI.cameras.capture_orbbecSDK_image import ImageCaptureSDK

if __name__ == '__main__':

    orbbec_lib_path = 'OrbbecSDK/lib_arm/'
    camera_ip = "169.254.4.153"
    # robot_ip = "169.254.4.70"
    root_dir = 'imgs'
    
    capture = ImageCaptureSDK(camera_ip, root_dir,orbbec_lib_path)
    capture.run()
