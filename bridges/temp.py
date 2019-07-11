import webcolors

colors = webcolors.CSS3_HEX_TO_NAMES
color_names = []

for key, value in colors.items():
    color_names.append(value)
print (color_names)
