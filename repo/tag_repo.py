import json


def add_tag(tag_to_add: str):
    print("adding new tag:", tag_to_add)
    pool = json.load(open("repo/tag_pool.json", mode="r"))
    tag_to_add = tag_to_add.strip().lower()
    if tag_to_add not in pool:
        pool.append(tag_to_add)
        with open("repo/tag_pool.json", mode="w") as file:
            json.dump(pool, file, indent=4)


def get_all():
    return json.load(open("repo/tag_pool.json", mode="r"))
