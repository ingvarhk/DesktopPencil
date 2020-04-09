import win32gui
import win32api
from win32api import GetSystemMetrics
from PIL import Image
import time

        
screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1)
    
dc = win32gui.GetDC(0)

def load(file, start_pos_x, start_pos_y, **kwargs):

    if not type(start_pos_x) == int:
        raise TypeError("Start position has to be an integer")
    if not type(start_pos_y) == int:
        raise TypeError("Start position has to be an integer")

    rotation = kwargs.get('rotation', 0)
    
    if not type(rotation) == int or rotation > 360 or rotation < 0:
        raise TypeError("Rotation has to be an integer between 0 and 360")
        
    size = kwargs.get('size', None)
    if size != None:
        if not type(size) == tuple:
            raise TypeError("Size has to be a tuple")
    
    try:
        im = Image.open(file)
    except FileNotFoundError:
        raise FileNotFoundError("Image '" + str(file) + "' not found")
        
    im = im.rotate(rotation)
    
    if size != None:
        im = im.resize(size)
    
    pixels = im.load()
    
    height = im.size[0]
    width = im.size[1]

    
    to_draw = []
    
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
                to_draw.append([start_pos_x + x,start_pos_y + y,rgb_color])
                
    return to_draw
                
  
def draw(pixels, *args):
    
    if not type(pixels) == list:
        raise TypeError("Invalid pixels. Use the list returned from the 'load' function")
    
    try:
        duration = args[0]
    except:
        duration = None
    
    if duration != None:
        start = time.time()
        
        while True:
            try:
                elapsed = int((time.time() - start) * 1000)
                
                if not elapsed > duration:
                    for pixel in pixels:
                        win32gui.SetPixel(dc, pixel[0], pixel[1], pixel[2])
                else:
                    break
            except:
                raise TypeError("Invalid pixels. Use the list returned from the 'load' function")
    else:
        for pixel in pixels:
            win32gui.SetPixel(dc, pixel[0], pixel[1], pixel[2])
            
        