# Sen-Yai-Networking
A Python Flask server for routing traffic through Tor.

To use, first install from flask, flask_cors, and requests_tor from pip (pip3 for Python 3, most commonly) and then run:

```bash
python3 sen-yai-networking.py
```

Then, it will be hosted at 127.0.0.1:8006. As a result, it will pass the result of the request to the user like in the response in HTTP in TurboWarp. This also bypasses CORS to an extent as well.

You must have either Tor Browser or Tor open on your computer to use this server, and you can indeed have Sen Yai Networking and Sen Yai API in separate Terminal tabs if needed. It is meant for *NIX systems like macOS or Linux in mind, but you can port it to Windows if needed.
