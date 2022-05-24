import base64
import os

from PyPDF2 import PdfReader, PdfFileReader
from docx2txt import docx2txt


def __extract_text_pdf(data: str):
    # byte_pdf = base64.b64decode(data)
    # with open("tmp.pdf", "wb") as file_to_save:
    #     file_to_save.write(byte_pdf)
    # with open("tmp.pdf", "rb") as file_to_read:
    #     pdfReader = PdfFileReader(file_to_read)
    #     text = ''
    #     for i in range(0, pdfReader.numPages):
    #         # creating a page object
    #         pageObj = pdfReader.getPage(i)
    #         # extracting text from page
    #         text = text + pageObj.extractText()
    #     print(text)
    reader = PdfReader("tmp.pdf")
    text = ""
    for page in reader.pages:
        text += page.extract_text()
        text += "\n"
    print(text)
    return text


def __extract_text_docx(data: str):
    byte_pdf = base64.b64decode(data)
    with open("tmp.docx", "wb") as file_to_save:
        file_to_save.write(byte_pdf)
    text = docx2txt.process("tmp.docx")
    return text


def __save_locally(data: str, file_name: str):
    try:
        # file_bytes = data.encode("utf-8")
        file_bytes = base64.b64encode(base64.b64decode(data))
    except Exception:
        file_bytes = ""

    if file_bytes is not "":
        print("writing binary")
        with open(file_name, "wb") as file_to_save:
            decoded_file = base64.decodebytes(file_bytes)
            file_to_save.write(decoded_file)
    else:
        print("writing text")
        with open(file_name, "w") as file_to_save:
            file_to_save.write(data)


def __extract_text_else(file_name: str):
    with open(file_name, "r") as file_to_read:
        text = file_to_read.read()
    return text


def extract_text(data: str, file_name: str):
    file_type = file_name.rsplit(".", 1)[-1].strip().lower()
    if file_type == "pdf":
        res = __extract_text_pdf(data)
    elif file_type == "docx":
        res = __extract_text_docx(data)
    else:
        __save_locally(data, file_name)
        res = __extract_text_else(file_name)
        os.remove(file_name)
    return res
