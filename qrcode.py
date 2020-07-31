import pyqrcode
import png
from pyqrcode import QRCode
QRstr = "www.google.com"
url = pyqrcode.create(QRstr)
url.png("myqr.png",scale=8)