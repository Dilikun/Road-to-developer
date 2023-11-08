# from stegano import lsb
#
# secret = lsb.hide('stegano/1.png',
#                   'Your password: qwerty')
# secret.save('stegano/1_secret.png')
#
# result = lsb.reveal('stegano/1_secret.png')
# print(result)

# from stegano import exifHeader
# secret = exifHeader.hide('stegano/2.jpg', 'stegano/2_secret.jpg', 'Жду не дождусь лицо того кто расшифровал это изоображение '
#                                                           'только для этого сосбщения')
# result = exifHeader.reveal('stegano/2_secret.jpg')
# result = result.decode()
# print(result)

from steganocryptopy.steganography import Steganography

Steganography.generate_key('')
secret = Steganography.encrypt('key.key', 'stegano/3.png', 'secret_message.txt')
secret.save('stegano/3_secret.png')

result = Steganography.decrypt('key.key', 'stegano/3_secret.png')
print(result)