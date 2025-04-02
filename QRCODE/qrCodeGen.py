import qrcode #import the qrcode class

# Data to be encoded
data = "https://crumblcookies.com/" # website

# Create QR Code
qr = qrcode.QRCode(
    version=2, # small qrcode, bigger number holds more data
    box_size=5, # each black square is 5 pixels apart
    border=2 # empty space around the qr code
)

qr.add_data(data) # store the website link inside the qr code
qr.make(fit=True) # make sure that everything fits perfectly

# Create and save the image
img = qr.make_image(fill="black", back_color="white") # creates the image
img.save("custom.png") # save it as a png

print("QR Code generated and saved as 'qrcode.png'")
