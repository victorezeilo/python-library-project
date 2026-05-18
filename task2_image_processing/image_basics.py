import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("BL_Royal_Vincent_of_Beauvais.jpg")

# Convert to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# rows 5000 to 5600, columns 2400 to 4000
sub_image = img_rgb[5000:5600, 2400:4000]

height, width, planes = sub_image.shape
print(f"Sub-image height:  {height} pixels")
print(f"Sub-image width:   {width} pixels")
print(f"Number of planes:  {planes}")

plt.figure(figsize=(10, 6))
plt.imshow(sub_image)
plt.title("Victor Ezeilo - Module 2 - " + "2026-04-27")
plt.axis("off")
plt.tight_layout()
plt.savefig("part1_result.png", dpi=150, bbox_inches="tight")
plt.show()