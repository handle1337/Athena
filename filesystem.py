import os
import shutil
from configparser import ConfigParser

conf_file = "config.INI"
config = ConfigParser()
config.read(conf_file)




def get_db_host():
    return config["mariadb"]["Host"]


def get_db_user():
    return config["mariadb"]["User"]


def get_db_password():
    return config["mariadb"]["Password"]


def get_db_port():
    return config["mariadb"]["Port"]


def get_json_filename():
    return config["files"]["JSON"]


def create_folder(path):
    print("paths : " + path + "\n")
    if not os.path.isdir(path):
        os.mkdir(path)


def target_dir_setup(program, *args) -> str:
    assets = args  # assets becomes a tuple containing args' elements
    print(assets)
   # print(type(assets))

    print("program : " + program + "\n")

    p_path = os.path.expanduser(f"~/{program}/")

    create_folder(p_path)

    for asset in assets:
        print("iter paths : " + asset + "\n")
        create_folder(f"{p_path}{asset}/")

    return p_path


def target_dir_remove(path):
    shutil.rmtree(path)


def dump_domains_text(domains, filename):
    with open(filename, 'w') as f:
        for domain in domains:
            f.write(f"{domain}\n")
