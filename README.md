# Desktop Pencil
This python package will allow you to draw small images on your screen. You will be able to rotate and resize your image before drawing it. Desktop Pencil can draw many image file formats such as PNG, JPG, GIF and ICO. Desktop Pencil is best at drawing small images with few pixels.

Install the package via PyPi [here](https://pypi.org/project/DesktopPencil/). 

### Exampel
This exampel will draw a frog on the screen for 5 seconds. The ```load``` function returns a list with all the needed pixels including the position of them.
```python
import DesktopPencil

frog = DesktopPencil.load("frog.png", 50, 1005)
DesktopPencil.draw(frog, 5000)
```
<img src="/Exampels/1.PNG">
