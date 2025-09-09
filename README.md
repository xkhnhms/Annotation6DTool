# Annotation 6D API

This is a high-performance Annotation 6D API built with python.

## DataSets DIR

```
├── grasp_label
│   ├── 000_labels.npz
│   ├── 001_labels.npz
├── models
│   ├── 000
│   │   ├── nontextured.ply
│   └── 001
│       ├── nontextured.ply
└── scenes
    ├── scene_0000
    │   ├── mecheye                             # data of mecheye camera
    │   │   ├── cam0_wrt_table.npy
    │   │   ├── depth
    │   │   │   ├── 0000.png to 0255.png        # 256 depth images
    │   │   ├── params.json                     # camera intrinsic,external parameters
    │   │   ├── rgb
    │   │   │   ├── 0000.png to 0255.png        # 256 rgb images
    │   │   └── robot
    │   │       ├── 0000.txt to 0255.txt        # 256 robot poses ,split by '_' 
    │   ├── me_wrt_ob.npz                       # mecheye camera pose with respect to orbbec, shape: 256x(4x4)
    │   ├── object_id_list.txt                  # objects' id that appear in this scene, 0-indexed
    │   └── orbbec                              # data of orbbec camera
    │       ├── same structure as mecheye
    └── ... scene_000n

```

## 1 Features

- cameras
- grippers
- robots
- pose_transform

## 2 Installation

### optional dependencies 

```bash
pip install opencv-python pycocotools matplotlib onnxruntime onnx
```

## 2.1 mecheye 

### dependencies

```
sudo apt update
sudo apt install libflann-dev
```

1. API install

```bash
pip install MechEyeAPI
```

2. control camera

[Mech-Eye SDK 2.5.1](https://downloads.mech-mind.com/?tab=tab-sdk)

```bash
(base) byd@ubuntu:~/fs/sw$ sudo dpkg -i Mech-Eye_API_2.5.0_arm64.deb
Selecting previously unselected package mecheyeapi.
(Reading database ... 352025 files and directories currently installed.)
Preparing to unpack Mech-Eye_API_2.5.0_arm64.deb ...
Unpacking mecheyeapi (2.5.0) ...
Setting up mecheyeapi (2.5.0) ...
Removing /etc/ld.so.conf.d/mech-eye-sdk.conf.
Creating /etc/ld.so.conf.d/mech-eye-sdk.conf.
Reloading library path.

Installation summary:
Update libraries path                  [  OK  ]

Installation complete.
mech-eye-sdk installed in /opt/mech-mind/mech-eye-sdk

Processing triggers for libc-bin (2.35-0ubuntu3.9) ...
```

配置~/.bashrc   

```bash
export MECHEYE_SDK_PATH=/opt/mech-mind/mech-eye-sdk
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/mech-mind/mech-eye-sdk/lib

```


## 2.2   Annotation GUI

1. set SAM checkpoint path

```python
from Annotation6DAPI.label_gui import DatasetViewerApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = DatasetViewerApp(root,sam_checkpoint = '../weights/sam_vit_b_01ec64.pth')
    root.mainloop()
```

2. run AnnotationTool.py
```bash
cd examples
python AnnotationTool.py
```









