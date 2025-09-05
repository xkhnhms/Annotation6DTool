# Annotation 6D API

This is a high-performance Annotation 6D API built with python.

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

### 2.1 SAM [optional]

[SAM](https://github.com/facebookresearch/segment-anything)

Install Segment Anything:

```bash
pip install git+https://github.com/facebookresearch/segment-anything.git

```

or clone the repository locally and install with

``bash
git clone git@github.com:facebookresearch/segment-anything.git
cd segment-anything; pip install -e .
```

[Model Checkpoints](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b_01ec64.pth)

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










