app.background = gradient('dodgerBlue', 'navy')

dot1 = Circle(100, 100, 10, fill=gradient('lightCoral', 'crimson'))
dot2 = Circle(300, 100, 10, fill=gradient('lightCoral', 'crimson'))
dot3 = Circle(100, 300, 10, fill=gradient('lightCoral', 'crimson'))
dot4 = Circle(300, 300, 10, fill=gradient('lightCoral', 'crimson'))

Line(0, 200, 400, 200, dashes=True)
Line(200, 400, 200, 0, dashes=True)

def onMouseMove(mouseX, mouseY):
    dot1.centerX = mouseX
    dot1.centerY = mouseY
    dot2.centerX = 400 - mouseX
    dot2.centerY = mouseY
    dot3.centerX = mouseX 
    dot3.centerY = 400 - mouseY
    dot4.centerX = 400 - mouseX
    dot4.centerY = 400 - mouseY
    pass
