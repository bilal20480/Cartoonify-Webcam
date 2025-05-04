import cv2

def cartoonize_image(img):
    # Resize for performance (optional)
    # img = cv2.resize(img, (640, 480))

    # Convert to gray and apply a light blur
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)

    # Edge detection
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, blockSize=7, C=2
    )

    # Bilateral filter with lower blur for sharper results
    color = cv2.bilateralFilter(img, d=5, sigmaColor=100, sigmaSpace=100)

    # Combine edges with color
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    cartoon_frame = cartoonize_image(frame)

    cv2.imshow('Live Cartoonized (Improved)', cartoon_frame)

    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

cap.release()
cv2.destroyAllWindows()
