from pdfminer.pdfparser import PDFParser  # fetches data from pdf file
from pdfminer.pdfdocument import PDFDocument  # stores data parsed by PDFParser
from pdfminer.pdfpage import PDFPage

# PDFPageInterpreter - processes page contents from PDFDocument
# PDFResourceManager - Stores shared resources such as fonts or images used by both PDFPageInterpreter and PDFDevice
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFTextExtractionNotAllowed

# LAParams - A layout analyzer returns a LTPage object for each page in the PDF document
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
# PDFPageAggregator - Extract the decive to page aggregator to get LT object elements
from pdfminer.converter import PDFPageAggregator

from utils.regex_functions import quotes_cleaner
import re
import logging


def read_pdf_to_text(pdf_file):

    password = ""
    extracted_text = ""

    # reset pdfminer logging level as ERROR
    logging.getLogger("pdfminer").setLevel(logging.ERROR)
    logging.getLogger("pdfminer.pdfparser").setLevel(logging.ERROR)
    logging.getLogger("pdfminer.layout").setLevel(logging.ERROR)

    # Open and read the pdf file in binary mode
    fp = open(pdf_file, "rb")

    # Create parser object to parse the pdf content
    parser = PDFParser(fp)

    # Store the parsed content in PDFDocument object
    document = PDFDocument(parser, password)

    # Check if document is extractable, if not abort
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed

    # Create PDFResourceManager object that stores shared resources such as fonts or images
    rsrcmgr = PDFResourceManager()

    # set parameters for analysis
    laparams = LAParams()

    # Create a PDFDevice object which translates interpreted information into desired format
    # Device needs to be connected to resource manager to store shared resources
    # device = PDFDevice(rsrcmgr)
    # Extract the decive to page aggregator to get LT object elements
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)

    # Create interpreter object to process page content from PDFDocument
    # Interpreter needs to be connected to resource manager for shared resources and device
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # header and reference handling -------------------
    i = 0
    first_page_text = ""
    end_read = False
    ref_words = ['참고문헌', 'REFERENCE', 'REFERENCES']
    # --------------------------------------------------

    # Ok now that we have everything to process a pdf document, lets process it page by page
    for page in PDFPage.create_pages(document):
        # As the interpreter processes the page stored in PDFDocument object
        interpreter.process_page(page)
        # The device renders the layout from interpreter
        layout = device.get_result()

        # ------ Original script -----------------
        # Out of the many LT objects within layout, we are interested in LTTextBox and LTTextLine
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()
        # -----------------------------------------


    #close the pdf file
    fp.close()

    return extracted_text.split('\n')