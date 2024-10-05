from barcode import EAN13
from barcode.writer import ImageWriter
num = '5901234123457'
obj = EAN13(num, writer=ImageWriter())
obj.save("name")

