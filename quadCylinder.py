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
    sliderHeight: floatSliderGrp object holding the cylinder height value
        
    Adjusts the cylinder height based on the slider value
    """
    
    valHeight = cmds.floatSliderGrp(sliderHeight, q=True, value=True)
    quadcylinderls = cmds.ls('quad*', long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    quadcylinderName = 'quad' + quadcylinderNumber
    cmds.select(quadcylinderName, r=True)
    print(quadcylinderName)
    cmds.setAttr('polyCylinder' + quadcylinderNumber + '.height', valHeight, **kwargs) 
    
def adjustRadius(sliderRadius, *args, **kwargs):
    """
    sliderRadius: floatSliderGrp object holding the cylinder radius value
        
    Adjusts the cylinder radius based on the slider value
    """
    
    valRadius = cmds.floatSliderGrp(sliderRadius, q=True, value=True)
    quadcylinderls = cmds.ls('quad*', long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    quadcylinderName = 'quad' + quadcylinderNumber
    cmds.select(quadcylinderName, r=True)
    print(quadcylinderName)
    cmds.setAttr('polyCylinder' + quadcylinderNumber+ '.radius', valRadius, **kwargs) 
    
def adjustSubH(sliderSubH, *args, **kwargs):
    """
    sliderSubH: floatSliderGrp object holding the cylinder subdivision height value
        
    Adjusts the cylinder subdivision height based on the slider value
    """
    
    quadcylinderls = cmds.ls('quad*', long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    quadcylinderName = 'quad' + quadcylinderNumber
    print(quadcylinderName)
    cmds.delete(quadcylinderName)
    base()
    
def adjustCap(sliderCap, *args, **kwargs):
    """
    sliderCap: floatSliderGrp object holding the cylinder subdivision cap value
        
    Adjusts the cylinder subdivision cap based on the slider value
    """
    
    quadcylinderls = cmds.ls('quad*', long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    quadcylinderName = 'quad' + quadcylinderNumber
    print(quadcylinderName)
    cmds.delete(quadcylinderName)
    base()     
    
def adjustSubAx(sliderSubAx, *args, **kwargs):
    """
    sliderSubAx: floatSliderGrp object holding the cylinder subdivision axis value
        
    Adjusts the cylinder subdivision axis based on the slider value
    """
    
    quadcylinderls = cmds.ls('quad*', long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    quadcylinderName = 'quad' + quadcylinderNumber
    print(quadcylinderName)
    cmds.delete(quadcylinderName)
    base()   

HeightSlider = cmds.floatSliderGrp(label='Height', columnAlign= (1,'right'), field=True, min=1, max=5, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(HeightSlider,  e=True, dc = partial(adjustHeight, HeightSlider))

RadiusSlider = cmds.floatSliderGrp(label='Radius', columnAlign= (1,'right'), field=True, min=1, max=5, value=0, step=0.1, dc = 'empty')
cmds.floatSliderGrp(RadiusSlider,  e=True, dc = partial(adjustRadius, RadiusSlider))

SubHSlider = cmds.intSliderGrp(label='Subdivision Height', columnAlign= (1,'right'), field=True, min=1, max=5, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(SubHSlider,  e=True, dc = partial(adjustSubH, SubHSlider))

CapSlider = cmds.intSliderGrp(label='Cap', columnAlign= (1,'right'), field=True, min=2, max=5, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(CapSlider,  e=True, dc = partial(adjustCap, CapSlider))

SubAxSlider = cmds.intSliderGrp(label='SubAx', columnAlign= (1,'right'), field=True, min=6, max=100, value=0, step=0.1, dc = 'empty')
cmds.intSliderGrp(SubAxSlider,  e=True, dc = partial(adjustSubAx, SubAxSlider))


#Butto'
cmds.button(l = 'Create Quad Cylinder',  c = 'base()')
cmds.separator(h=20)
cmds.showWindow()

    
def base():
    radius= cmds.floatSliderGrp(RadiusSlider, q=True, value=True)
    height = cmds.floatSliderGrp(HeightSlider, q=True, value=True)
    subax = cmds.intSliderGrp(SubAxSlider, q=True, value=True)
    subheight = cmds.intSliderGrp(SubHSlider, q=True, value=True)
    subcap = cmds.intSliderGrp(CapSlider, q=True, value=True)
    #quaded cylinders can only have an even subdivision axis number, so this ensures that it will only be set to an even number
    if (subax%2 == 1):
        subax+=1
    totaledges = ((subcap*4)+((subheight*2)-1))*subax
    startEdgeToDelete = totaledges - subax*2
    cylinder = cmds.polyCylinder(n='quad#', r=radius, h=height, sx=subax, sy=subheight, sc=subcap)
    quadcylinderls = cmds.ls('quad*', long=True)
    quadcylinderNumber= str(len(quadcylinderls)/2)
    
    #deleting every other edge in the inner most circle of the cylinder to turn the inner triangles into quads
    listtodel = []
    for i in range (startEdgeToDelete,totaledges,2):
        listtodel.append('quad' + str(quadcylinderNumber) + '.e[' + str(i) + ']')
    cmds.delete(listtodel)
