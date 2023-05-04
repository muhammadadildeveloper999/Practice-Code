import cv2

# Load the image
img = cv2.imread('image.jpeg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image to create a binary image
_, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Invert the binary image to create a mask for the grey regions
mask = cv2.bitwise_not(binary)

# Apply the mask to the original image to extract the grey regions
gray_regions = cv2.bitwise_and(img, img, mask=mask)

# Apply the binary image as a mask to the original image to extract the white regions
white_regions = cv2.bitwise_and(img, img, mask=binary)

# Display the white and grey regions
cv2.imshow('White Regions', white_regions)
cv2.imshow('Grey Regions', gray_regions)

# Save the white and grey regions
cv2.imwrite('white_regions.jpg', white_regions)
cv2.imwrite('gray_regions.jpg', gray_regions)

cv2.waitKey(0)
cv2.destroyAllWindows()
