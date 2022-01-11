from pprint import pprint

from mb_std import hrequest

from app import IP, LOGIN, PASSWORD


def main():
    url = f"https://robot-ws.your-server.de/firewall/{IP}"
    res = hrequest(url, auth=(LOGIN, PASSWORD))
    pprint(res.json)


if __name__ == "__main__":
    main()
