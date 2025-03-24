import qrcode #import the qrcode class

# Data to be encoded
data = "https://crumblcookies.com/"

# Create QR Code
qr = qrcode.QRCode(
    version=2,
    box_size=5,
    border=2
)
qr.add_data(data)
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill="black", back_color="white")
img.save("custom.png")

print("QR Code generated and saved as 'qrcode.png'")
