import os
from Annotation6DAPI.cameras.mechEyeCamera import mechCamera

if __name__=='__main__':
    camera = mechCamera()

    SN_IP=camera.getIdxAndIP()
    print(SN_IP)

    camera.ConnectToCameraByDefault()
    camera.ConnectToCameraBySN('xxxxxxx')

    depth_image=camera.capture_depth_map()
    camera.depth_to_point_cloud(depth_image,is_show=True)


