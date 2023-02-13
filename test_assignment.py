screwhole_edge = 96 * (1/16) #screw dimensions
screwhole = .09 * 96

def inputWidth():
    input_width = 0
    while input_width < 3 or input_width > 7:
        input_width = float(input("Input a width (3-7 in): "))
    return input_width

def inputLength():
    input_length = 0
    while input_length < 3 or input_length > 7:
        input_length = float(input("Input a length (3-7 in): "))
    return input_length

def inputHeight():
    input_height = 0
    while input_height < 2 or input_height > 4:
        input_height = float(input("Input a height (2-4 in): "))
    return input_height

def topMsg():
    msg = input('Input a custom message to put on the lid! (Max 25 Characters): ')
    while len(msg) > 25:
        msg = input('The message exceeded 25 characters. Input a custom message to put on the lid! (Max 25 Characters): ')
    return msg

def sideMsg():
    msg = input('Input a custom message to put on one side! (Max 25 Characters): ')
    while len(msg) > 25:
        msg = input('The message exceeded 25 characters. Input a custom message to put on one side! (Max 25 Characters): ')
    return msg

'''
create screw holes
side determines if it's on the length or width section
location determines if it's in the front or the back section for width
and left or right if it's length
'''

def hole(svg, side, location, start_x, start_y, rec_length, rec_width):
        if side == "l" and location == "l": #length and left
            for i in range(1, 3, 1):          
                svg.write('<circle cx = "{}" cy = "{}" r = "{}" ' \
                    'stroke-width="1" stroke="black" fill="none"/>\n'.format(screwhole_edge + start_x, i * rec_length/3 + start_y, screwhole/2))
        elif side == "w" and location == "b": #width and back
            for i in range(1, 3, 1):          
                svg.write('<circle cx = "{}" cy = "{}" r = "{}" ' \
                    'stroke-width="1" stroke="black" fill="none"/>\n'.format(i * rec_width/3 + start_x, screwhole_edge + start_y, screwhole/2))
        elif side == "l" and location == "r": #length and right
            for i in range(1, 3, 1):          
                svg.write('<circle cx = "{}" cy = "{}" r = "{}" ' \
                    'stroke-width="1" stroke="black" fill="none"/>\n'.format(-screwhole_edge + start_x + rec_width, i * rec_length/3 + start_y, screwhole/2))
        elif side == "w" and location == "f": #width and front
            for i in range(1, 3, 1):          
                svg.write('<circle cx = "{}" cy = "{}" r = "{}" ' \
                    'stroke-width="1" stroke="black" fill="none"/>\n'.format(i * rec_width/3 + start_x, -screwhole_edge + start_y + rec_length, screwhole/2))

def slot(svg, side, location, start_x, start_y, rec_length, rec_width):
    if side == "l" and location == "l": #length and left                
        for i in range(1, 3, 1):   
            slotx = start_x 
            sloty = i * rec_length/3 + start_y + .045*96       
            svg.write('<polyline points = "{},{} {},{} {},{} {},{} {},{} {},{}, {},{} {},{} {},{} {},{} {},{} {},{}" ' \
                'stroke-width="1" stroke="black" fill="none" transform="rotate(270,{},{})"/>\n'.format(slotx, sloty, slotx, sloty+.155*96,  
                slotx-.05*96, sloty+.155*96, slotx-.05*96, sloty+.225*96, slotx, sloty+.225*96,
                slotx, sloty+.38*96, slotx+.09*96, sloty+.38*96, slotx+.09*96, sloty+.225*96, 
                slotx+.14*96, sloty+.225*96, slotx+.14*96, sloty+.155*96, slotx+.09*96, sloty+.155*96, 
                slotx+.09*96, sloty, slotx, sloty))  
    elif side == "w" and location == "b": #width and back
        for i in range(1, 3):  
            slotx = i * rec_width/3 + start_x - .045*96
            sloty = start_y         
            svg.write('<polyline points = "{},{} {},{} {},{} {},{} {},{} {},{}, {},{} {},{} {},{} {},{} {},{} {},{}" ' \
                'stroke-width="1" stroke="black" fill="none"/>\n'.format(slotx, sloty, slotx, sloty+.155*96,  
                slotx-.05*96, sloty+.155*96, slotx-.05*96, sloty+.225*96, slotx, sloty+.225*96,
                slotx, sloty+.38*96, slotx+.09*96, sloty+.38*96, slotx+.09*96, sloty+.225*96, 
                slotx+.14*96, sloty+.225*96, slotx+.14*96, sloty+.155*96, slotx+.09*96, sloty+.155*96, 
                slotx+.09*96, sloty))               
    elif side == "l" and location == "r": #length and right                
        for i in range(1, 3, 1): 
            slotx = start_x + rec_width
            sloty = i * rec_length/3 + start_y - .045*96         
            svg.write('<polyline points = "{},{} {},{} {},{} {},{} {},{} {},{}, {},{} {},{} {},{} {},{} {},{} {},{}" ' \
                'stroke-width="1" stroke="black" fill="none" transform="rotate(90,{},{})"/>\n'.format(slotx, sloty, slotx, sloty+.155*96,  
                slotx-.05*96, sloty+.155*96, slotx-.05*96, sloty+.225*96, slotx, sloty+.225*96,
                slotx, sloty+.38*96, slotx+.09*96, sloty+.38*96, slotx+.09*96, sloty+.225*96, 
                slotx+.14*96, sloty+.225*96, slotx+.14*96, sloty+.155*96, slotx+.09*96, sloty+.155*96, 
                slotx+.09*96, sloty, slotx, sloty))  
    elif side == "w" and location == "f": #width and front                
        for i in range(1, 3, 1):    
            slotx = i * rec_width/3 + start_x + .045*96
            sloty = start_y + rec_length      
            svg.write('<polyline points = "{},{} {},{} {},{} {},{} {},{} {},{}, {},{} {},{} {},{} {},{} {},{} {},{}" ' \
                'stroke-width="1" stroke="black" fill="none" transform="rotate(180,{},{})"/>\n'.format(slotx, sloty, slotx, sloty+.155*96,  
                slotx-.05*96, sloty+.155*96, slotx-.05*96, sloty+.225*96, slotx, sloty+.225*96,
                slotx, sloty+.38*96, slotx+.09*96, sloty+.38*96, slotx+.09*96, sloty+.225*96, 
                slotx+.14*96, sloty+.225*96, slotx+.14*96, sloty+.155*96, slotx+.09*96, sloty+.155*96, 
                slotx+.09*96, sloty, slotx, sloty))

