#!/usr/bin/python3
"""Write a Python script that fetches"""

if __name__ == "__main__":
    import requests as req
    r = req.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
