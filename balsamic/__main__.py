from balsamic import balsamic
if __name__ == "__main__":
    # Importing argparse
    print('''\33[49m                    \33[38;5;15;49m▄▄▄▄▄▄▄▄\33[49m                    \33[m
\33[49m              \33[38;5;15;49m▄▄\33[48;5;15m                \33[38;5;15;49m▄▄\33[49m              \33[m
\33[49m           \33[38;5;15;49m▄\33[48;5;15m                        \33[38;5;15;49m▄\33[49m           \33[m
\33[49m        \33[38;5;15;49m▄\33[48;5;15m            \33[38;5;95;48;5;15m▄\33[38;5;137;48;5;15m▄▄▄▄\33[38;5;95;48;5;15m▄\33[48;5;15m            \33[38;5;15;49m▄\33[49m        \33[m
\33[49m      \33[38;5;15;49m▄\33[48;5;15m              \33[48;5;95m      \33[48;5;15m              \33[38;5;15;49m▄\33[49m      \33[m
\33[49m     \33[38;5;15;49m▄\33[48;5;15m               \33[48;5;95m      \33[48;5;15m               \33[38;5;15;49m▄\33[49m     \33[m
\33[49m    \33[48;5;15m                 \33[48;5;0m    \33[38;5;188;48;5;0m▄▄\33[48;5;15m                 \33[49m    \33[m
\33[49m   \33[48;5;15m                  \33[48;5;0m    \33[48;5;188m  \33[48;5;15m                  \33[49m   \33[m
\33[49m  \33[48;5;15m                   \33[48;5;0m    \33[48;5;188m  \33[48;5;15m                   \33[49m  \33[m
\33[49m  \33[48;5;15m                 \33[38;5;0;48;5;15m▄\33[48;5;0m \33[38;5;188;48;5;0m▄▄▄\33[48;5;0m \33[38;5;0;48;5;188m▄▄\33[48;5;0m \33[38;5;0;48;5;15m▄\33[48;5;15m                 \33[49m  \33[m
\33[49m \33[48;5;15m                \33[38;5;0;48;5;15m▄\33[48;5;0m \33[38;5;188;48;5;0m▄\33[48;5;188m     \33[38;5;232;48;5;0m▄\33[48;5;0m    \33[38;5;0;48;5;15m▄\33[48;5;15m                \33[49m \33[m
\33[49m \33[48;5;15m               \33[38;5;0;48;5;15m▄\33[48;5;0m \33[48;5;188m        \33[38;5;188;48;5;0m▄\33[48;5;0m    \33[38;5;0;48;5;15m▄\33[48;5;15m               \33[49m \33[m
\33[49m \33[48;5;15m              \33[38;5;0;48;5;15m▄\33[48;5;0m \33[48;5;188m          \33[48;5;0m     \33[38;5;0;48;5;15m▄\33[48;5;15m              \33[49m \33[m
\33[49m \33[48;5;15m              \33[48;5;0m \33[38;5;252;48;5;0m▄\33[48;5;188m           \33[48;5;0m     \33[48;5;15m              \33[49m \33[m
\33[49m  \33[48;5;15m            \33[38;5;0;48;5;15m▄\33[48;5;0m \33[48;5;188m            \33[48;5;0m     \33[38;5;0;48;5;15m▄\33[48;5;15m            \33[49m  \33[m
\33[49m  \33[48;5;15m            \33[48;5;0m  \33[48;5;188m            \33[38;5;235;48;5;235m▄\33[48;5;0m     \33[48;5;15m            \33[49m  \33[m
\33[49m   \33[48;5;15m           \33[48;5;0m  \33[48;5;188m            \33[48;5;0m      \33[48;5;15m           \33[49m   \33[m
\33[49m    \33[48;5;15m          \33[48;5;0m   \33[48;5;188m          \33[38;5;246;48;5;188m▄\33[48;5;0m      \33[48;5;15m          \33[49m    \33[m
\33[49m     \33[49;38;5;15m▀\33[48;5;15m         \33[48;5;0m                  \33[48;5;15m         \33[49;38;5;15m▀\33[49m     \33[m
\33[49m      \33[49;38;5;15m▀\33[48;5;15m        \33[38;5;15;48;5;0m▄\33[48;5;0m                \33[38;5;15;48;5;0m▄\33[48;5;15m        \33[49;38;5;15m▀\33[49m      \33[m
\33[49m        \33[49;38;5;15m▀\33[48;5;15m        \33[38;5;15;48;5;0m▄▄▄▄▄▄▄▄▄▄▄▄▄▄\33[48;5;15m        \33[49;38;5;15m▀\33[49m        \33[m
\33[49m           \33[49;38;5;15m▀\33[48;5;15m                        \33[49;38;5;15m▀\33[49m           \33[m
\33[49m              \33[49;38;5;15m▀▀\33[38;5;15;48;5;15m▄\33[48;5;15m               \33[49;38;5;15m▀▀\33[49m              \33[m
\33[49m                    \33[49;38;5;15m▀▀▀▀▀▀▀▀\33[49m                    \33[m
''')
    import argparse

    # Define the parser function
    def parser():
        
        # Create the base argument parser
        parser = argparse.ArgumentParser(description="balsamic args")
        subparse = parser.add_subparsers(dest="attack")

        # Create subparsers for different attacks
        webreqparser = subparse.add_parser("webreq")
        webreqparser.add_argument("-m", "--method")
        webreqparser.add_argument("-u", "--url", required=True)
        webreqparser.add_argument("-p", "--parameter")
        webreqparser.add_argument("-co", "--cookie")
        webreqparser.add_argument("-P", "--payload", required=True)
        webreqparser.add_argument("-c", "--command")
        webreqparser.add_argument("-H", "--headers")  # New argument for custom headers

        socksendparser = subparse.add_parser("socksend")
        socksendparser.add_argument("-rh", "--rhost", required=True)
        socksendparser.add_argument("-rp", "--rport", required=True)
        socksendparser.add_argument("-P", "--payload", required=True)
        socksendparser.add_argument("-c", "--command")
        socksendparser.add_argument("-s", "--steps", default="0")
        socksendparser.add_argument("-e", "--encode", action="store_true")
        socksendparser.add_argument("--ipv6", action="store_true", help="Use IPv6")

        socklistenparser = subparse.add_parser("socklisten")
        socklistenparser.add_argument("-lp", "--lport", required=True)
        socklistenparser.add_argument("-P", "--payload", required=True)
        socklistenparser.add_argument("-c", "--command")
        socklistenparser.add_argument("-s", "--steps", default="0")
        socklistenparser.add_argument("-e", "--encode", action="store_true")
        socklistenparser.add_argument("--ipv6", action="store_true", help="Use IPv6")
        
        # Return parsed arguments
        args = parser.parse_args()
        return args

    args = parser()
    if args.command:
        balsamic.updatecmd(args.command)

    # Extract custom headers from the arguments
    if args.attack == "webreq":
        balsamic.webreq(args.method, args.url, args.payload, args.parameter, args.cookie, custom_header=args.headers)
    elif args.attack == "socksend":
        balsamic.socksend(args.rhost, args.rport, args.payload, args.encode, args.steps,args.ipv6)
    elif args.attack == "socklisten":
        balsamic.socklisten(args.lport, args.payload, args.encode, args.steps,args.ipv6)
