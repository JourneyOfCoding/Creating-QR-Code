import qrcode  # Import the qrcode library to generate QR codes
from PIL import Image  # Import the PIL library for image manipulation
import qrcode.constants  # Import constants used for QR code configuration

# Define the data to be encoded in the QR code
data = "https://www.example.com"  # This will generate a QR code for the given URL

# Create a QRCode object with specific configuration
qr = qrcode.QRCode(
    version=1,  # Version 1 of the QR code (21x21 matrix)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
    box_size=10,  # Size of each box in the QR code
    border=4,  # Thickness of the border (4 boxes)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)  # Optimize the QR code to fit the data

# Create an image of the QR code
img = qr.make_image(fill='black', back_color='white')  # Black QR code on a white background

# Save the QR code image to a file
img.save("qrcode.png")

# Print a confirmation message
print("QR Code generated and saved as qrcode.png")

# Note: When you scan this qrcode.png file, it will redirect you to the URL 'https://www.example.com'
