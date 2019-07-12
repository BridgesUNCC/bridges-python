from bridges.bridges import *

bridges = Bridges(1, "", "")

bridges.window = [4, 5, 6, 7]
print(bridges.window)

try:
    bridges.window = 4
except TypeError:
    print("bridges window test passed")
else:
    print("Setter failed for bad type value")


bridges.set_visualize_JSON(True)
bridges.visualize()
