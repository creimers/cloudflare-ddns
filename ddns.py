import json
import os
import requests
import socket


def get_ip() -> str:
    """
    get the ip address of whoever executes the script
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    print(s.getsockname()[0])
    s.close()
    return str(ip_address)


def set_ip(current_ip: str):
    """
    sets the ip in via cloudflare api
    """
    zone_id = os.environ.get("ZONE_ID")
    record_id = os.environ.get("RECORD_ID")
    url = (
        "https://api.cloudflare.com/client/v4/zones/%(zone_id)s/dns_records/%(record_id)s"
        % {"zone_id": zone_id, "record_id": record_id}
    )

    api_key = os.environ.get("API_KEY")
    record_name = os.environ.get("RECORD_NAME")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {"type": "A", "name": record_name, "content": current_ip}
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    if response.status_code != 200:
        print(f"Error retrieving DNS record.")
        print(f"url={url}")
        print(f"headers={headers}")
        print(f"payload={payload}")
        print(f"response.status_code={response.status_code}")
        print(json.dumps(json.loads(response.content), indent = 2))
        exit(1)


def main():
    current_ip = get_ip()
    set_ip(current_ip)


if __name__ == "__main__":
    main()
