# Q5. Create a 2-D Array of three rows and four columns, named ucs420_<your_name>>
# with following values – 10, 20, 30, 40, 50, 60, 70, 80, 90, 15, 20, 35. 

import numpy as np

ucs420_yourname = np.array([
    [10, 20, 30, 40], 
    [50, 60, 70, 80], 
    [90, 15, 20, 35]
])
print(f"Original 2D Array (ucs420_yourname):\n{ucs420_yourname}\n")

# Compute the mean,median, max, min, unique elements. 

print(f"Mean of array: {np.mean(ucs420_yourname)}\n")
print(f"Median of array: {np.median(ucs420_yourname)}\n")
print(f"Maximum value: {np.max(ucs420_yourname)}\n")
print(f"Minimum value: {np.min(ucs420_yourname)}\n")
print(f"Unique elements in the array: {np.unique(ucs420_yourname)}\n")

# Reshape the array to four rows and three columns and name it as reshaped_ ucs420_<your_name>>. 

reshaped_ucs420_yourname = ucs420_yourname.reshape(4, 3)
print(f"Reshaped Array (4x3):\n{reshaped_ucs420_yourname}\n")

# Resize the array to two rows and three columns and name it as resized_ ucs420_<your_name>>.

resized_ucs420_yourname = np.resize(ucs420_yourname, (2, 3))
print(f"Resized Array (2x3):\n{resized_ucs420_yourname}\n")