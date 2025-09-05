from Annotation6DAPI.grippers.dhControlAG import AGGripperControl


if __name__=='__main__':
    # init dh gripper
    dh_client=AGGripperControl()
    dh_client.dh_init(True)
    while True:
        print("请输入指令： cmd: num  a:结束")
        cmd = input()
        if cmd == 'a':
            break
        else:
            # dh_client.control_gripper(int(cmd)) # 发送【0-1000】
            dh_client.rectificate_gripper(float(cmd))  # 发送距离,单位 mm [0-145mm]