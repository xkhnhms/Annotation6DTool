from Annotation6DAPI.cameras.calib import hand_eye_calibration


if __name__=='__main__':

    chess_board_x_num=11
    chess_board_y_num=8
    chess_board_unit=10
    is_m=True
    is_angle=True

    save_txt_file_name='me_' 
    is_eye_in_hand=True

    images_folder = r"./images"
    hand_eye_calibration(images_folder, chess_board_x_num, chess_board_y_num, chess_board_unit,is_m,is_angle,save_txt_file_name, is_eye_in_hand,
                         is_show=True)

