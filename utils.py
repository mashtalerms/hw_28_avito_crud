import csv
import json

from my_project.settings import PATH_FOR_UTILS_CONVERTERS


def csv_to_json_for_ads() -> None:

    """Open csv"""
    with open(PATH_FOR_UTILS_CONVERTERS['CSV_PATH_FOR_ADS'], encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        result = []

        """Change csv file"""
        for row in csv_reader:

            to_add = {"model": PATH_FOR_UTILS_CONVERTERS["MODEL_FOR_ADS"], "pk": int(row['Id'])}
            del row['Id']
            if row['is_published'] == "TRUE":
                row['is_published'] = True
            else:
                row['is_published'] = False
            row['price'] = int(row['price'])
            to_add['fields'] = row

            result.append(to_add)

    """Write in json"""
    with open(PATH_FOR_UTILS_CONVERTERS['JSON_PATH_FOR_ADS'], 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(result, indent=4, ensure_ascii=False))


def csv_to_json_for_categories() -> None:

    """Open csv"""
    with open(PATH_FOR_UTILS_CONVERTERS["CSV_PATH_FOR_CAT"], encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        result = []

        """Change csv file"""
        for row in csv_reader:

            to_add = {"model": PATH_FOR_UTILS_CONVERTERS["MODEL_FOR_CAT"], "pk": int(row['id'])}
            del row['id']
            to_add['fields'] = row

            result.append(to_add)

    """Write in json"""
    with open(PATH_FOR_UTILS_CONVERTERS["JSON_PATH_FOR_CAT"], 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(result, indent=4, ensure_ascii=False))


def csv_to_json_for_location() -> None:

    """Open csv"""
    with open(PATH_FOR_UTILS_CONVERTERS["CSV_PATH_FOR_LOCATION"], encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        result = []

        """Change csv file"""
        for row in csv_reader:

            to_add = {"model": PATH_FOR_UTILS_CONVERTERS["MODEL_FOR_LOCATION"], "pk": int(row['id'])}
            del row['id']
            to_add['fields'] = row

            result.append(to_add)

    """Write in json"""
    with open(PATH_FOR_UTILS_CONVERTERS["JSON_PATH_FOR_LOCATION"], 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(result, indent=4, ensure_ascii=False))


def csv_to_json_for_user() -> None:

    """Open csv"""
    with open(PATH_FOR_UTILS_CONVERTERS["CSV_PATH_FOR_USER"], encoding='utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
        result = []

        """Change csv file"""
        for row in csv_reader:

            to_add = {"model": PATH_FOR_UTILS_CONVERTERS["MODEL_FOR_USER"], "pk": int(row['id'])}
            del row['id']
            to_add['fields'] = row

            result.append(to_add)

    """Write in json"""
    with open(PATH_FOR_UTILS_CONVERTERS["JSON_PATH_FOR_USER"], 'w', encoding='utf-8') as json_file_handler:
        json_file_handler.write(json.dumps(result, indent=4, ensure_ascii=False))

if __name__=="__main__":
    csv_to_json_for_ads()
    csv_to_json_for_categories()
    csv_to_json_for_location()
    csv_to_json_for_user()
