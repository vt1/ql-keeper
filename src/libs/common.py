def delete_none_keys(dictionary):
    filtered = {k: v for k, v in dictionary.items() if v is not None}
    dictionary.clear()
    dictionary.update(filtered)
    return dictionary
