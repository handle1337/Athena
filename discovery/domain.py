import asyncio
import re
import subprocess
import sys


def remove_protocol(url):
    # TODO: use this to clean stdin files

    if url.startswith('http'):
        url = re.sub(r'https?://', '', url)
    if url.startswith('www.'):
        url = re.sub(r'www.', '', url)
    return url


# TODO make the file param optional as you should be able to just run one subdomain as well
def find_subdomains(in_file, out_file):
    """
    Begins searching for live subdomains


    :param in_file: Input file to feed subfinder
    :param out_file: Path to file for httpx output
    :return: None
    """

    print(f"in: {in_file}\n")
    print(f"out: {out_file}\n")

    subfinder_process = subprocess.run(f"subfinder -silent -dL {in_file} -o {out_file}", stdout=sys.stdout,
                                       shell=True,
                                       stderr=subprocess.STDOUT)


def probe_subdomains(in_file, out_file):
    httprobe_process = subprocess.run(f"cat {in_file} | httprobe | tee {out_file}", stdout=sys.stdout,
                                      shell=True,
                                      stderr=subprocess.STDOUT)


def brute_directories(wordlist_file, target, port=80):
    ffuf_process = subprocess.Popen(f"ffuf -w {wordlist_file} {target}/FUZZ", stdout=subprocess.PIPE,
                                    universal_newlines=True,
                                    stderr=subprocess.PIPE)
