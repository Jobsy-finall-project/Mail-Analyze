import base64
import os

from PyPDF2 import PdfReader, PdfFileReader
from docx2txt import docx2txt
import fitz


def __extract_text_pdf(data: str):
    text = ""
    with fitz.open(data) as doc:
        for page in doc:
            text += page.get_text()

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
        __save_locally(data, file_name)
        res = __extract_text_pdf(file_name)
    elif file_type == "docx":
        res = __extract_text_docx(data)
    else:
        __save_locally(data, file_name)
        res = __extract_text_else(file_name)
        os.remove(file_name)
    return res
