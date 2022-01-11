from pprint import pprint

from mb_std import hrequest

from app import IP, LOGIN, PASSWORD


def main():
    params = {
        "status": "active",
        "whitelist_hos": "true",
        "rules[input][0][name]": f"discard all",
        "rules[input][0][ip_version]": "ipv4",
        "rules[input][0][src_ip]": "",
        "rules[input][0][dst_port]": "",
        "rules[input][0][action]": "discard",
    }
    url = f"https://robot-ws.your-server.de/firewall/{IP}"
    res = hrequest(url, method="post", params=params, auth=(LOGIN, PASSWORD), json_params=False)
    pprint(res.json)


if __name__ == "__main__":
    main()
