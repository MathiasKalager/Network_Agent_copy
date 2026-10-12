# from utils.routers import get_router


class Router:
    def __init__(self, name: str, host: str, user: str, password: str):
        self.name = name
        self.host = host
        self.user = user
        self.password = password


# Her legger vi inn alle rutere vi vil støtte
ROUTERS = {
    "router1": Router(name="R1", host="192.168.0.1", user="restconf", password="pswd"),
    "router2": Router(name="R2", host="172.16.0.1", user="restconf", password="pswd"),
    "router3": Router(name="R3", host="203.0.113.1", user="restconf", password="pswd"),
}


def get_router(name: str) -> Router:
    """
    Henter Router-objekt basert på navn.
    Kaster KeyError hvis router ikke finnes.
    """
    return ROUTERS[name.lower()]
