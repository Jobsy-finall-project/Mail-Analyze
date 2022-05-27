import re

from repo import tag_repo


def analyze(new_cv):
    tag_pool = tag_repo.get_all()
    output_tags = __compere_to_model(tag_pool, new_cv)

    return output_tags


def __compere_to_model(model: list, cv: str):
    output = []
    cv = cv.strip().lower()
    cv_words = cv.split(" ")
    clean_cv = re.sub("[.?!,]", "", cv)
    for key in model:
        clean_key = key.strip().lower()
        if len(clean_key.split(" ")) > 1:
            if clean_key in clean_cv:
                output.append(key)
        elif clean_key in cv_words:
            output.append(key)
    return output
