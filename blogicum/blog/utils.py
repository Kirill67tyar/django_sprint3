LENGTH_FOR_STR = 15


def output_for_model(field_value: str) -> str:
    if len(field_value) > LENGTH_FOR_STR:
        return field_value[:LENGTH_FOR_STR] + '...'
    return field_value
