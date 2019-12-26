def dirReduc(arr):
    final_coord = []
    coordinates = {}
    coordinates["x"] = arr.count("EAST") - arr.count("WEST")
    coordinates["y"] = arr.count("NORTH") - arr.count("SOUTH")
    if coordinates["x"] == 0 and coordinates["y"] == 0:
        return final_coord
    # or just remove pairs of EAST/WEST, NORTH/SOUTH
    if coordinates["x"] < 0:
        final_coord.extend(["WEST" for i in range(abs(coordinates["x"]))])
    else:
        final_coord.extend(["EAST" for i in range(abs(coordinates["x"]))])
    if coordinates["y"] < 0:
        final_coord.extend(["SOUTH" for i in range(abs(coordinates["y"]))])
    else:
        final_coord.extend(["NORTH" for i in range(abs(coordinates["y"]))])

    return final_coord


raw_dir = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
reduced_dir = dirReduc(raw_dir)
print(reduced_dir)