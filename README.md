# 🔵 BlurZone

🖼️ **BlurZone** is a simple desktop application to blur specific areas of an image using mouse selection, with support for undo/redo actions. Built using Python and OpenCV.

![BlurZone Logo](https://raw.githubusercontent.com/omerturantr/BlurZone/main/BlurZone%20Icon.ico)

---

## 🚀 Features

- 🎯 Select and blur any region with your mouse
- ↩️ Undo (Ctrl+Z) and Redo (Ctrl+Y) support
- 📷 Image scaling and live feedback with counter
- 🪄 Smooth UI experience with window positioning
- 🧠 Ideal for redacting or anonymizing parts of photos

---

## 🛠️ Installation

1. Clone the repository or download the ZIP:
```bash
git clone https://github.com/omerturantr/BlurZone.git
```

2. Navigate to the folder:
```bash
cd BlurZone
```

3. (Optional) Install dependencies if using the source code:
```bash
pip install opencv-python tk
```

4. Run the app:
```bash
python main.py
```

If you are using the `.exe`, just double-click `BlurZone.exe`

---

## 🖱️ Usage

- Use your **mouse** to select a rectangular area to blur.
- Hit **ESC** to exit the app.
- Use **Ctrl+Z** to undo, and **Ctrl+Y** to redo.
- Change count is displayed at the top right.

---

## 📁 Project Structure

```
BlurZone/
├── main.py             # Main Python app
├── Elderly Man.jpg     # Sample image
├── blurzone.ico        # Application icon
├── dist/               # Folder with executable
└── README.md           # This file
```

---

## 👨‍💻 Developer

Developed by [@omerturantr](https://github.com/omerturantr)

---

## 📄 License

This project is licensed under the MIT License.