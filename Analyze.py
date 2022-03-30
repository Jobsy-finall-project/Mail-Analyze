import json
import re


def analyze(new_mail):
    print(new_mail)
    mail_words = count_mail_words(new_mail)
    print(mail_words)
    accepted_model = json.load(open("accepted_model.json", mode="r"))
    accepted_score = compere_to_model(accepted_model, mail_words)
    rejected_model = json.load(open("rejected_model.json", mode="r"))
    rejected_score = compere_to_model(rejected_model, mail_words)

    print(f"accepted score: {accepted_score}")
    print(f"rejected score: {rejected_score}")
    return {
        "accepted_score": accepted_score,
        "rejected_score": rejected_score
    }


def compere_to_model(model: dict, mail: dict):
    score = 0
    for key in model:
        if key in mail:
            score += model[key]
    return score


def count_mail_words(mail):
    words_in_file = {}
    for word in mail.strip().split(" "):
        curr_word = re.sub("[.?!,]", "", word).strip().lower()

        if curr_word in words_in_file:
            words_in_file[curr_word] += 1
        else:
            words_in_file[curr_word] = 1
    return words_in_file
