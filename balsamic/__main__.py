from balsamic import balsamic
import argparse
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
		socksendparser.add_argument("-s","--steps",default="0")

		#create subparser for socklisten attack
		socklistenparser=subparse.add_parser("socklisten")
		socklistenparser.add_argument("-lp","--lport",required=True)
		socklistenparser.add_argument("-P","--payload",required=True)
		socklistenparser.add_argument("-c","--command")
		socklistenparser.add_argument("-s","--steps",default="0")
		
		#return parsed arguments
		args = parser.parse_args()
		return args

	args=parser()
	if args.command:
		balsamic.updatecmd(args.command)

	if args.attack == "webreq":
		balsamic.webreq(args.schema,args.method,args.rhost,args.rport,args.payload,args.parameter,args.cookie)
	elif args.attack == "socksend":
		balsamic.socksend(args.rhost,args.rport,args.payload,args.steps)
	elif args.attack == "socklisten":
		balsamic.socklisten(args.lport,args.payload,args.steps)
