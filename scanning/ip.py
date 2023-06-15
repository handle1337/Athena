

import subprocess
import sys

def scan(in_file):
    """
    Scans hosts with nmap


    :param in_file: Input file to feed nmap
    :return: None
    """

    print(f"in: {in_file}\n")
    # For now we only scan for ssh because testing is easier/faster that way lol
    nmap_process = subprocess.run(f"nmap -n -A -T4 -sV -p 22 -iL {in_file}", stdout=sys.stdout,
                                       shell=True,
                                       stderr=subprocess.STDOUT)



