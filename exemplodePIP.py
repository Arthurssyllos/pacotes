
import qrcode

# criar um código QR

qr = qrcode.QRCode(version=1, box_size=10, border=5)  # definindo a versão, tamanho da caixa e definindo a borda

# adicionar dados ao código QE

data = 'https://www.google.com'  #adicionar o site que vai abrir
qr.add_data(data)
qr.make(fit=True)

# criar imagem do código QR

img = qr.make_image(fill_color='blue', back_color='cyan')

# salvar imagem em um arquivo

img.save("qr_code.png")