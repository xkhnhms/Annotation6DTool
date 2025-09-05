import os
from Annotation6DAPI.pose_transform.me_wrt_ob_tools import me_wrt_ob

if __name__=='__main__':

    json_path_mech = os.path.join('./grasp_datasets_origin/scenes/scene_0000/mecheye', 'params.json')
    json_path_orbbec = os.path.join('./grasp_datasets_origin/scenes/scene_0000/orbbec', 'params.json')
    save_json_path = os.path.join('./grasp_datasets_origin/scenes/scene_0000','me_wrt_ob.json')

    me_wrt_ob(json_path_mech, json_path_orbbec,save_json_path)


