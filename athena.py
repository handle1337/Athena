BANNER = """
 █████╗ ████████╗██╗  ██╗███████╗███╗   ██╗ █████╗ 
██╔══██╗╚══██╔══╝██║  ██║██╔════╝████╗  ██║██╔══██╗
███████║   ██║   ███████║█████╗  ██╔██╗ ██║███████║
██╔══██║   ██║   ██╔══██║██╔══╝  ██║╚██╗██║██╔══██║
██║  ██║   ██║   ██║  ██║███████╗██║ ╚████║██║  ██║
╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝
"""

import schedule

import filesystem
import core
from discovery import domain
from scanning import ip


class Program:
    def __init__(self, name: str):
        self.domains = core.get_program_domains(name)
        self.name = name

    def set_priority(self, priority: int):
        pass
    def get_priority(self, priority: int):
        pass

    def add_domain(self, domain: str):
        core.add_program_domain(self.name, domain)

    def remove_domain(self, domain: str):
        core.remove_program_domain(self.name, domain)




def recon():
    path = filesystem.target_dir_setup("test")

    filesystem.dump_domains_text(core.get_program_domains("test"), f"{path}domains.txt")

    domain.find_subdomains(f"{path}domains.txt", f"{path}subdomains.txt")
    ip.scan(f"{path}subdomains.txt")
    domain.probe_subdomains(f"{path}subdomains.txt", f"{path}probed_subdomains.txt")


def test_save_to_db():
    pass


def main():
    # db = Database()
    # db.__del__()
    print(BANNER)
    recon()

    # schedule.every(2).days.at("12:00").do(recon())

    # while True:
    #   schedule.run_pending()


if __name__ == "__main__":
    main()
