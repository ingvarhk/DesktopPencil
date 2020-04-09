# Desktop Pencil
Desktop Pencil is a python package that will allow you to draw small images on your screen. Install the package via PyPi [here](https://pypi.org/project/DesktopPencil/). Desktop Pencil is best at drawing small images.

### Exampel
This exampel will draw a small frog on the screen for 5 seconds. The ```load``` function returns a list with all the needed pixels including the position. 
```python
import DesktopPencil

frog = DesktopPencil.load("frog.png", 50, 1005)
DesktopPencil.draw(frog, 5000)
```
<img src="/Exampels/1.PNG">
