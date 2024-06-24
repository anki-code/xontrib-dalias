import json
import ast

try:
    import demjson3
except:
    demjson3 = None

def load_as_dict(text):
    """Read `text` as json, javascript or python dict object."""
    dct = None
    text = text.strip()
    errors = []

    try:  # JSON
        dct = json.loads(text)
    except Exception as e:
        errors.append(f'JSON dict error: {e}. Line: {repr(text)}')

    if dct is None:
        try:  # Python dict
            dct = ast.literal_eval(text)
        except Exception as e:
            errors.append(f'Python dict error: {e}. Content: {repr(text)}')

    if dct is None and demjson3:
        try:  # JavaScript Object
            dct = demjson3.decode(text)
        except Exception as e:
            errors.append(f'JavaScript dict error: {e}. Content: {repr(text)}')

    return {"dict":dct, "errors":errors}

