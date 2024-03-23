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

    :return: JSON object
    """
    programs = get_programs_sorted(data)
    for program_obj in programs:
        if program_obj["name"] == program:
            return program_obj
    return {}


def get_program_domains(program: str) -> list:
    """
    Get program JSON object dictionaries in domains array

    :return: List of domains belonging to a program
    """

    with open(json_file, 'r') as f:
        data = json.load(f)
        program_obj = get_program_object(program, data)
        return program_obj['domains']



def add_program_domain(program: str, new_domain: str):
    """
    Adds domain dict to program JSON object

    :return:
    """

    with open(json_file, 'r') as f:
        data = json.load(f)

    program_obj = get_program_object(program, data)
    program_obj['domains'].append(new_domain)

    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)

def remove_program_domain(program: str, domain_to_remove: str):
    """
    Adds domain dict to program JSON object

    :return:
    """

    with open(json_file, 'r') as f:
        data = json.load(f)

    program_obj = get_program_object(program, data)
    try:
        program_obj['domains'].remove(domain_to_remove)
    except:
        pass

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
