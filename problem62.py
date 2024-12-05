# Create a list of cube numbers
# Aim is to find a same permutation there
# For every cube number, sort the digits in it to find its equivalence class
# Find a class with five members

cubes = [n*n*n for n in range(1,10000)]

classes = {}
for cube in cubes:
    cube_id = ''.join(sorted(str(cube)))
    classes[cube_id] = classes.setdefault(cube_id, []) + [cube]
best_class = max(classes.keys(), key=lambda k: len(classes[k]))
print("Best class:",best_class)
print("Class entries:", classes[best_class])