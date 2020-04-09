# Desktop Pencil
This python package will allow you to draw small images on your screen. You will be able to rotate and resize your image before drawing it. Desktop Pencil can draw many image file formats such as PNG, JPG, GIF and ICO. Desktop Pencil is best at drawing small images with few pixels.

### Installation
If you have PIP installed you can simply run this command: `pip install DesktopPencil`
The package is uploaded to PyPi and can be also installed [here](https://pypi.org/project/DesktopPencil/).

### Exampel
This exampel will draw a frog on the screen for 5 seconds. The ```load``` function returns a list with all the needed pixels including the position of them.
```python
import DesktopPencil

frog = DesktopPencil.load("frog.png", 50, 1005)
DesktopPencil.draw(frog, 5000)
```
<img src="/Exampels/1.PNG">

### ```DesktopPencil.load()```
Rotation and size are optional arguments.
* ```file``` - The image you want to draw
* ```start_pos_x``` - Start position horizontal
* ```start_pos_y``` - Start position vertical
* ```rotation``` - Image rotation eg. 90
* ```size``` - Image size in tuple eg. (50,100)

### ```DesktopPencil.draw()```
Duration is an optional arguments.
* ```pixels``` - List returned from the ```load``` function
* ```duration``` - How long the image is visible in milliseconds eg. 3500
