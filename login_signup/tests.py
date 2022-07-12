import valve.source.a2s
SERVER_ADDRESS = ('13.126.178.114',27015)
with valve.source.a2s.ServerQuerier(SERVER_ADDRESS) as server:

    print(server.info()["server_type"])


