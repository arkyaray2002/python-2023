def remove_item(li, item):
    return [x for x in li if x != item]

def check_common(li1, li2):
    return True if len(set(li1) & set(li2)) > 0 else False
