from PIL import Image
import numpy as np
from tkinter import ttk
# from tk import *


class Interface(Frame):
    def __init__(self, window, width=800, height=600, **kwargs):
        super().__init__(window, width=width, height=height, **kwargs)
        self.pack(fill=BOTH)


if __name__ == "__main__":
    window = Tk()
    root = VideoDownloader(window)
    root.center()
    root.mainloop()
