<h1 align="center">🌀 BlurZone</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/5b7c50b7-e69c-4a5f-8769-1f6953e4cc48" width="100" alt="App Icon"/>
</p>

<p align="center">
  <b>Blur any part of an image with ease – just click, drag, and blur.</b><br>
  🖼️ Built with Python + OpenCV + Tkinter
</p>

<p align="center">
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/omerturantr/BlurZone?style=flat-square">
  <img alt="GitHub stars" src="https://img.shields.io/github/stars/omerturantr/BlurZone?style=flat-square">
  <img alt="License" src="https://img.shields.io/github/license/omerturantr/BlurZone?style=flat-square">
</p>

---

## ✨ Features

- 🖱️ Select rectangular area with mouse
- 💨 Apply instant Gaussian blur
- 🔁 Undo/Redo support with keyboard (Ctrl+Z / Ctrl+Y)
- 📐 Auto scaling and repositioning of window
- 🔢 Change count shown in top-right corner
- 🎯 Ideal for anonymizing faces or details in images

---

## 📷 Before / After Example

<table>
  <tr>
    <td align="center"><b>Before</b></td>
    <td align="center"><b>After</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/5bd3b8b1-fb01-4eeb-b730-fd77dfa0c375" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/9ceb996f-3e92-44fa-920a-2f49a87fe99c" width="300"></td>
  </tr>
</table>

> ℹ️ Make sure the above images exist in your repository under the `Pictures/` folder

---

## ⚙️ Installation

```bash
git clone https://github.com/omerturantr/BlurZone.git
cd BlurZone
pip install -r requirements.txt
python main.py
```

✅ Or run the portable `BlurZone.exe` directly.

---

## 🖱️ How to Use

1. Open an image (`Elderly Man.jpg` is included)
2. Click and drag to draw a rectangle
3. The selected area will be blurred
4. Use:
   - `ESC` → Exit
   - `Ctrl + Z` → Undo
   - `Ctrl + Y` → Redo

---

## 📁 Folder Structure

```
BlurZone/
├── main.py
├── Elderly Man.jpg
├── Pictures/
│   ├── Elderly_Original.jpg
│   └── Elderly_Blurred.jpg
├── blurzone.ico
├── dist/
└── README.md
```

---

## 👤 Developer

Made with by [@omerturantr](https://github.com/omerturantr)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
