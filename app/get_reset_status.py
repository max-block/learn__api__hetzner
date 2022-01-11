from mb_std import hrequest

from app import IP, LOGIN, PASSWORD


def main():
    url = f"https://robot-ws.your-server.de/reset/{IP}"
    res = hrequest(url, auth=(LOGIN, PASSWORD))
    print(res.json)
    # {'reset': {'server_ip': '****', 'server_ipv6_net': '****', 'server_number': ****, 'type': ['power', 'hw', 'man'], 'operating_status': 'shut off'}}


if __name__ == "__main__":
    main()
