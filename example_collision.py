from Annotation6DAPI.utils.collisionUtils import scene_collision_detection_gpu,vis_recontruct_collision_camera


if __name__=='__main__':
    # dataset_root = '/home/ls/fs/codes/object-grasp-annotation/Data/scenes/scene_0000/mecheye'
    # dataset_root = '/home/ls/fs/codes/object-grasp-annotation/grasp_datasets/scenes/scene_0001/mecheye'

    # dataset_root = '/home/ls/fs/codes/object-grasp-annotation/camera/grasp_datasets_origin/scenes/scene_0001/mecheye'
    # model_root = '/home/ls/fs/codes/object-grasp-annotation/grasp_datasets/models'

    dataset_root = '/home/ls/fs/codes/object-grasp-annotation/camera/grasp_datasets_origin/scenes/scene_0001/mecheye'
    model_root = '/home/ls/fs/codes/object-grasp-annotation/camera/grasp_datasets_origin/models'

    scene_idx = 1  # 0
    anno_idx = 0  # 0
    # 单CPU
    # scene_collision_detection_single_cpu(dataset_root,
    #                           scene_idx,
    #                           anno_idx,
    #                           model_root,
    #                           voxel_size=0.008,# 0.005
    #                           approach_dist=0.02, 
    #                           collision_thresh=0.002, 
    #                           show_gripper_num=100, 
    #                           align=False,  # True
    #                           is_show = False
    #                         )
    
    # # 多线程
    # scene_collision_detection_parallel(dataset_root,
    #                           scene_idx,
    #                           anno_idx,
    #                           model_root,
    #                           voxel_size=0.006,  # 0.005
    #                           approach_dist=0.05, # 0.02
    #                           collision_thresh=0.001,  # 0.002
    #                           show_gripper_num=100, 
    #                           align=False, 
    #                           is_show = False
    #                         )

    # GPU
    scene_collision_detection_gpu(dataset_root,
                              scene_idx,
                              anno_idx,
                              model_root,
                              voxel_size=0.003,  # 0.005  0.004
                              approach_dist=0.03, 
                              collision_thresh=0.005,  # 0.002
                              show_gripper_num=100, 
                              align=True,   # False
                              is_show = False,
                              is_custom=False
                            )
    
    # # camera
    # # scene_collision_detection(dataset_root,scene_idx,anno_idx,model_root,voxel_size=0.005,approach_dist=0.02, collision_thresh=0.005, show_gripper_num=100, align=False, is_show = True)
    


    # vis on robot base
    # vis_recontruct_collision_robot_base(dataset_root,
    #                                     scene_idx, 
    #                                     anno_idx,model_root, 
    #                                     voxel_size=0.005, 
    #                                     approach_dist=0.02, 
    #                                     collision_thresh=0.005, 
    #                                     show_gripper_num=50
    #                                 )
     

    # post_check_collision_labels(dataset_root,scene_idx,anno_idx,model_root,align=False)
    
    vis_recontruct_collision_camera(dataset_root,
                                    scene_idx, 
                                    anno_idx,model_root, 
                                    show_gripper_num=50     # 50
                                )

    # vis_realScene_collision_camera(dataset_root,scene_idx, anno_idx,model_root, show_gripper_num=50)
     

    # # data root
    # dataset_root = '/home/ls/fs/codes/object-grasp-annotation/camera/grasp_datasets_origin/scenes/'
    # model_root = '/home/ls/fs/codes/object-grasp-annotation/grasp_datasets/models'
    # # scene_idx = 1
    # anno_idx = 0

    # scene_nums = len([d for d in os.listdir(dataset_root) if os.path.isdir(os.path.join(dataset_root, d))])
    # print(scene_nums)
    # for scene_idx in range(0,scene_nums):
    #     current_scene = os.path.join(dataset_root,f'scene_{scene_idx:04d}', 'mecheye')
    #     scene_collision_detection_gpu(current_scene,
    #                         scene_idx,
    #                         anno_idx,
    #                         model_root,
    #                         voxel_size=0.003,  # 0.005  0.004
    #                         approach_dist=0.03, 
    #                         collision_thresh=0.005,  # 0.002
    #                         show_gripper_num=100, 
    #                         align=True,   # False
    #                         is_show = False,
    #                         is_custom=False
    #                     )

    #     print(f'scene {scene_idx} has finished!')

