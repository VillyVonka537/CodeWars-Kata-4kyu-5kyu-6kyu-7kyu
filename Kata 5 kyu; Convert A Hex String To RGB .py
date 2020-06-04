# When working with color values it can sometimes be useful to extract 
# the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:

#     Accepts a case-insensitive hexadecimal color string as its 
#     parameter (ex. "#FF9933" or "#ff9933")
#     Returns an object with the structure {r: 255, g: 153, b: 51} 
#     where r, g, and b range from 0 through 255

# Note: your implementation does not need to support the shorthand form 
# of hexadecimal notation (ie "#FFF")
# Example

# "#FF9933" --> {r: 255, g: 153, b: 51}



def hex_string_to_RGB(hex_string): 
    hex_string = hex_string[1:]
    r = hex_string[0:2]
    g = hex_string[2:4]
    b = hex_string[4:6]
    
    return {'r':int(r, 16), 'g':int(g, 16), 'b':int(b, 16)}