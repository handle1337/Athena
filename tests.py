import os
import core
import filesystem


def filesystem_setup_test():
    args_test = ["d_test1", "d_test2", "d_test3"]
    path = filesystem.target_dir_setup("test", *args_test)
    print(f"\n path :   {path}\n")

    assert os.path.exists(path)

    return path


def filesystem_remove_test(path):
    filesystem.target_dir_remove(path)
    assert not os.path.exists(path)


def json_parser_test():
    print(core.get_programs_unsorted())
    print(core.get_programs_sorted())
    print(core.add_program_domain("test", "lo.com"))


def test_obj_dumps():
    print(core.get_program_domains("test"))


def database_domain():
    pass


def database_subdomain():
    pass


def database_ip():
    pass


def test_subdomains():

    pass


def test_domain_dump():
    filesystem.dump_domains_text(core.get_program_domains("test"), "domains.txt")



def subdomain_brute_test():
    pass


if __name__ == "__main__":
    program_path = filesystem_setup_test()
    filesystem_remove_test(program_path)
    json_parser_test()
    test_obj_dumps()
    test_domain_dump()
