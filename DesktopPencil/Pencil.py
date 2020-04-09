import win32gui
import win32api
from win32api import GetSystemMetrics
from PIL import Image
import time


class DesktopPencil:
    
    def __init__(self):
        self.screen_width = GetSystemMetrics(0)
        self.screen_height = GetSystemMetrics(1)
        
        self.dc = win32gui.GetDC(0)

    def load(self, file, start_pos_x, start_pos_y, **kwargs):
        
        rotation = kwargs.get('rotation', 0)
        size = kwargs.get('size', None)
        
        im = Image.open(file)
        im = im.rotate(180)
        if size != None:
            im = im.resize(size)
        
        pixels = im.load()
        
        height = im.size[0]
        width = im.size[1]

        
        self.to_draw = []
        
        for x in range(0, width):
            for y in range(0, height):
                try:
                    color = pixels[x,y]
                except:
                    break
        
                r = color[0]
                g = color[1]
                b = color[2]
        
                try:
                    opacity = color[3]
                except:
                    opacity = 1
                
                rgb_color = win32api.RGB(r,g,b)
                
                if opacity != 0:
                    self.to_draw.append([start_pos_x + x,start_pos_y + y,rgb_color]) 
                    
      
    def draw(self, *args):
        try:
            duration = args[0]
        except:
            duration = None
        
        if duration != None:
            start = time.time()
            
            while True:
                elapsed = int((time.time() - start) * 1000)
                
                if not elapsed > duration:
                    for pixel in self.to_draw:
                        win32gui.SetPixel(self.dc, pixel[0], pixel[1], pixel[2])
                else:
                    break
        else:
            for pixel in self.to_draw:
                win32gui.SetPixel(self.dc, pixel[0], pixel[1], pixel[2])
                
            