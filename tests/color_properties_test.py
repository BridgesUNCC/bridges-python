from bridges.color import Color

my_color = Color()

my_color.red = 10
my_color.green = 100
my_color.blue = 255
my_color.alpha = 1.0

print(my_color.rgba)

other_color = Color()
other_color.rgba = 100, 0, 20, 0
print(my_color.rgba, other_color.rgba)

print(Color.red.__doc__)
