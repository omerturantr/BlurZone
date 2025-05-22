import cv2
import tkinter as tk

# Global variables
drawing = False
ix, iy = -1, -1
rectangles = []
undo_stack = []
redo_stack = []
img_display = None
original_img = None
temp_img = None
change_count = 0  # 👈 Yeni: değişiklik sayacı

def draw_change_count(image):
    text = f"Changes: {change_count}"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.8
    color = (0, 255, 0)
    thickness = 2
    text_size, _ = cv2.getTextSize(text, font, font_scale, thickness)
    x = image.shape[1] - text_size[0] - 15
    y = 30
    cv2.putText(image, text, (x, y), font, font_scale, color, thickness)

def mouse_callback(event, x, y, flags, param):
    global ix, iy, drawing, img_display, temp_img, undo_stack, redo_stack, original_img, change_count

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        temp_img = img_display.copy()
        cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 255, 0), 1)
        draw_change_count(temp_img)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        fx, fy = min(ix, x), min(iy, y)
        tx, ty = max(ix, x), max(iy, y)

        if (tx - fx) > 0 and (ty - fy) > 0:
            ratio_x = original_img.shape[1] / img_display.shape[1]
            ratio_y = original_img.shape[0] / img_display.shape[0]
            x1, y1 = int(fx * ratio_x), int(fy * ratio_y)
            x2, y2 = int(tx * ratio_x), int(ty * ratio_y)

            blurred = original_img.copy()
            roi = blurred[y1:y2, x1:x2]
            roi_blurred = cv2.GaussianBlur(roi, (13, 13), 0)
            blurred[y1:y2, x1:x2] = roi_blurred

            undo_stack.append(original_img.copy())
            redo_stack.clear()
            original_img[:] = blurred
            change_count += 1  # 👈 Artır değişiklik sayısı

def blur_with_change_counter(img_path):
    global img_display, original_img, temp_img, undo_stack, redo_stack, change_count

    original_img = cv2.imread(img_path)
    if original_img is None:
        raise ValueError("Görüntü yüklenemedi: " + img_path)

    undo_stack = [original_img.copy()]
    redo_stack = []
    change_count = 0

    window_name = "Image - ESC: Exit | Ctrl+Z: Undo | Ctrl+Y: Redo"

    # Ekran boyutunu al
    root = tk.Tk()
    root.withdraw()
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    root.destroy()

    window_w, window_h = 900, 700
    x_pos = (screen_w - window_w) // 2
    y_pos = int(screen_h * 0.15)

    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, window_w, window_h)
    cv2.moveWindow(window_name, x_pos, y_pos)
    cv2.setMouseCallback(window_name, mouse_callback)

    print("🖱 Blur seç, değişiklik sayısı sağ üstte görünür. ESC: çık, Ctrl+Z/Y: geri/ileri.")

    while True:
        try:
            _, _, win_w, win_h = cv2.getWindowImageRect(window_name)
            if win_w > 0 and win_h > 0:
                img_display = cv2.resize(original_img, (win_w, win_h))
        except cv2.error:
            break  # pencere kapandıysa sessiz çık

        # Sayaç göster
        show_img = temp_img.copy() if drawing and temp_img is not None else img_display.copy()
        draw_change_count(show_img)
        cv2.imshow(window_name, show_img)

        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break
        elif key == 26:  # Ctrl+Z
            if len(undo_stack) > 1:
                redo_stack.append(undo_stack.pop())
                original_img[:] = undo_stack[-1].copy()
                change_count = max(0, change_count - 1)
                print("↩️ Undo")
        elif key == 25:  # Ctrl+Y
            if redo_stack:
                redo_img = redo_stack.pop()
                undo_stack.append(redo_img.copy())
                original_img[:] = redo_img.copy()
                change_count += 1
                print("↪️ Redo")

    cv2.destroyAllWindows()

# Çalıştır
blur_with_change_counter("Elderly Man.jpg")  # Görsel yolunu değiştir
