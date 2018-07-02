import pyqrcode

url = pyqrcode.create('https://github.com/kserjey')
url.svg('url.svg', scale=5, module_color="#BADA55")
