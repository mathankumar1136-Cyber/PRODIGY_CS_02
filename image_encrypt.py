from PIL import Image
import os

# =======================
# Encrypt Function
# =======================
def encrypt_image(image_path, key):
    if not os.path.isfile(image_path):
        print("❌ Error: File not found!")
        return

    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")  # Supports PNG with alpha
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b, a = pixels[i, j]

                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

                pixels[i, j] = (r, g, b, a)

        img.save("encrypted_image.png")
        print("✅ Image Encrypted Successfully!")

    except Exception as e:
        print("❌ Error during encryption:", e)


# =======================
# Decrypt Function
# =======================
def decrypt_image(image_path, key):
    if not os.path.isfile(image_path):
        print("❌ Error: File not found!")
        return

    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
        pixels = img.load()
        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b, a = pixels[i, j]

                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

                pixels[i, j] = (r, g, b, a)

        img.save("decrypted_image.png")
        print("✅ Image Decrypted Successfully!")

    except Exception as e:
        print("❌ Error during decryption:", e)


# =======================
# Main Program
# =======================
choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").strip().upper()

image_path = input(
    "Enter full image path (example: D:\\Internship\\Prodigy Infotech\\sample.png): "
).strip()

# Auto add extension if missing
if not image_path.lower().endswith(('.png', '.jpg', '.jpeg')):
    image_path += ".png"

# Safe key input
while True:
    try:
        key = int(input("Enter secret key (number): ").strip())
        break
    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

# Execute
if choice == 'E':
    encrypt_image(image_path, key)
elif choice == 'D':
    decrypt_image(image_path, key)
else:
    print("❌ Invalid Choice. Please type E or D.")
