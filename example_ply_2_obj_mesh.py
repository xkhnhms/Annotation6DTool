import os
from Annotation6DAPI.pose_transform.ply_2_obj_mesh import convert_ply_obj_mesh,mesh_to_pointcloud

if __name__=='__main__':


    ######## 1. mesh ply to pointcloud ply ########
    mesh_file = "models/001_mesh.ply"
    output_file = "001.ply"

    pcd = mesh_to_pointcloud(
        mesh_file,
        num_points=500000,
        visualize=True,
        save_path=output_file
    )


    ######## 2. ply to obj mesh  ########

    modelpath = 'models'
    obj_names = sorted([d for d in os.listdir(modelpath) if os.path.isdir(os.path.join(modelpath, d))])
    print("Found models:", obj_names)

    for obj_name in obj_names:
        print(f"\nProcessing {obj_name}")
        objpath = os.path.join(modelpath, obj_name)
        
        ply_file = os.path.join(objpath, 'nontextured.ply')
        obj_file = os.path.join(objpath, 'nontextured.obj')

        convert_ply_obj_mesh(ply_file,obj_file,is_show=True)

    print("\nAll done.")


