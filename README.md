# Balsamic  
balsamic is a library for sending malicious pickles to a vunlerable application, via web requests, or a malicious server or client(currently ipv4 only).  
we will add more payloads but for now we just execute shell commands. via the oscmd payload.  

## useage (standalone)  
web request mode  
```
usage: balsamic.py webreq [-h] -s {http,https} [-m METHOD] -rh RHOST -rp RPORT [-p PARAMETER] [-co COOKIE] -P PAYLOAD [-c COMMAND]

options:
  -h, --help            show this help message and exit
  -s {http,https}, --schema {http,https}
  -m METHOD, --method METHOD
  -rh RHOST, --rhost RHOST
  -rp RPORT, --rport RPORT
  -p PARAMETER, --parameter PARAMETER
  -co COOKIE, --cookie COOKIE
  -P PAYLOAD, --payload PAYLOAD
  -c COMMAND, --command COMMAND
```
socksend mode  
```
usage: balsamic.py socksend [-h] -rh RHOST -rp RPORT -P PAYLOAD [-c COMMAND] [-s STEPS]

options:
  -h, --help            show this help message and exit
  -rh RHOST, --rhost RHOST
  -rp RPORT, --rport RPORT
  -P PAYLOAD, --payload PAYLOAD
  -c COMMAND, --command COMMAND
  -s STEPS, --steps STEPS
```
socklisten mode
```
usage: balsamic.py socklisten [-h] -lp LPORT -P PAYLOAD [-c COMMAND]

options:
  -h, --help            show this help message and exit
  -lp LPORT, --lport LPORT
  -P PAYLOAD, --payload PAYLOAD
  -c COMMAND, --command COMMAND
```

## useage (library)
```
from balsamic import balsamic
balsamic.utility.command="command"
balsamic.webreq("schema","method","rhost","rport","payload","parameter","cookie")
balsamic.socksend("ip",port,"payload",steps)
balsamic.socklisten(port,"payload",steps)
```
