import qrcode

'''data = "Don't forget to have a great time today!" #fill this with any data you want the QR code to have

img = qrcode.make(data)

img.save('C:/Users/ambright/Documents/Python/myqrcode.png') #save the qr image to a specific folder in Windows, like this example
'''

#let's try another way to make the qr img more stylistic

data2 = "Don't just have a good day, have a great day!" #get it, Free Guy reference

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data2)

qr.make(fit=True)
img2 = qr.make_image(fill_color = 'blue', back_color = 'white')

img2.save('C:/Users/alexb/OneDrive/Documents/Python/myqrcode2.png')