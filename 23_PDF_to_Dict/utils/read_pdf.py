'''
    pdf_parser
'''

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

def read_pdf_to_text(pdf_file):

    password = ""
    extracted_text = ""

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
        # for lt_obj in layout:
        #     if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
        #         extracted_text += lt_obj.get_text()
        # -----------------------------------------

        # first page에서 line수가 15줄보다 적으면 cover로 생각하여 그 페이지는 넘어감
        if i == 0:
            i += 1
            for lt_obj in layout:
                if isinstance(lt_obj, LTTextBox):
                    first_page_text += lt_obj.get_text()

            if len(first_page_text.split('\n')) < 15:
                continue

        # 각 페이지당 첫번째 나오는 줄은 header로 인식하여 삭제
        header_tracker = True
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox):
                if header_tracker:
                    # 숫자이면 next line check
                    if lt_obj.get_text().strip().isdigit():
                        continue
                    else:
                        header_tracker = False
                        continue

                # quotation marks regex
                cleaned_line = quotes_cleaner(lt_obj.get_text())

                # Remove reference
                if cleaned_line.strip().replace(' ', '').upper() in ref_words:
                    # 목차 부분에서 break 방지
                    if i > 1:
                        end_read = True
                        break
                    else:
                        continue

                # check ref with special characters - compare only letters
                elif bool(re.search(r'(참고문헌|REFERENCE|REFERENCES)', cleaned_line.strip().replace(' ', '').upper())):
                    p = re.compile(r'(([가-힣A-Z])+)')
                    ref = p.search(cleaned_line.strip().replace(' ', '').upper())
                    if ref.group(1) in ref_words:
                        # 목차 부분에서 break 방지
                        if i > 1:
                            end_read = True
                            break
                        else:
                            continue

                # super-script 부분은 "다. 1)" 부분 중 숫자 제거해서 그냥 문장으로 인식하도록 수정
                cleaned_line = re.sub(re.compile(r'(다.\s{0,1})(\d\)\s{0,})'), r"\1 ", cleaned_line)

                # 1) 1. 이런식으로 나온 문장 숫자 제거하고 문장만 저장
                cleaned_line = re.sub(re.compile(r'(^\d\.|^\d{1,}\))\s{0,}([\D[ㄱ-ㅣ가-힣|a-zA-Z].*)'), r'\2', cleaned_line)

                # concat each line
                extracted_text += cleaned_line

        # page_num update
        i += 1

        # for outer loop exit
        if end_read:
            break

    #close the pdf file
    fp.close()

    return extracted_text.split('\n')