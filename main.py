# -*- coding: UTF-8 -*-
from pdf2image import convert_from_path
import tempfile
from printimg import print_img
import os
import traceback
from optparse import OptionParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')


# 添加poppler环境变量
os.environ["PATH"] += os.pathsep + os.getcwd() + '/poppler-0.68.0/bin/'
# print (os.getcwd() + '/poppler-0.68.0/bin/')


# 打印pdf
def print_pdf(filenames, printer):
    filename_list = filenames.split(',')
    for filename in filename_list:
        images = convert_from_path(filename)
        img_paths = []
        tmp_dir = tempfile.mkdtemp()
        for index, img in enumerate(images):
            img_path = tmp_dir + '\\%s.png' % (index)
            img_paths.append(img_path)
            img.save(img_path)
        print_img(os.path.basename(filename), img_paths, printer)


if __name__ == '__main__':
    # filename = 'D:/开户照片/1/单位保证金账户开户通知书.pdf,D:/开户照片/1/单位保证金账户开户通知书.pdf'.decode("utf-8").encode("gbk")
    # printer = 'Microsoft Print to PDF'
    # print_pdf(filename, printer)
    
    try:
        parser = OptionParser()
        parser.add_option("-f", "--file",
                          action="store", dest="file", default=None,
                          help="pdf file path")

        parser.add_option("-p", "--printer",
                          action="store", dest="printer", default=None,
                          help="printer name")

        (options, args) = parser.parse_args()
        filename = options.file
        printer = options.printer
        # print filename
        # print printer
        if filename is None:
            parser.print_help()
            sys.exit(0)
        print_pdf(filename, printer)
    except Exception as expt:
        print traceback.format_exc()
        print expt
