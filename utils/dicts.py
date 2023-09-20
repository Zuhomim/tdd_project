def get_val(collection, key, default='git'):
    """возвращает значение из словаря по ключу, если ключ существует, иначе возвращает default"""
    if collection.get(key) is None:
        return default
    return collection[key] if key else default
