
from skimage import img_as_float

def draw_H(image, coords, color=(0, 255, 0)):
    # makes a copy of the image
    out = image.copy()
    
    # Defines the size of the letter H
    canvas = out[coords[0]:coords[0] + 24,
                 coords[1]:coords[1] + 20]
    
    # sets the color
    canvas[:, :3] = color
    canvas[:, -3:] = color
    canvas[11:14] = color
    
    return out
