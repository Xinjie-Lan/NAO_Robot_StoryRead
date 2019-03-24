from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import re
import sys, os
sys.path.append('NAO CODE/')

def convert(fname,pages=None):
    
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = file(os.path.join(sys.path[0],fname), 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    #print text 

    # write Content to .txt
    text_file = open(os.path.join(sys.path[0],"output.txt"), "w")
    text = re.sub("\s\s+", " ", text)
    text_file.write("%s" % text)
    text_file.close()

convert("60744-whoop-goes-the-pufferfish.pdf",pages=[1,2,3,4,5,6,7,8,9,10,11])