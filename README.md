# Balsamic  
balsamic is a library for sending malicious pickles to a vunlerable application, via web requests, or a malicious server or client(currently ipv4 only).  
we will add more payloads but for now we just execute shell commands. via the oscmd payload.  
![image](https://github.com/malectricasoftware/balsamic/assets/107813117/c9e8138c-9f8f-4d68-b71c-331cf7a42343)

## useage (standalone)  
web request mode  
```
usage: balsamic.py webreq [-h] [-m METHOD] -u URL [-p PARAMETER] [-co COOKIE] -P PAYLOAD
                          [-c COMMAND] [-H HEADERS]

options:
  -h, --help            show this help message and exit
  -m METHOD, --method METHOD
  -u URL, --url URL
  -p PARAMETER, --parameter PARAMETER
  -co COOKIE, --cookie COOKIE
  -P PAYLOAD, --payload PAYLOAD
  -c COMMAND, --command COMMAND
  -H HEADERS, --headers HEADERS

```
socksend mode  
```
usage: balsamic.py socksend [-h] -rh RHOST -rp RPORT -P PAYLOAD [-c COMMAND] [-s STEPS] [-e]
                            [--ipv6]

options:
  -h, --help            show this help message and exit
  -rh RHOST, --rhost RHOST
  -rp RPORT, --rport RPORT
  -P PAYLOAD, --payload PAYLOAD
  -c COMMAND, --command COMMAND
  -s STEPS, --steps STEPS
  -e, --encode
  --ipv6                Use IPv6
```
socklisten mode
```
usage: balsamic.py socklisten [-h] -lp LPORT -P PAYLOAD [-c COMMAND] [-s STEPS] [-e] [--ipv6]

options:
  -h, --help            show this help message and exit
  -lp LPORT, --lport LPORT
  -P PAYLOAD, --payload PAYLOAD
  -c COMMAND, --command COMMAND
  -s STEPS, --steps STEPS
  -e, --encode
  --ipv6                Use IPv6
```

## useage (library)
```
from balsamic import balsamic
balsamic.utility.command="command"
balsamic.webreq("method", "url", "payload", "param", "cookie", custom_headers)
balsamic.socksend("rhost", rport, "payload", enc, steps, use_ipv6)
balsamic.socklisten(lport, "payload", enc, steps, use_ipv6)
```
