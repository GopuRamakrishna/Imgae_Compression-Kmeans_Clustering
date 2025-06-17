# 🎨 KMeans Image Compression App

A simple yet powerful Streamlit web app to compress images by reducing the number of unique colors using **KMeans clustering**. Great for learning unsupervised ML and practical image processing!

---

## 🚀 Features

- 📁 Upload any `.jpg`, `.jpeg`, or `.png` image
- 🎯 Choose up to **3 different K (color count)** values to compare
- 🔍 View **original** and **compressed images** side-by-side
- 💾 See **file sizes** and **compression ratios**
- 📥 Download compressed images directly from the app
- 🌙 **Dark mode** ready

---

## 🧠 How It Works

1. The image is converted into a 2D array of RGB pixel values.
2. KMeans clustering is applied to group similar colors into `K` clusters.
3. The image is reconstructed using the `K` cluster centroids.
4. The app displays and compares the original and compressed results.

---

## 🖥️ Tech Stack

- [Streamlit](https://streamlit.io/) – UI and interaction
- [scikit-learn](https://scikit-learn.org/) – KMeans clustering
- [Pillow](https://python-pillow.org/) – Image manipulation
- [NumPy](https://numpy.org/) – Array computations

---




