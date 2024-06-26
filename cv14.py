import cv2

def bgr_color_palette():
    # Function to handle trackbar events
    def on_trackbar_change(pos, user_data):
        # Retrieve current trackbar positions
        b = cv2.getTrackbarPos('Blue', 'BGR Color Palette')
        g = cv2.getTrackbarPos('Green', 'BGR Color Palette')
        r = cv2.getTrackbarPos('Red', 'BGR Color Palette')

        # Update the image with the selected BGR values
        img = user_data[0]
        img[:, :] = [b, g, r]

        # Display the updated image
        cv2.imshow('BGR Color Palette', img)

    # Create a black image window
    img = cv2.imread('blank_image.png')  # Provide a blank image of desired size and type
    cv2.namedWindow('BGR Color Palette')

    # Initialize BGR values and create trackbars
    initial_b, initial_g, initial_r = 0, 0, 0
    cv2.createTrackbar('Blue', 'BGR Color Palette', initial_b, 255, lambda pos, ud: on_trackbar_change(pos, ud))
    cv2.createTrackbar('Green', 'BGR Color Palette', initial_g, 255, lambda pos, ud: on_trackbar_change(pos, ud))
    cv2.createTrackbar('Red', 'BGR Color Palette', initial_r, 255, lambda pos, ud: on_trackbar_change(pos, ud))

    # Display the initial image
    cv2.imshow('BGR Color Palette', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
bgr_color_palette()
