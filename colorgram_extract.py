#Use colorgram to extract colors from the Hirst painting in  image.jpg
import colorgram
colors = colorgram.extract('image.jpg', 10)
list_colors = []
for colors in colors:
    r = colors.rgb[0]
    g = colors.rgb[1]
    b = colors.rgb[2]

    list_colors.append((r,g,b))

print(list_colors)
