# Importing Image from PIL package
import itertools
from operator import itemgetter
from PIL import Image
from scipy.spatial import KDTree
import webcolors
import threading

def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = webcolors.CSS3_HEX_TO_NAMES
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(webcolors.hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return names[index] #return f'closest match: {names[index]}'
 
# creating a image object
img = Image.open(r"C:\Users\milla\OneDrive\Koulu\Gradu\United States\E-commerce\walmart.com - edited.png")
pix = img.load()

final_colors = {}
color_groups = [
[0, "lightblue", "aliceblue", "aqua", "azure", "cyan", "lightcyan", "lightskyblue", "lightsteelblue", "paleturquoise", "powderblue", "skyblue", "ghostwhite", "lavender", "turquoise"],
[0, "blue", "cornflowerblue", "darkturquoise", "deepskyblue", "dodgerblue", "mediumblue", "mediumslateblue", "mediumturquoise", "royalblue", "slateblue", "steelblue"],
[0, "darkblue", "cadetblue", "darkcyan", "darkslateblue", "midnightblue", "navy"],
[0, "lightred", "indianred", "rosybrown", "snow", "tomato"],
[0, "red", "crimson"],
[0, "darkred", "firebrick", "maroon"],
[0, "lightyellow", "cornsilk", "ivory", "khaki", "lemonchiffon", "lightgoldenrodyellow", "moccasin", "navajowhite", "palegoldenrod"],
[0, "yellow", "gold"],
[0, "darkyellow", "darkgoldenrod", "darkkhaki", "goldenrod"],
[0, "lightgreen", "aquamarine", "greenyellow", "honeydew", "lawngreen", "lime", "mediumspringgreen", "mintcream", "palegreen", "springgreen", "yellowgreen"],
[0, "green", "chartreuse", "darkseagreen", "lightseagreen", "limegreen", "mediumaquamarine", "mediumseagreen", "seagreen"],
[0, "darkgreen", "darkolivegreen", "forestgreen", "olive", "olivedrab", "teal"],
[0, "black"],
[0, "gray", "grey", "darkgray", "darkgrey", "darkslategray", "darkslategrey", "dimgray", "dimgrey", "gainsboro", "lightgray", "lightgrey", "lightslategray", "lightslategrey", "silver", "slategray", "slategrey", "whitesmoke"],
[0, "white"],
[0, "lightbrown", "burlywood", "floralwhite", "linen", "oldlace", "papayawhip", "sandybrown", "tan", "wheat"],
[0, "brown", "chocolate", "peru", "saddlebrown", "sienna"],
[0, "beige", "antiquewhite", "bisque", "blanchedalmond"],
[0, "lightpurple", "mediumorchid", "mediumpurple", "orchid", "plum", "thistle"],
[0, "purple", "blueviolet", "darkorchid", "darkviolet", "indigo", "magenta", "mediumvioletred"],
[0, "darkpurple", "magenta"],
[0, "pinkorange", "coral", "darksalmon", "lightcoral", "lightsalmon", "salmon"],
[0, "lightorange", "peachpuff", "seashell"],
[0, "orange", "darkorange", "orangered"],
[0, "lightpink", "lavenderblush", "mistyrose", "violet"],
[0, "pink", "deeppink", "fuchsia", "hotpink", "palevioletred"]]

def check_color_group(color):
    for list in color_groups:
        for color in list:
            if color in list:
                list[0] += 1
            

def process_pixels(img, start_row, end_row):
    picture_colors = {}
    picture_pixels = 0
    global final_pixels
    global color_groups
    for y in range(start_row, end_row):
        for x in range(img.width):
            pixel = img.getpixel((x, y))
            # do something with the pixel value
            if (len(pixel) == 4):
                if (pixel[3] == 0):
                    continue
                else:
                    r = pixel[0]
                    g = pixel[1]
                    b = pixel[2]
                    pixel = (r, g, b)
                    color = convert_rgb_to_names((r,g,b))
                    if (color in picture_colors) == True:
                        picture_colors[color] = picture_colors[color] + 1
                        picture_pixels += 1
                        final_pixels +=  1
                        continue
                    else:
                        picture_colors.update({color : 1})
                        picture_pixels += 1
                        final_pixels += 1
                        continue
            else:
                r = pixel[0]
                g = pixel[1]
                b = pixel[2]
                pixel = (r, g, b)
                color = convert_rgb_to_names((r,g,b))
                if (color in picture_colors) == True:
                    picture_colors[color] = picture_colors[color] + 1
                    picture_pixels += 1
                    final_pixels += 1
                    continue
                else:
                    picture_colors.update({color : 1})
                    picture_pixels += 1
                    final_pixels += 1
                    continue
    for color in picture_colors:
        if (color in final_colors) == True:
            final_colors[color] = final_colors.get(color) + picture_colors.get(color)
            continue
        else:
            final_colors[color] = picture_colors.get(color)
            continue

final_pixels = 0
threads = []
num_threads = 8
rows_per_thread = img.height // num_threads
for i in range(num_threads):
    start_row = i * rows_per_thread
    end_row = (i + 1) * rows_per_thread
    if i == num_threads - 1:
        end_row = img.height
    thread = threading.Thread(target=process_pixels, args=(img, start_row, end_row))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

sorted_final_colors = sorted(final_colors.items(), key=lambda x:x[1], reverse=True)
sorted_final = dict(sorted_final_colors)
pixels = img.size[0] * img.size[1]


for key in sorted_final:
    for list in color_groups:
        if key in list:
            list[0] += sorted_final[key]

sorted_color_groups = (sorted(color_groups, key=itemgetter(0), reverse=True))

for list in sorted_color_groups:
    percent_of_color_group = round(((list[0])/final_pixels)*100, 2)
    if percent_of_color_group == 0.0:
        continue
    else:
        print(list[1] + ": " + str(percent_of_color_group) + " %")
        continue


print("pixels of side x side: " + str(pixels))
print("amount of non-transparent pixels: " + str(final_pixels))
print("last print of final_colors: " + str(sorted_final))