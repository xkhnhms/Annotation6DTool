from Annotation6DAPI.cameras.calib import hand_eye_calibration


if __name__=='__main__':

    '''
        images_folder 下的文件名命名为： x_y_z_rx_ry_rz.png
            其中 x,y,z    单位为 m
                rx,ry,rz 单位为 角度
        
        文件名参考如下：
            -0.06498954930757_-0.5123334724211326_0.6388436056314158_176.38535577495972_-15.164498721856532_68.49861166645319.png
    '''

    chess_board_x_num=11    # 棋盘格横向角点数
    chess_board_y_num=8     # 棋盘格纵向角点数
    chess_board_unit=10     # 棋盘格尺寸
    is_m=True               # 机械臂x,y,z 单位是否为 m
    is_angle=True           # 机械臂rx,ry,rz 单位是否为 角度

    save_txt_file_name='me_'   # 保存的文件名
    is_eye_in_hand=True        # 是否为眼在手上手眼标定

    images_folder = r"./images"   # 标定采集的棋盘格图片文件夹
    hand_eye_calibration(images_folder, chess_board_x_num, chess_board_y_num, chess_board_unit,is_m,is_angle,save_txt_file_name, is_eye_in_hand,
                         is_show=True)

