def inputWidth():
    input_width = 0
    while input_width < 1 or input_width > 7:
        input_width = float(input("Input a width (1-7 in): "))
    return input_width

def inputLength():
    input_length = 0
    while input_length < 1 or input_length > 7:
        input_length = float(input("Input a length (1-7 in): "))
    return input_length

def inputHeight():
    input_height = 0
    while input_height < 1 or input_height > 5:
        input_height = float(input("Input a height (1-7 in): "))
    return input_height

def inputHorCompartment():
    input_Horcompartment = 0
    while input_Horcompartment < .5 or input_Horcompartment > 5:  #input_length instead of 5 but need it to be a global variable
        input_Horcompartment = float(input("How far from the front do you want the compartment (1-5 in): "))
    return input_Horcompartment

def inputVerCompartment():
    input_Vercompartment = 0
    while input_Vercompartment < 1 or input_Vercompartment > 5: #input_width instead of 5 but need it to be a global variable
        input_Vercompartment = float(input("How far from the right do you want the compartment (1-5 in): "))
    return input_Vercompartment

def inputInitials():
    while True:
        cand_initials = input('Input your initials (max 3): ')
        if len(cand_initials) <= 3:
            if cand_initials.isalpha() or cand_initials == '':
                return cand_initials.upper()
            else:
                print('Invalid input')
        else:
            print('Invalid Input')

def main():
    start_x = 100
    start_y = 100
    thickness = .125

    #initials = inputInitials()
    rec_width = 96 * inputWidth()  # (96 pixels to an inch) * inches
    rec_length = 96 * inputLength()
    #rec_height = 96 * inputHeight() 

    #screw dimensions
    screwhole_edge = .25 * 96
    screwhole = .086

    #create screw holes
    #side determines if it's on the length or width section
    #location determines if it's in the front or the back section for width
    #and left or right if it's length
    def hole(side, location):
        if side == "l" and location == "l": #length and left
            for i in range(1, 3, 1):          
                dot = svg.write('<circle cx = "{}" cy = "{}" r = "{}" ' \
                    'stroke-width="2" stroke="black" fill="black"/>\n'.format(screwhole_edge + start_x, i * rec_length/3 + start_y, screwhole))
            return dot
        elif side == "w" and location == "b": #width and back
            for i in range(1, 3, 1):          
                dot = svg.write('<circle cx = "{}" cy = "{}" r = "{}" ' \
                    'stroke-width="2" stroke="black" fill="black"/>\n'.format(i * rec_width/3 + start_x, screwhole_edge + start_y, screwhole))
            return dot
        elif side == "l" and location == "r": #length and right
            for i in range(1, 3, 1):          
                dot = svg.write('<circle cx = "{}" cy = "{}" r = "{}" ' \
                    'stroke-width="2" stroke="black" fill="black"/>\n'.format(-screwhole_edge + start_x + rec_width, i * rec_length/3 + start_y, screwhole))
            return dot
        elif side == "w" and location == "f": #width and front
            for i in range(1, 3, 1):          
                dot = svg.write('<circle cx = "{}" cy = "{}" r = "{}" ' \
                    'stroke-width="2" stroke="black" fill="black"/>\n'.format(i * rec_width/3 + start_x, -screwhole_edge + start_y + rec_length, screwhole))
            return dot
        else:
            return "define side"

 

    with open("pre.svg", "w") as svg:
        svg.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n') #xml version
        
        svg.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" ' \
            '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n') #doctype
        
        svg.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" ' \
            'width="1000%" height="1000%" viewbox="0 0 1000 1000" version="1.1">\n') #svg tag kms
        
        #base
        svg.write('<rect x="{}" y="{}" width="{}" height="{}" ' \
            'stroke-width="2" stroke="black" fill="none"/>\n'.format(start_x, start_y, rec_width, rec_length)) 
        
               


        #screw holes for base
        hole("w", "f")
        hole("w", "b")
        hole("l", "r")
        hole("l", "l")



        # if len(initials) != 0:
        #     svg.write('<text x="{}" y="{}" font-size="{}" dominant-baseline="central" ' \
        #         'text-anchor="middle"> {} </text>\n'.format(100 + (square_dim/2), 
        #         100 + (square_dim/2), square_dim / 96 * 32, initials))

        svg.write('</svg>') #svg end tag
    
    print("pre.svg has been created.")

if __name__=="__main__":
    main()