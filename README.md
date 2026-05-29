# 👁️ OpenCV Computer Vision Masterclass

🚀 **A Premium, Step-by-Step Hands-On Repository to Master Computer Vision using Python & OpenCV.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.20+-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![PIL](https://img.shields.io/badge/Pillow-PIL-4D789B?style=for-the-badge)](https://python-pillow.github.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📖 Table of Contents
1. [Overview](#-overview)
2. [Key Features](#-key-features)
3. [Repository Directory Structure](#-repository-directory-structure)
4. [Deep Dive into Modules & Scripts](#-deep-dive-into-modules--scripts)
   * [1. Media I/O (Image, Video, Webcam)](#1-media-io-image-video-webcam)
   * [2. Geometry & Manipulation](#2-geometry--manipulation)
   * [3. Color Spaces & Conversions](#3-color-spaces--conversions)
   * [4. Thresholding & Binarization](#4-thresholding--binarization)
   * [5. Image Blurring & Smoothing](#5-image-blurring--smoothing)
   * [6. Edge & Morphological Operations](#6-edge--morphological-operations)
   * [7. Contour Detection](#7-contour-detection)
   * [8. Real-time HSV Color Detection Tracker](#8-real-time-hsv-color-detection-tracker)
5. [Installation & Setup](#-installation--setup)
6. [How to Run the Code](#%EF%B8%8F-how-to-run-the-code)
7. [Mathematical & Conceptual Deep Dives](#-mathematical--conceptual-deep-dives)
8. [License](#-license)

---

## 🌟 Overview

Welcome to the **OPENCV** repository! This is a meticulously curated, highly readable collection of modular scripts designed to take you from a complete beginner to a seasoned practitioner of **Computer Vision (CV)**. 

Rather than overloading you with abstract theory, this codebase walks you through core image processing concepts, geometric transformations, filtering math, and structural analysis, building up to real-time object tracking using webcams.

---

## ⚡ Key Features

* 📸 **Core Media Streaming:** Read, write, scale, and render images, static video files, and real-time live webcam feeds.
* 📐 **Spatial & Geometric Operations:** Precise resizing and regional cropping using efficient NumPy matrix slicing.
* 🎨 **Color Representation:** Deep insights into how color spaces (BGR, RGB, HSV, Grayscale) operate and convert.
* 🎛️ **Binarization & Thresholding:** Adaptive Gaussian thresholding vs. global binary thresholding to isolate features under varying lighting conditions.
* 🧼 **Noise Reduction Filters:** Normalized box blur, Gaussian blur, and Median filtering to suppress high-frequency noise.
* 📈 **Edge & Geometry Detection:** Canny edge detection matched with morphological dilation/erosion and shape drawings.
* 🎯 **Dynamic Object Tracking:** Real-time webcam color detector that calculates dynamic HSV bounding limits and tracks targets inside a bounding box.

---

## 📂 Repository Directory Structure

```directory
OPENCV/
├── C:\Users\Mian\Desktop\CV\
│   ├── blur.py                # Image blurring and noise reduction techniques
│   ├── colordetection.py      # Dynamic webcam color detection and tracker
│   ├── colorspace.py          # Color space transforms (BGR, RGB, HSV, Gray)
│   ├── contours.py            # Contour identification and rendering
│   ├── drawing.py             # Geometric shape and text annotations
│   ├── edge.py                # Canny edge detection & morphological operations
│   ├── img_resize_crop.py     # Image scaling and regional cropping operations
│   ├── io_img.py              # Read, write, and display static images
│   ├── io_vid.py              # Load and process video file streams
│   ├── io_web.py              # Establish and visualize live webcam feeds
│   ├── threshold.py           # Global and adaptive Gaussian thresholding
│   ├── README.md              # Beautiful project documentation (This file!)
│   └── images/                # Asset storage for images and videos
│       ├── Urban Environmental Intelligence Engine - Opera...mp4
│       ├── balloons_noisy.png
│       ├── birds.jpg
│       ├── board.jfif
│       ├── istockphoto-627966690-612x612.jpg
│       ├── note.png
│       └── pexels-roshan-kamath-793618-1661179.jpg
```

---

## 🔍 Deep Dive into Modules & Scripts

### 1. Media I/O (Image, Video, Webcam)
Foundation of all Computer Vision. Handling media pipelines correctly prevents latency and dropped frames.

* **[io_img.py](io_img.py)**
  * **Description:** Reads a source image, creates a copy in the `images/` directory, and shows it on screen.
  * **Key Functions:** `cv2.imread()`, `cv2.imwrite()`, `cv2.imshow()`, `cv2.waitKey()`.
* **[io_vid.py](io_vid.py)**
  * **Description:** Accesses video streams from disk (`images/Urban...mp4`) and renders frames with manual refresh pacing.
  * **Key Functions:** `cv2.VideoCapture()`, `video.read()`, `video.release()`.
* **[io_web.py](io_web.py)**
  * **Description:** Establishes a standard feed connecting to default webcam `0` and captures continuous video frames in a loop, terminating gracefully upon pressing the `q` key.
  * **Key Functions:** `cv2.VideoCapture(0)`.

---

### 2. Geometry & Manipulation
Spatial transformations are essential for deep learning preprocessing, augmentations, and region interest framing.

* **[img_resize_crop.py](img_resize_crop.py)**
  * **Description:** Demonstrates how to scale image dimensions and pull specific sections using fast NumPy multi-dimensional array slicing `img[y1:y2, x1:x2]`.
  * **Key Functions:** `img.shape`, `cv2.resize(img, (width, height))`.
* **[drawing.py](drawing.py)**
  * **Description:** Showcases basic canvas drawing. Renders circles, lines, rectangles, and overlays customized text labels on top of an image.
  * **Key Functions:** `cv2.line()`, `cv2.rectangle()`, `cv2.circle()`, `cv2.putText()`.

---

### 3. Color Spaces & Conversions
Computers view images as matrices. Understanding how color channels correspond determines success in isolating key features.

* **[colorspace.py](colorspace.py)**
  * **Description:** Converts default OpenCV **BGR** images to **RGB** (standard for matplotlib/web), **HSV** (standard for color detection), and **Grayscale** (standard for structural algorithms).
  * **Key Functions:** `cv2.cvtColor(img, cv2.COLOR_BGR2RGB)`, `cv2.COLOR_BGR2HSV`, `cv2.COLOR_BGR2GRAY`.

---

### 4. Thresholding & Binarization
Isolating foreground details from complex backgrounds by converting grayscale intensities into binary black-and-white.

* **[threshold.py](threshold.py)**
  * **Description:** Contrasts global binary thresholding (assigns a fixed value of `127` as threshold) with advanced Gaussian Adaptive Thresholding which computes regional thresholds dynamically to account for uneven shadows or bright spots.
  * **Key Functions:** `cv2.threshold()`, `cv2.adaptiveThreshold()`.

---

### 5. Image Blurring & Smoothing
Reduces noise, details, and unwanted textures. Frequently used as a precursor to edge detection to prevent false positives.

* **[blur.py](blur.py)**
  * **Description:** Highlights three distinct blurring filters: standard box blur, Gaussian blur (bell-curve weighted), and Median blur (superb for removing salt-and-pepper noise).
  * **Key Functions:** `cv2.blur()`, `cv2.GaussianBlur()`, `cv2.medianBlur()`.

---

### 6. Edge & Morphological Operations
Detecting structural discontinuities (boundaries) and refining them to fill gaps or eliminate tiny specks of noise.

* **[edge.py](edge.py)**
  * **Description:** Runs Canny edge detection, then uses morphological dilation to thicken borders (fill gaps) and erosion to shrink them back, showing how to isolate shape skeletons.
  * **Key Functions:** `cv2.Canny()`, `cv2.dilate()`, `cv2.erode()`.

---

### 7. Contour Detection
Contours are continuous curves representing boundary shapes. Vital for shape recognition, object classification, and size measurement.

* **[contours.py](contours.py)**
  * **Description:** Grayscales an image, applies a binary-inverse threshold to isolate birds against a bright sky, computes the outer contour boundaries, and draws them directly onto the source image with a bright green outline.
  * **Key Functions:** `cv2.findContours()`, `cv2.drawContours()`.

---

### 8. Real-time HSV Color Detection Tracker
This represents an advanced interactive utility highlighting the combination of multiple computer vision concepts in a real-time live application.

* **[colordetection.py](colordetection.py)**
  * **Description:** Reads webcam input, dynamically calculates HSV lower and upper bounds around a specific target color (configured to **Yellow** by default), masks the frame, identifies the non-zero pixel envelope (bounding box) using PIL, and tracks the physical object live on your screen.
  * **Key Functions:** `cv2.inRange()`, `PIL.Image.getbbox()`, `cv2.rectangle()`.

---

## ⚙️ Installation & Setup

Ensure you have **Python 3.8+** installed on your system. Follow these quick steps to get up and running:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/moosarehan/OPENCV.git
   cd OPENCV
   ```

2. **Create a Virtual Environment (Recommended):**
   * **Windows (PowerShell/CMD):**
     ```powershell
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install opencv-python numpy pillow
   ```

---

## ▶️ How to Run the Code

Simply invoke the specific python script you want to run using Python from the root folder. For example:

* **To run real-time HSV color tracking:**
  ```bash
  python colordetection.py
  ```

* **To see how thresholding behaves under varying lighting:**
  ```bash
  python threshold.py
  ```

* **To experiment with edge detection and dilation:**
  ```bash
  python edge.py
  ```

> 💡 *Note: For scripts that display images (e.g. `blur.py`, `edge.py`), click on the window and press **`Any Key`** or **`0`** to close them and exit.*
> 💡 *For webcam scripts (e.g. `colordetection.py`, `io_web.py`), press **`q`** on your keyboard to close the live stream.*

---

## 🧠 Mathematical & Conceptual Deep Dives

### A. Dynamic HSV Color Bounds
In `colordetection.py`, standard HSV bounding limits are calculated dynamically to catch colors in varying illumination:
```python
def bounds(color):
    c = np.uint8([[color]])
    hsv = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    hue = hsv[0][0][0]
    # Creates tolerance limits around Hue, Saturation, and Value
    lowerlimit = np.array([max(hue - 15, 0), 40, 40], dtype=np.uint8)
    upperlimit = np.array([min(hue + 15, 179), 255, 255], dtype=np.uint8)
    return lowerlimit, upperlimit
```
* **Hue Range ($\pm 15$):** Allows tracking color even when ambient lighting changes the tint slightly.
* **Saturation Floor ($40$):** Catches pastel or washed-out shades of the target color.
* **Value Floor ($40$):** Ensures the target can still be tracked in shadow or dim environments.

### B. Smoothing Kernels
* **Average Blur:** Computes the average pixel value under a kernel (e.g., $10 \times 10$). Highly destructive to edge structures.
* **Gaussian Blur:** Uses a 2D Gaussian distribution kernel. Reduces noise while preserving edge boundaries much better than average blur.
* **Median Blur:** Replaces the central pixel with the median of all pixels in the kernel window. Mathematically excellent at discarding absolute outliers like "Salt & Pepper" noise without degrading surrounding sharpness.

### C. Adaptive Gaussian Thresholding
Unlike global thresholding which applies a static pixel cut-off across the entire image, **Adaptive Gaussian Thresholding** computes the threshold for each individual pixel based on a Gaussian-weighted sum of its neighboring block (size $11 \times 11$). This enables text extraction from paper documents containing shadows and gradient lighting (e.g., in `threshold.py`).

---

## ⚖️ License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

⭐ *If you found this repository helpful, please consider giving it a star on GitHub!*

---

## 📬 Contact Me

Feel free to reach out for questions, collaboration, or support:
* **Email:** [moosarehan4@gmail.com](mailto:moosarehan4@gmail.com)

