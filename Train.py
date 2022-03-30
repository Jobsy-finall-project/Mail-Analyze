from glob import glob
import json
import re


def train():
    print("training")
    files = load_folder(".\\trainingData")
    print(files)

    accepted_model = {}
    for curr_file in files["accepted"]:
        new_words = read_file(curr_file)
        accepted_model = merge_word_counts(accepted_model, new_words)
    print(accepted_model)

    rejected_model = {}
    for curr_file in files["rejected"]:
        new_words = read_file(curr_file)
        rejected_model = merge_word_counts(rejected_model, new_words)
    print(rejected_model)

    save_model(accepted_model, "accepted_model")
    save_model(rejected_model, "rejected_model")


def load_folder(folder_name) -> dict:
    folders = glob(f"{folder_name}/*")
    files = {
        "accepted": glob(f"{folders[0]}/*"),
        "rejected": glob(f"{folders[1]}/*")
    }
    return files


def read_file(file_to_read):
    words_in_file = {}
    with open(file_to_read, mode='r') as f:
        for line in f:
            stripped_line = line.strip().split(" ")
            if stripped_line == "":
                continue
            for word in line.strip().split(" "):
                curr_word = re.sub("[.?!,()*'\"]", "", word).strip().lower()
                if curr_word == "" or re.match("^\\w{2,5}://[\\w./=&?]+$", curr_word):
                    continue

                if curr_word in words_in_file:
                    words_in_file[curr_word] += 1
                else:
                    words_in_file[curr_word] = 1

    return words_in_file


def merge_word_counts(original: dict, new_dict: dict):
    output = {}
    for key in original:
        output[key] = original[key]
    for key in new_dict:
        if key in output:
            output[key] += new_dict[key]
        else:
            output[key] = new_dict[key]

    return output


def save_model(dict_to_save, file_name):
    json.dump(dict_to_save, open(file_name + ".json", "w"))
