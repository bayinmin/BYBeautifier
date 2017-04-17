import json

def beautify_json(input_json, k_indent=4, k_sort_keys=True):
    beautified_string = json.dumps(input_json, sort_keys=True, indent=k_indent)
    return beautified_string