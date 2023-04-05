"""import mariadb
import filesystem
import logging
from logger import output

user = filesystem.get_db_user()
password = filesystem.get_db_password()
host = filesystem.get_db_host()
port = filesystem.get_db_port()

conn = None

try:
    conn = mariadb.connect(
        user=user,
        password=password,
        host=host,
        port=int(port),
        database="targets"
    )

    print(f"[!]Connecting to MariaDB")
    output.log_element("user", user)
    output.log_element("host", host)
    output.log_element("port", port)

    cursor = conn.cursor(prepared=True)

except mariadb.Error as error:
    print(f"[Error] connecting to MariaDB server: {error}")


def execute(query, data=None):
    try:
        cursor.execute(query, data)
    except mariadb.Error as e:
        print(f"[Error] Unable to execute query {e}")


def insert_domain(url):
    execute("INSERT INTO domain ('url') VALUES (?)", url)
    conn.commit()


def insert_subdomain(url):
    execute("INSERT INTO subdomain ('url') VALUES (?)", url)
    conn.commit()


def insert_ip(ip):
    execute("INSERT INTO ip ('address') VALUES (?)", ip)
    conn.commit()


def get_domains():
    cursor.execute("SELECT domain FROM targets")
    result = cursor.fetchall()
    return result


def get_subdomains():
    cursor.execute("SELECT subdomain FROM targets")
    result = cursor.fetchall()
    return result


def get_ips():
    cursor.execute("SELECT ip FROM targets")
    result = cursor.fetchall()
    return result


def insert_program(name, domains, private=0, platform=1, expl_level=1, priority=1):

    print(f"Inserting target: {name} into database\n")

    cursor.execute("INSERT INTO program ('name', 'platform_id', 'expl_level', 'priority') VALUES (?,?,?,?)")


    try:

    except mariadb.Error as e:
        print(f"[!] Error inserting data {e}")
    finally:
        conn.close()


def __del__():
    conn.close()
"""