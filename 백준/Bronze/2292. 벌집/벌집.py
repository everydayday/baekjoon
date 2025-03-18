N = int(input())
layer = 1
cells = 1

while N > cells:
    cells += 6 * layer
    layer += 1

print(layer)
