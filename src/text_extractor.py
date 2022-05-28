import base64
import os
from uuid import uuid4
import fitz
from docx2txt import docx2txt


def __extract_text_pdf(file_name: str):
    print("analyzing PDF")
    text = ""
    with fitz.open("tmpFiles/" + file_name) as doc:
        for page in doc:
            text += page.get_text()

    return text


def __extract_text_docx(file_name: str):
    print("analyzing DOCX")
    text = docx2txt.process("tmpFiles/" + file_name)
    return text


def __save_locally(data: str, file_name: str):
    print("analyzing something else")
    try:
        file_bytes = base64.b64encode(base64.b64decode(data))
    except Exception as e:
        print(e.args)
        file_bytes = ""

    if file_bytes != "" and not file_name.endswith("txt"):
        print("writing binary")
        with open("tmpFiles/" + file_name, "wb") as file_to_save:
            decoded_file = base64.decodebytes(file_bytes)
            file_to_save.write(decoded_file)
    else:
        print("writing text")
        with open("tmpFiles/" + file_name, "w") as file_to_save:
            file_to_save.write(data)


def __extract_text_else(file_name: str):
    with open("tmpFiles/" + file_name, "r") as file_to_read:
        text = file_to_read.read()
    return text


def extract_text(data: str, file_name: str):
    file_type = file_name.rsplit(".", 1)[-1].strip().lower()
    file_name = str(uuid4()) + "-" + file_name

    __save_locally(data, file_name)
    match file_type:
        case "pdf":
            res = __extract_text_pdf(file_name)
        case "docx":
            res = __extract_text_docx(file_name)
        case _:
            res = __extract_text_else(file_name)

    os.remove("tmpFiles/" + file_name)
    return res
