from pdf2image import convert_from_path
from pytesseract import image_to_string
import sys

def convert_pdf_to_img(pdf_file):
    """
    @desc: this function converts a PDF into Image
    
    @params:
        - pdf_file: the file to be converted
    
    @returns:
        - an interable containing image format of all the pages of the PDF
    """
    return convert_from_path(pdf_file)


def convert_image_to_text(file):
    """
    @desc: this function extracts text from image
    
    @params:
        - file: the image file to extract the content
    
    @returns:
        - the textual content of single image
    """

    custom_config = sys.argv[3]+' '+sys.argv[4]
    text = image_to_string(file,config=custom_config)
    return text


def get_text_from_any_pdf(pdf_file):
    """
    @desc: this function is our final system combining the previous functions
    
    @params:
        - file: the original PDF File
    
    @returns:
        - the textual content of ALL the pages
    """
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    for pg, img in enumerate(images): 
        final_text += convert_image_to_text(img)
    out_put_file_path = sys.argv[2]# path of output txt file
    file = open(out_put_file_path,'w')
    file.writelines(final_text)
    file.close()
    return 'done'

path_to_pdf = sys.argv[1] # path of pdf
print(get_text_from_any_pdf(path_to_pdf))

