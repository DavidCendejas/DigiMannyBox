def inputWidth():
    input_width = 0
    while input_width < 0.1 or input_width > 2:
        input_width = float(input("Input a width (0.1-2 in): "))
    return input_width

def inputHeight():
    input_height = 0
    while input_height < 0.1 or input_height > 2:
        input_height = float(input("Input a height (0.1-2 in): "))
    return input_height

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
    
    square_dim = 96 * inputWidth() # (96 pixels to an inch) * inches
    initials = inputInitials()

    '''
    REMOVE ABOVE WHEN DOING RECTANGLES AND NOT JUST SQUARE
    rec_width = inputWidth() 
    rec_height = inputHeight() 
    '''
    

    with open("pre.svg", "w") as svg:
        svg.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n') #xml version
        
        svg.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" ' \
            '"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n') #doctype
        
        svg.write('<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" ' \
            'width="1000%" height="1000%" viewbox="0 0 1000 1000" version="1.1">\n') #svg tag kms
        
        svg.write('<rect x="100" y="100" width="{}" height="{}" ' \
            'stroke-width="2" stroke="black" fill="none"/>\n'.format(square_dim, square_dim)) #square
        
        if len(initials) != 0:
            svg.write('<text x="{}" y="{}" font-size="{}" dominant-baseline="central" ' \
                'text-anchor="middle"> {} </text>\n'.format(100 + (square_dim/2), 
                100 + (square_dim/2), square_dim / 96 * 32, initials))

        svg.write('</svg>') #svg end tag
    
    print("pre.svg has been created.")

if __name__=="__main__":
    main()