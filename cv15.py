import cv2

def find_contour_coordinates(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Print coordinates of each contour
    for contour in contours:
        for point in contour:
            x, y = point[0]
            print(f"({x}, {y})")

    # Draw and display contours on the original image
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
find_contour_coordinates("C:/Users/thimm/OneDrive/Pictures/WhatsA.jpg")
