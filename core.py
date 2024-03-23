import json
import filesystem
# import db_handler
from discovery import domain
from configparser import ConfigParser

# from termcolor import colored

json_file = filesystem.get_json_filename()


def get_programs_unsorted(data=None) -> list:
    """
    Get all programs from set JSON targets file

    Returns empty list if exception is raised.

    :return: List of JSON objects
    """
    programs = []
    try:
        with open(json_file, 'r') as f:
            if not data:
                data = json.load(f)
            for i in data["program"]:
                programs.append(i)
            return programs
    except Exception as e:
        print(f"Error couldn't open JSON targets file {e}")
        return []


def get_programs_sorted(data=None):
    """
    Get all programs sorted by priority level from set JSON targets file

    Returns empty list if exception is raised.

    :return: List of JSON objects
    """
    programs = get_programs_unsorted(data) if data else get_programs_unsorted()
    if not programs:
        return []
    else:
        programs.sort(key=lambda x: x["priority"])
        return programs


def get_program_object(program: str, data) -> dict:
    """
    Get program JSON object information

    :return: JSON obj dictionary
    """
    programs = get_programs_sorted(data)
    for program_obj in programs:
        if program_obj["name"] == program:
            return program_obj
    return {}


def get_program_domains(program: str) -> list:
    """
    Get program JSON object information

    :return: list of domains
    """

    domains = []

    with open(json_file, 'r') as f:
        data = json.load(f)
        program_obj = get_program_object(program, data)
        for domain in program_obj['domains']:
            domains.append(domain)

    return domains


def add_program_domain(program: str, new_domain: str):

    with open(json_file, 'r') as f:
        data = json.load(f)

    program_obj = get_program_object(program, data)
    program_obj['domains'].append({'url': new_domain})

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)


def json_to_db_bulk():
    """
    Convert all JSON targets object to DB row
    :return:
    """

"""
db(program: str) -> dict:
    program = get_program_object(program)
    print(f"{program['name']}")
    db_handler.insert_domain(program['name'])
    print(f"{program['url']}")
    print(f"{program['expl_level']}")
    db_handler.insert_program(program['name'], get_program_domains("test"))
    print(f"{program['priority']}")
    print(f"{program['domains']}")
    return program
    """
