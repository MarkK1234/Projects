# QR code generator

import qrcode

# chooses the size and version of qrcode
features = qrcode.QRCode(version=1, box_size=40, border=3)

# adds the link for data when scanning
features.add_data('https://github.com/MarkK1234/Projects')
features.make(fit=True)
generate_image = features.make_image(fill_color="black",back_color='white')
# Saves the QR code as a png
generate_image.save('qrcode.png')