def lidSlot(svg, start_x, start_y, rec_width):
    lidx = rec_width/2 + start_x  - .5*96
    lidy =  start_y 
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
        'stroke-width="1" stroke="black" fill="none"/>\n'.format(lidx, lidy, 1*96, .125*96))

def lidOutline(svg, start, length, width, T):
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
            'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0], start[1], width/2 - .5*96, T))
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
        'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0], start[1], T, length/2 - .5*96))
    #top right corner
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
        'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0] + width/2 + .5*96, start[1], width/2 - .5*96, T))
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
        'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0] + width - T, start[1], T, length/2 - .5*96))
    #bottom left corner
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
        'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0], start[1] + length - T, width/2 - .5*96, T))
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
        'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0], start[1] + length/2 + .5*96, T, length/2 - .5*96))
    #bottom right corner
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
        'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0] + width/2 + .5*96, start[1] + length - T, width/2 - .5*96, T))
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
        'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0] + width - T, start[1] + length/2 + .5*96, T, length/2 - .5*96))

def create_panel(svg, width, length, side, start, msg=''):
    T = .125 * 96

    if side == 'width':
        width = width
        length = length - T
    elif side == 'length':
        width = width - 2*T
        length = length - T
    
    svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
            'stroke-width="1" stroke="black" fill="none"/>\n'.format(start[0], start[1], width, length))

    if side == 'base':
        hole(svg, "w", "f", start[0], start[1], length, width)
        hole(svg, "w", "b", start[0], start[1], length, width)
        hole(svg, "l", "r", start[0], start[1], length, width)
        hole(svg, "l", "l", start[0], start[1], length, width)
    elif side == 'width':
        hole(svg, "l", "l", start[0], start[1], length, width)
        hole(svg, "l", "r", start[0], start[1], length, width)
        slot(svg, "w", "f", start[0], start[1], length, width)
        lidSlot(svg, start[0], start[1], width)
        if msg != '':
            svg.write('<text x="{}" y="{}" font-size="{}" dominant-baseline="central" ' \
                'text-anchor="middle"> Digital Manufacturing </text>\n'.format(start[0] + width/2, 
                start[1] + length/2, width / 96 * 5))
    elif side == 'length':
        slot(svg, "w", "f", start[0], start[1], length, width)
        slot(svg, "l", "l", start[0], start[1], length, width)
        slot(svg, "l", "r", start[0], start[1], length, width)
        lidSlot(svg, start[0], start[1], width)
    elif side == 'lid':
        lidOutline(svg, start, length, width, T)
        if msg != '':
            svg.write('<text x="{}" y="{}" font-size="{}" dominant-baseline="central" ' \
                    'text-anchor="middle"> {} </text>\n'.format(start[0] + width/2, 
                    start[1] + length/2, width / 96 * 7, msg))

        

def main():
    start_x = 50
    start_y = 50
    
    width, length, height = 96 * inputWidth(), 96 * inputLength(), 96 * inputHeight()  # (96 pixels to an inch) * inches
    lid_msg = topMsg()
    side_msg = sideMsg()
    filename = input("Input a file name for the svg file: ")

    with open("{}.svg".format(filename), "w") as svg:
        svg.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n') #xml version
        
        svg.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" ' \
            '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n') #doctype
        
        svg.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" ' \
            'width="1152" height="1728" viewbox="0 0 1152 1728" version="1.1">\n') #svg tag kms
         
        create_panel(svg, width, length, "base", (start_x, start_y))
        create_panel(svg, width, height, "width", (start_x, start_y + length + 10))
        create_panel(svg, width, height, "width", (start_x, start_y + length + height + 10), msg=side_msg)
        create_panel(svg, width, length, "lid", (start_x, start_y + length + (2 * height) + 10), msg=lid_msg)
        create_panel(svg, length, height, "length", (start_x + width + 10, start_y))
        create_panel(svg, length, height, "length", (start_x + width + 10, start_y + height + 10))
        # create_panel(svg, width, length, "lid", (start_x + width + 10, start_y + length + height + 10), msg=lid_msg)

        svg.write('</svg>') #svg end tag
    
    print("{}.svg has been created.".format(filename))

if __name__=="__main__":
    main()