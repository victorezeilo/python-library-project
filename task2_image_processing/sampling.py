import cv2
import matplotlib.pyplot as plt
import numpy as np
 
img = cv2.imread("flowers_color.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
original_height, original_width = img_rgb.shape[:2]
print(f"Original size: {original_width} x {original_height}")

# Divide width and height by 4
new_width  = original_width  // 4
new_height = original_height // 4
 
downsampled = cv2.resize(img_rgb, (new_width, new_height), interpolation=cv2.INTER_LINEAR)
print(f"Downsampled size: {new_width} x {new_height}")

# Upsample with Nearest Neighbor
upsampled_nearest = cv2.resize(downsampled, (original_width, original_height), interpolation=cv2.INTER_NEAREST)
print(f"Upsampled (Nearest Neighbor) size: {upsampled_nearest.shape[1]} x {upsampled_nearest.shape[0]}")
 
# Upsample with Cubic interpolation
upsampled_cubic = cv2.resize(downsampled, (original_width, original_height), interpolation=cv2.INTER_CUBIC)
print(f"Upsampled (Cubic) size: {upsampled_cubic.shape[1]} x {upsampled_cubic.shape[0]}")

fig, axes = plt.subplots(1, 4, figsize=(20, 5))
 
axes[0].imshow(img_rgb)
axes[0].set_title("Original")
axes[0].axis("off")
 
axes[1].imshow(downsampled)
axes[1].set_title("Downsampled (x4)")
axes[1].axis("off")

axes[2].imshow(upsampled_nearest)
axes[2].set_title("Upsampled - Nearest Neighbor")
axes[2].axis("off")
 
axes[3].imshow(upsampled_cubic)
axes[3].set_title("Upsampled - Cubic")
axes[3].axis("off")

plt.suptitle("Part 2 - Sampling and Quantization", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("part2_result.png", dpi=150, bbox_inches="tight")
plt.show()
 
print("Part 2 complete. Saved: part2_result.png")