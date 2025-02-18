# %%
from colorama import Fore, Back

class RGB:

    main_colors = []
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    def to_list(self):
        return [self.r, self.g, self.b]

    def distance(self, other, bg_color=None) -> int:
        if bg_color:
            fg_effect = 0.3
            other_r = max(min(255, (other.r + bg_color.r)-(255*fg_effect)),0)
            other_g = max(min(255, (other.g + bg_color.g)-(255*fg_effect)),0)
            other_b = max(min(255, (other.b + bg_color.b)-(255*fg_effect)),0)
            #print(other_r, other_g, other_b)
        else:
            other_r = other.r
            other_g = other.g
            other_b = other.b
        return int(((self.r - other_r)**2 + (self.g - other_g)**2 + (self.b - other_b)**2)**0.5)

class Color:
    def __init__(self, fore, back, rgb):
        self.fore = fore
        self.back = back
        self.rgb = rgb

def get_cloosest_color(color: RGB) -> RGB:
    if type(color) is not RGB:
        raise ValueError("Color must be a RGB")
    bg_color = get_bg_color(color)
    fg_color = get_fg_color(color, bg_color.rgb)
    #return Color(fg_color.fore, bg_color.back, bg_color.rgb)
    #return Color(fg_color.fore, bg_color.back, fg_color.rgb)
    return Color(bg_color.fore, bg_color.back, RGB(0,0,0))


def get_bg_color(color: RGB):
    distances = []
    for c in RGB.main_colors:
        distances.append(color.distance(c.rgb))
    # print(distances)
    return RGB.main_colors[distances.index(min(distances))]

def get_fg_color(color: RGB, bg_color: RGB):
    distances = []
    for c in RGB.main_colors:
        distances.append(color.distance(c.rgb, bg_color))
    # print(distances)
    return RGB.main_colors[distances.index(min(distances))]

# class Colors:
#     colors = []


black = Color(Fore.BLACK, Back.BLACK, RGB(0,0,0))
white = Color(Fore.WHITE, Back.WHITE, RGB(255,255,255))
red = Color(Fore.RED, Back.RED, RGB(255, 0, 0))
green = Color(Fore.GREEN, Back.GREEN, RGB(0,255,0))
blue = Color(Fore.BLUE, Back.BLUE, RGB(0,0,255))
yellow = Color(Fore.YELLOW, Back.YELLOW, RGB(255,255,0))
cyan = Color(Fore.CYAN, Back.CYAN, RGB(0,255, 255))
magenta = Color(Fore.MAGENTA, Back.MAGENTA, RGB(255,0,255))

'''
black = RGB(0,0,0)
white = RGB(255,255,255)
red = RGB(255, 0, 0)
green = RGB(0,255,0)
blue = RGB(0,0,255)
yellow = RGB(255,255,0)
cyan = RGB(0,255, 255)
magenta = RGB(255,0,255)
'''

RGB.main_colors = [black, white, red, green, blue, yellow, cyan, magenta]

if __name__ == "__main__":
    c= RGB(254,255,255)
    col = get_cloosest_color(c)

# %%
