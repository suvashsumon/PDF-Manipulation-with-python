import PyPDF2 
  
def merge(pdfs, output):  
    pdfMerger = PyPDF2.PdfFileMerger()
    
    for pdf in pdfs: 
        with open(pdf, 'rb') as f: 
            pdfMerger.append(f)
            
    with open(output, 'wb') as f: 
        pdfMerger.write(f) 
  
def main():  
    pdflist = ['first.pdf', 'second.pdf'] 
    marged  = 'marged.pdf'      
    merge(pdflist, marged) 
  
if __name__ == "__main__": 
    main() 