import json

def validate(fileName, plate):
    with open(fileName, 'r') as file:
        jsonFile = json.load(file)

    total_letters, total_numbers = 0, 0

    for ch in plate:
        if ch.isalpha():
            total_letters += 1

        if ch.isdigit():
            total_numbers += 1

    for key, val in jsonFile.items():
        if key == "length" and len(plate) != val:
            return False

        if key == "letters" and total_letters != val:
            return False

        if key == "numbers" and total_letters != val:
            return False

    return True