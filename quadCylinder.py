from functools import partial

#Window
cmds.window("Quad Cylinder", sizeable=True, resizeToFitChildren=True) 
cmds.columnLayout( adjustableColumn=True )                                             

#Text
cmds.separator(h=20)
cmds.text("Adjust Parameters of the Quad Cylinder")
cmds.separator(h=20)

#Stem Funcations
def adjustHeight(sliderHeight, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the stem radius value
        
    Adjusts the stem radius of the stem based on the slider value
    """
    
    valHeight = cmds.floatSliderGrp(sliderHeight, q=True, value=True)
    quadcylinderls = cmds.ls('quad*', long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    quadcylinderName = 'quad' + quadcylinderNumber
    cmds.select(quadcylinderName, r=True)
    cmds.setAttr('polyCylinder' + quadcylinderNumber + '.height', valHeight, **kwargs) 
    
def adjustRadius(sliderRadius, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the stem radius value
        
    Adjusts the stem radius of the stem based on the slider value
    """
    
    valRadius = cmds.floatSliderGrp(sliderRadius, q=True, value=True)
    quadcylinderls = cmds.ls('quad*', long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    quadcylinderName = 'quad' + quadcylinderNumber
    cmds.select(quadcylinderName, r=True)
    cmds.setAttr('polyCylinder' + quadcylinderNumber+ '.radius', valRadius, **kwargs) 
    
def adjustSubH(sliderSubH, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the stem radius value
        
    Adjusts the stem radius of the stem based on the slider value
    """
    
    quadcylinderls = cmds.ls('quad*', long=True)
    print(quadcylinderls)
    lengthName = len(quadcylinderls[len(quadcylinderls)-1])
    multipleDigitOffset = lengthName - 17
    quadcylinderName = quadcylinderls[len(quadcylinderls)-1][1:6+multipleDigitOffset]
    cmds.delete(quadcylinderName)
    base()
    
def adjustCap(sliderHeight, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the stem radius value
        
    Adjusts the stem radius of the stem based on the slider value
    """
    
    quadcylinderls = cmds.ls('quad*', long=True)
    lengthName = len(quadcylinderls[len(quadcylinderls)-1])
    multipleDigitOffset = lengthName - 17
    capName = quadcylinderls[len(quadcylinderls)-1][1:6+multipleDigitOffset]
    cmds.delete(capName)
    base()     
    
def adjustSubAx(sliderSubAx, *args, **kwargs):
    """
    sliderHeight: floatSliderGrp object holding the stem radius value
        
    Adjusts the stem radius of the stem based on the slider value
    """
    
    quadcylinderls = cmds.ls('quad*', long=True)
    lengthName = len(quadcylinderls[len(quadcylinderls)-1])
    multipleDigitOffset = lengthName - 17
    quadName = quadcylinderls[len(quadcylinderls)-1][1:6+multipleDigitOffset]
    cmds.delete(quadName)
    base()   

HeightSlider = cmds.floatSliderGrp(label='Height', columnAlign= (1,'right'), field=True, min=1, max=5, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(HeightSlider,  e=True, dc = partial(adjustHeight, HeightSlider))


RadiusSlider = cmds.floatSliderGrp(label='Radius', columnAlign= (1,'right'), field=True, min=1, max=5, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(RadiusSlider,  e=True, dc = partial(adjustRadius, RadiusSlider))

SubHSlider = cmds.intSliderGrp(label='Subdivision Height', columnAlign= (1,'right'), field=True, min=1, max=5, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(SubHSlider,  e=True, dc = partial(adjustSubH, SubHSlider))

CapSlider = cmds.intSliderGrp(label='Cap', columnAlign= (1,'right'), field=True, min=2, max=5, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(CapSlider,  e=True, dc = partial(adjustCap, CapSlider))

SubAxSlider = cmds.intSliderGrp(label='SubAx', columnAlign= (1,'right'), field=True, min=4, max=16, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(SubAxSlider,  e=True, dc = partial(adjustSubAx, SubAxSlider))


#Butto'
cmds.button(l = 'Create Cake Stand',  c = 'base()')
cmds.separator(h=20)
cmds.showWindow()

    
def base():
    radius= cmds.floatSliderGrp(RadiusSlider, q=True, value=True)
    height = cmds.floatSliderGrp(HeightSlider, q=True, value=True)
    subax = cmds.intSliderGrp(SubAxSlider, q=True, value=True)
    subheight = cmds.intSliderGrp(SubHSlider, q=True, value=True)
    subcap = cmds.intSliderGrp(CapSlider, q=True, value=True)
    if (subax%2 == 1):
        subax+=1
    totaledges = ((subcap*4)+((subheight*2)-1))*subax
    startEdgeToDelete = totaledges - subax*2
    finalStem = cmds.polyCylinder(n='quad#', r=radius, h=height, sx=subax, sy=subheight, sc=subcap)
    quadcylinderls = cmds.ls('quad*', long=True)
    lengthName = len(quadcylinderls[len(quadcylinderls)-1])
    multipleDigitOffset = lengthName - 17
    quadcylinderNumber= quadcylinderls[len(quadcylinderls)-1][5:6+multipleDigitOffset]
    
    stringTodelete = ''
    listtodel = []
    
    for i in range (startEdgeToDelete,totaledges,2):
        print (i)
        listtodel.append('quad' + str(quadcylinderNumber) + '.e[' + str(i) + ']')

        #if i != totaledges -2:
        #    stringTodelete = stringTodelete + 'quad1' + '.e[' + str(i) + ']' + ','
        #else:
        #    stringTodelete = stringTodelete + 'quad1' + '.e[' + str(i) + ']'
        
    #stringTodelete = stringTodelete + 'quad1' + '.e[' + str(startEdgeToDelete) + ']'
    #listtodel.append('quad1' + '.e[' + str(startEdgeToDelete) + ']')
    #listtodel.append('quad1' + '.e[' + str(startEdgeToDelete + 2) + ']')
    cmds.delete(listtodel)
