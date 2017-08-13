# cloudflare DDNS python script

A tiny python script that updates a cloudflare dns record with your current ip.

Useful for raspberry pi projects for example.

In the current setup, it is expected that you clone this repo to `/home/pi` and don't change its name.

You need to put an `.env` file into `/home/pi/cloudflare-ddns` that looks like `.env-example`.

You can then register a cronjob executing `/home/pi/cloudflare-ddns/ddns.sh` in an interval of choice.
