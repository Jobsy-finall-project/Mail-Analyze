import json
import re


def analyze(new_mail):
    accepted_model = json.load(open("tag_pool.json", mode="r"))
    output_tags = __compere_to_model(accepted_model, new_mail)

    return output_tags


def __compere_to_model(model: list, mail: str):
    output = []
    mail = mail.strip().lower()
    mail_words = mail.split(" ")
    clean_mail = re.sub("[.?!,]", "", mail)
    for key in model:
        clean_key = key.strip().lower()
        if len(clean_key.split(" ")) > 1:
            if clean_key in clean_mail:
                output.append(key)
        elif clean_key in mail_words:
            output.append(key)
    return output


def count_mail_words(mail):
    words_in_file = {}
    for word in mail.strip().split(" "):
        curr_word = re.sub("[.?!,]", "", word).strip().lower()

        if curr_word in words_in_file:
            words_in_file[curr_word] += 1
        else:
            words_in_file[curr_word] = 1
    return words_in_file
