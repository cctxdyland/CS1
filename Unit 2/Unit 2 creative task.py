app.background = 'gray'

# the speaker
speakerBackground = Circle(200,200,120)
speakerSurround = Circle(200,200,120, fill=None, border=gradient('black', 'black', 'black', rgb(40,40,40), rgb(58,61,68),start='center'), borderWidth=22)
cone1 = Circle(200,200,99, border='khaki', dashes=True)
cone2 = Circle(200,200,95, border='khaki', dashes=True)
dustcap = Circle(200,200,50, fill=rgb(44,45,50), border=rgb(111,113,123))


# music notes
qNoteOval = Oval(-200,-200,40,30, rotateAngle=-20)
qNoteLine = Line(qNoteOval.centerX + 16.3, qNoteOval.centerY, qNoteOval.centerX+16, qNoteOval.centerY-100, lineWidth=6)
def quarterNote(locationX, locationY):
    qNoteOval.centerX = locationX
    qNoteOval.centerY = locationY
    qNoteLine.x1 = qNoteOval.centerX + 16.3
    qNoteLine.y1 = qNoteOval.centerY
    qNoteLine.x2 = qNoteOval.centerX+16 
    qNoteLine.y2 = qNoteOval.centerY-100
    pass

qNoteOval2 = Oval(-200,-200,40,30, rotateAngle=-20)
qNoteLine2 = Line(qNoteOval2.centerX + 16.3, qNoteOval2.centerY, qNoteOval2.centerX+16, qNoteOval2.centerY-100, lineWidth=6)
def quarterNote2(locationX, locationY):
    qNoteOval2.centerX = locationX
    qNoteOval2.centerY = locationY
    qNoteLine2.x1 = qNoteOval2.centerX + 16.3
    qNoteLine2.y1 = qNoteOval2.centerY
    qNoteLine2.x2 = qNoteOval2.centerX+16 
    qNoteLine2.y2 = qNoteOval2.centerY-100
    pass

qNoteOval3 = Oval(-200,-200,40,30, rotateAngle=-20)
qNoteLine3 = Line(qNoteOval3.centerX + 16.3, qNoteOval3.centerY, qNoteOval3.centerX+16, qNoteOval3.centerY-100, lineWidth=6)
def quarterNote3(locationX, locationY):
    qNoteOval3.centerX = locationX
    qNoteOval3.centerY = locationY
    qNoteLine3.x1 = qNoteOval3.centerX + 16.3
    qNoteLine3.y1 = qNoteOval3.centerY
    qNoteLine3.x2 = qNoteOval3.centerX+16 
    qNoteLine3.y2 = qNoteOval3.centerY-100
    pass

qNoteOval4 = Oval(-200,-200,40,30, rotateAngle=-20)
qNoteLine4 = Line(qNoteOval4.centerX + 16.3, qNoteOval4.centerY, qNoteOval4.centerX+16, qNoteOval4.centerY-100, lineWidth=6)
def quarterNote4(locationX, locationY):
    qNoteOval4.centerX = locationX
    qNoteOval4.centerY = locationY
    qNoteLine4.x1 = qNoteOval4.centerX + 16.3
    qNoteLine4.y1 = qNoteOval4.centerY
    qNoteLine4.x2 = qNoteOval4.centerX+16 
    qNoteLine4.y2 = qNoteOval4.centerY-100
    pass

# random music note color thing
def rainbowNotes():
    if 0.1 > random():
        qNoteOval.fill = 'gold'
        qNoteLine.fill = 'gold'
    elif 0.2 > random():
        qNoteLine2.fill = 'deepSkyBlue'
        qNoteOval2.fill = 'deepSkyBlue'
    elif 0.3 > random():
        qNoteLine3.fill = 'darkViolet'
        qNoteOval3.fill = 'darkViolet'
    elif 0.4 > random():
        qNoteLine4.fill = 'maroon'
        qNoteOval4.fill = 'maroon'
    elif 0.7 > random():
        qNoteLine.fill = 'khaki'
        qNoteOval.fill = 'khaki'
        qNoteLine2.fill = 'khaki'
        qNoteOval2.fill = 'khaki'
        qNoteLine3.fill = 'khaki'
        qNoteOval3.fill = 'khaki'
        qNoteLine4.fill = 'khaki'
        qNoteOval4.fill = 'khaki'

# speaker moving functions
def bump():
    cone1.radius = 88
    cone2.radius = 85
    dustcap.radius = 40
    pass

def reverseBump():
    cone1.radius = 98
    cone2.radius = 95
    dustcap.radius = 50
    pass

# mouse events
musicTime = Label('Music Time Brwah', -200,-200, fill='white', size=20, font='orbitron')
def onMousePress(mouseX, mouseY):
    musicTime.centerX = 200
    musicTime.centerY = 40
    musicTime.visible=True
    quarterNote(50,350)
    quarterNote2(50, 125)
    quarterNote3(350,350)
    quarterNote4(350,125)
    qNoteOval.visible = True
    qNoteLine.visible = True
    qNoteOval2.visible = True
    qNoteLine2.visible = True
    qNoteOval3.visible = True
    qNoteLine3.visible = True
    qNoteOval4.visible = True
    qNoteLine4.visible = True
    musicTime.visible = True
    rainbowNotes()
    bump()

def onMouseRelease(mouseX, mouseY):
    qNoteOval.visible = False
    qNoteLine.visible = False
    qNoteOval2.visible = False
    qNoteLine2.visible = False
    qNoteOval3.visible = False
    qNoteLine3.visible = False
    qNoteOval4.visible = False
    qNoteLine4.visible = False
    musicTime.visible = False
    reverseBump()
  
