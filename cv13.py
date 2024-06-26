import cv2

def display_clicked_points(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Create a window to display the image
    cv2.namedWindow('Image')

    # Define a callback function to handle mouse clicks
    def click_event(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Clicked at ({x}, {y})")

    # Set the callback function for the window
    cv2.setMouseCallback('Image', click_event)

    # Display the image
    cv2.imshow('Image', image)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()

# Example usage
display_clicked_points("C:/Users/thimm/OneDrive/Pictures/WhatsA.jpg")
