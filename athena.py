BANNER = """
 █████╗ ████████╗██╗  ██╗███████╗███╗   ██╗ █████╗ 
██╔══██╗╚══██╔══╝██║  ██║██╔════╝████╗  ██║██╔══██╗
███████║   ██║   ███████║█████╗  ██╔██╗ ██║███████║
██╔══██║   ██║   ██╔══██║██╔══╝  ██║╚██╗██║██╔══██║
██║  ██║   ██║   ██║  ██║███████╗██║ ╚████║██║  ██║
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝
"""
print(BANNER)

# TODO: Implement asyncio

import schedule

import filesystem
#import db_handler
import core
from discovery import domain
from plugins import cvelookup

"""
class Target:
    def __init__(self, name):
        self.domains = []
        self.name = name

    def add_parent_domain(self, parent_domain):
        self.domains.append(parent_domain)

    def fetch(self):
        pass
"""


def recon():

    path = filesystem.target_dir_setup("test")

    filesystem.dump_domains_text(core.get_program_domains("test"), f"{path}domains.txt")

    domain.find_subdomains(f"{path}domains.txt", f"{path}subdomains.txt")
    domain.probe_subdomains(f"{path}subdomains.txt", f"{path}probed_subdomains.txt")


def test_save_to_db():
    pass


def main():
    # db = Database()
    # db.__del__()



    #schedule.every(2).days.at("12:00").do(recon())

    #while True:
     #   schedule.run_pending()
    recon()


if __name__ == "__main__":
    recon()
