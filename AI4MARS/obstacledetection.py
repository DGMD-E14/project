# -*- coding: utf-8 -*-
"""obstacleDetection.ipynb
### Import Required Libraries
"""

# Install and import necessary libraries
!pip install opencv-python-headless
from google.colab import drive
drive.mount('/content/drive')

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

"""### Define Dataset Paths and Classes"""

# Define paths to AI4MARS dataset
dataset_path = '/content/drive/MyDrive/AI4MARS/msl/'
images_path = os.path.join(dataset_path, 'images', 'edr')  # Raw Mars images
labels_path = os.path.join(dataset_path, 'labels', 'train')  # Crowdsourced training labels

# Define terrain classes from dataset info
class_colors = {
    0: (0, 0, 0),       # Soil
    1: (255, 255, 255), # Bedrock
    2: (128, 128, 128), # Sand
    3: (255, 0, 0),     # Big Rock
    255: (0, 0, 0)      # NULL
}
class_names = {
    0: "Soil",
    1: "Bedrock",
    2: "Sand",
    3: "Big Rock",
    255: "Unlabeled"
}

"""### Load Dataset Files"""

# List images and labels
image_files = sorted([f for f in os.listdir(images_path) if f.endswith(('.jpg', '.png'))])
label_files = sorted([f for f in os.listdir(labels_path) if f.endswith('.png')])

# Ensure matching file counts
assert len(image_files) == len(label_files), "Mismatch between image and label files!"

print(f"Found {len(image_files)} images and {len(label_files)} labels in the dataset.")

"""### Visualization Functions"""

def visualize_terrain(image, label):
    # Create a segmentation overlay
    overlay = np.zeros_like(image, dtype=np.uint8)
    for class_id, color in class_colors.items():
        overlay[label == class_id] = color

    # Blend overlay with the original image
    blended = cv2.addWeighted(image, 0.7, overlay, 0.3, 0)

    # Plot results
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(label, cmap="tab10")
    plt.title("Segmentation Mask")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))
    plt.title("Blended Overlay")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

"""### Analyze Obstacles"""

def analyze_obstacles(image, label, obstacle_classes):
    # Identify obstacle regions from the label map
    obstacle_mask = np.isin(label, obstacle_classes).astype('uint8')

    # Find contours of the obstacle regions
    contours, _ = cv2.findContours(obstacle_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by minimum area
    min_area = 200
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_area]

    # Draw filtered contours on the original image
    filtered_image = image.copy()
    cv2.drawContours(filtered_image, filtered_contours, -1, (255, 0, 0), 2)  # Red for obstacles

    # Display results
    plt.figure(figsize=(12, 6))
    plt.imshow(cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB))
    plt.title("Filtered Obstacles")
    plt.axis("off")
    plt.show()

"""### Process Dataset"""

# Process images and labels
for image_file, label_file in zip(image_files, label_files):
    # Load image and corresponding label
    image = cv2.imread(os.path.join(images_path, image_file))
    label = cv2.imread(os.path.join(labels_path, label_file), cv2.IMREAD_GRAYSCALE)

    # Ensure both image and label are loaded
    if image is None or label is None:
        print(f"Failed to load {image_file} or {label_file}. Skipping...")
        continue

    print(f"Processing {image_file} with {label_file}...")

    # Visualize terrain classification
    visualize_terrain(image, label)

    # Analyze obstacles (e.g., sand and big rocks are obstacles)
    analyze_obstacles(image, label, obstacle_classes=[2, 3])

    # Process only a few images for testing (optional)
    if image_files.index(image_file) >= 2:
        break