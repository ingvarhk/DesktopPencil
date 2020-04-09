import DesktopPencil

frog_pixels = DesktopPencil.load("frog.png", 0, 500, rotation=270)
DesktopPencil.draw(frog_pixels, 1000)

cat_pixels = DesktopPencil.load("epic_glasses.png", 0, 0, size=(400,400))
DesktopPencil.draw(cat_pixels)