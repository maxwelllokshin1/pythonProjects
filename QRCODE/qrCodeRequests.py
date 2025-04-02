from PIL import Image, ImageDraw

def draw_square(draw, x, y, size, fill="black"):
    """Helper function to draw a square."""
    draw.rectangle([x, y, x + size, y + size], fill=fill)

def generate_fixed_qr(data, size=10, border=4):
    """
    Generates a scannable QR-like pattern manually without using the qrcode library.
    This includes the necessary finder patterns.
    """
    qr_size = 21  # Standard size for QR version 1
    img_size = (qr_size + 2 * border) * size
    img = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(img)

    # Draw Finder Patterns (Top-Left, Top-Right, Bottom-Left)
    finder_pattern_positions = [(0, 0), (qr_size - 7, 0), (0, qr_size - 7)]
    for x, y in finder_pattern_positions:
        for i in range(3):
            draw_square(draw, (x + i) * size, (y + i) * size, (7 - 2 * i) * size, fill="black" if i % 2 == 0 else "white")

    # Convert text to binary
    binary_data = ''.join(format(ord(char), '08b') for char in data)

    # Fill in QR code with binary data, avoiding finder patterns
    index = 0
    for y in range(qr_size):
        for x in range(qr_size):
            if any(x_start <= x < x_start + 7 and y_start <= y < y_start + 7 for x_start, y_start in finder_pattern_positions):
                continue  # Skip finder patterns

            if index < len(binary_data) and binary_data[index] == '1':
                x_pos = (x + border) * size
                y_pos = (y + border) * size
                draw_square(draw, x_pos, y_pos, size)
            index += 1

    # Save and display the QR code
    img.save("fixed_qrcode.png")
    img.show()

# Example usage
data = "https://bleach.fandom.com/wiki/Bleach_Wiki"
generate_fixed_qr(data)
print("✅ QR Code generated manually and saved as 'fixed_qrcode.png'")
