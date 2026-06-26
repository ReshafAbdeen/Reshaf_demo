import qrcode

data = "https://www.python.org"
filename = "python_qr.png"

print("--- QR Code Generator ---")
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(filename)
print(f"Success! Saved QR code to {filename}")