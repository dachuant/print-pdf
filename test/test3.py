from pdf2image import convert_from_path
import os

print os.getcwd()
os.environ["PATH"] += os.pathsep + 'D:/project/python/print/poppler-0.68.0/bin/'
print os.environ["PATH"] 

images = convert_from_path('D:\\project\\python\\print\\2.pdf')
for index, img in enumerate(images):
    img.save('D:\\project\\python\\print\\out\\%s.png' % (index))
