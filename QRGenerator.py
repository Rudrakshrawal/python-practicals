# pip install pyqrcode pillow
# pip install pypng





import pyqrcode
from PIL import Image

# Get the link from the user
link = input("Enter your link: ")

# Create the QR code
qr = pyqrcode.create(link)

# Save the QR code as a PNG file
qr.png("QRCode.png", scale=5)

# Open the QR code image
img = Image.open("QRCode.png")
img.show()
