from Annotation6DAPI.label_gui import DatasetViewerApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = DatasetViewerApp(root,sam_checkpoint = '../weights/sam_vit_b_01ec64.pth')
    root.mainloop()