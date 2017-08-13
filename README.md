# cloudflare DDNS python script

A tiny python script that updates a cloudflare dns record with your current ip.

Useful for raspberry pi projects for example.

In the current setup, it is expected that you clone this repo to `/home/pi` and don't change its name.

You can then register a cronjob executing `/home/pi/cloudflare-ddns/ddns.sh` in an interval of choice.
