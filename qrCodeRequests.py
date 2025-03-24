from PIL import Image, ImageDraw

def generate_simple_qr(data, size=10, border=4):
    """
    Generates a simple QR-like pattern manually without using qrcode library.
    """
    # Convert text to binary (simplified encoding)
    binary_data = ''.join(format(ord(char), '08b') for char in data)
    
    # Define QR code size (fixed 21x21 for simplicity)
    qr_size = 21  
    img_size = (qr_size + 2 * border) * size  
    img = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(img)

    # Simple pattern: fill in squares based on binary data
    index = 0
    for y in range(qr_size):
        for x in range(qr_size):
            if index < len(binary_data) and binary_data[index] == '1':
                x_pos = (x + border) * size
                y_pos = (y + border) * size
                draw.rectangle([x_pos, y_pos, x_pos + size, y_pos + size], fill="black")
            index += 1
    
    img.save("manual_qrcode.png")
    img.show()

# Example usage
data = "https://bleach.fandom.com/wiki/Bleach_Wiki"
generate_simple_qr(data)
print("QR Code generated manually and saved as 'manual_qrcode.png'")
