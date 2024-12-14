def parser(response):
    parsed_data = {
        "Category": "NA",
        "Individual_category": "NA",
        "category_by_Gender": "NA",
        "colour": "NA",
        "MOVE_ON": "false",
        "FOLLOW_UP_MESSAGE": "NA"
    }

    current_key = None
    for line in response.split('\n'):
        line = line.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"')
            if key in parsed_data:
                parsed_data[key] = value
                current_key = key
        elif current_key:
            # If there's no colon, it's a continuation of the previous value
            parsed_data[current_key] += ' ' + line.strip('"')

    # Convert MOVE_ON to boolean
    parsed_data["MOVE_ON"] = parsed_data["MOVE_ON"].lower() == "true"

    return parsed_data