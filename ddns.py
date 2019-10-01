import json
import os
import requests


def get_ip() -> str:
    """
    get the ip address of whoever executes the script
    """
    url = "http://ip.42.pl/raw"
    response = requests.get(url)
    return str(response.text)


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
    user_email = os.environ.get("USER_EMAIL")
    record_name = os.environ.get("RECORD_NAME")

    headers = {
        "X-Auth-Email": user_email,
        "X-Auth-Key": api_key,
        "Content-Type": "application/json",
    }

    payload = {"type": "A", "name": record_name, "content": current_ip}
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    print(response.status_code)


def main():
    current_ip = get_ip()
    set_ip(current_ip)


if __name__ == "__main__":
    main()
