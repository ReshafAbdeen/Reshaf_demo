#3D Arrays & Broadcasting (The Image Filter)

import numpy as np 
print("\033[2m === AI Computer Vision: Numpy Image Filter === \033[0m\n")

image_matrix = np.array([
    [[255, 0, 0], [0, 255, 0]],
    [[0,  0, 255], [255, 255, 0]]
])

print("---Original 3D Matrix---")
print(image_matrix)
print(f"Image shape : {image_matrix.shape}")

red_filter = np.array([1, 0, 0])

filtered_image = image_matrix * red_filter
print("\n-- Iamge After 'Red Filter' Applied")
print(filtered_image)