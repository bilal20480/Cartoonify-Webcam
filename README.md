# 🎨 Real-Time Cartoonizer with OpenCV

This project uses Python and OpenCV to turn your webcam feed into a **live cartoon-style video**, producing fun, stylized visuals similar to comic art or animated movies.

---

## 💡 How It Works

- Converts each video frame to **grayscale** and applies **median blur**.
- Performs **adaptive thresholding** to extract bold edges.
- Applies a **bilateral filter** to smooth colors while keeping edges sharp.
- Combines edge mask with the smoothed image for a cartoon effect.

---

## 🎬 Live Demo

> *(Insert a GIF or link to a video demo here)*

---

## 🛠️ Requirements

- Python 3.x
- OpenCV

### 🔧 Install Dependencies

```bash
pip install opencv-python
