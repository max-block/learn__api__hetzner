import os

from dotenv import load_dotenv
from mb_commons import hrequest

load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
IP = os.getenv("IP")


def main():
    url = f"https://robot-ws.your-server.de/reset/{IP}"
    res = hrequest(url, auth=(LOGIN, PASSWORD))
    print(res.json)
    # {'reset': {'server_ip': '****', 'server_ipv6_net': '****', 'server_number': ****, 'type': ['power', 'hw', 'man'], 'operating_status': 'shut off'}}


if __name__ == "__main__":
    main()
