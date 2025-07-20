# Now generate the actual QR code
import qrcode
from PIL import Image

# Create QR code for LMS
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.tcs.com/careers')
qr.make(fit=True)

# Create and save QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save('lms_qr.png')

print("✅ Created lms_qr.png (actual QR code)")