import json
import filesystem
import db_handler
from discovery import domain
from configparser import ConfigParser
from termcolor import colored

json_file = filesystem.get_json_filename()


# TODO: Fetch programs from BB platforms

def get_programs_unsorted() -> list:
    """
    Get all programs from set JSON targets file

    Returns empty list if exception is raised.

    :return: List of JSON objects
    """
    programs = []
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
            for i in data["program"]:
                programs.append(i)
            return programs
    except Exception as e:
        print(f"Error couldn't open JSON targets file {e}")
        return []


def get_programs_sorted():
    """
    Get all programs sorted by priority level from set JSON targets file

    Returns empty list if exception is raised.

    :return: List of JSON objects
    """
    programs = get_programs_unsorted()
    if not programs:
        return []
    else:
        programs.sort(key=lambda x: x["priority"])
        return programs


def get_program_object(program) -> dict:
    """
    Get program JSON object information

    :return: JSON obj dictionary
    """
    programs = get_programs_sorted()
    print(programs)
    for program_object in programs:
        if program_object["name"] == program:
            return program_object
    return {}


def get_program_domains(program) -> list:
    """
    Get program JSON object information

    :return: list of domains
    """

    domains = []

    program_obj = get_program_object(program)
    #print(f"\n{program_obj['domains']} \n {type(program_obj['domains'])}")

    for domain in program_obj['domains']:
        domains.append(domain.get('url'))

    return domains


def json_to_db_bulk():
    """
    Convert all JSON targets object to DB row
    :return:
    """


def json_to_db(program) -> dict:
    program = get_program_object(program)
    print(f"{program['name']}")
    db_handler.insert_domain(program['name'])
    print(f"{program['url']}")
    print(f"{program['expl_level']}")
    db_handler.insert_program(program['name'], get_program_domains("test"))
    print(f"{program['priority']}")
    print(f"{program['domains']}")
    return program
