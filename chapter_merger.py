from PyPDF2 import PdfFileMerger
import os
from utils import clear

def merge_pdfs(in_dir, out_file, max=0):
    '''
    params:
        in_dir<str>: the directory containing pdf files with a trailing /
        out_file<str>: the filename for the merged pdf
        max<int>: (optional) the total number of pdf files to be merged
    '''
    merger = PdfFileMerger()
    ctr=0
    pdfs = os.listdir(in_dir)

    for pdf in pdfs:
        if ctr == max and max > 0:
            break
        merger.append(in_dir+pdf)

        ctr+=1
        dot_ctr = '.' * round(10*ctr/len(pdfs))
        clear()
        print(f"working{dot_ctr}")

    merger.write(out_file)
    merger.close()
