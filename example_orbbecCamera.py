import cv2
from Annotation6DAPI.cameras.orbbecCamera import orbCamera

if __name__=='__main__':
    lib_path = '/home/ls/fs/codes/object-grasp-annotation/camera/OrbbecSDK/lib_arm/'
    orbbecs = orbCamera(lib_path = lib_path, ip = "169.254.217.153",align_mode = "SW",enable_sync = True)
    color_image, depth_data, depth_image = orbbecs.getColorDepthData()

    cv2.imshow("SyncAlignViewer ", color_image)
    cv2.waitKey(1000)
    cv2.imshow("SyncAlignViewer ", depth_image)
    cv2.waitKey(1000)


