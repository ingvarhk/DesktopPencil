# Desktop Pencil
Desktop Pencil is a python package that will allow you to draw small images on your screen. Install the package via PyPi [here](https://pypi.org/project/DesktopPencil/)

This exampel will draw a frog on the screen for 5 seconds.
```python
import DesktopPencil

frog = DesktopPencil.load("frog.png", 50, 1005)
DesktopPencil.draw(frog, 5000)
```
<img src="/Exampels/1.PNG">
