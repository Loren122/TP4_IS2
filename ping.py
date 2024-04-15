from abc import ABC, abstractmethod
import subprocess

class PingInterface(ABC):
    @abstractmethod
    def execute(self, ip_address: str) -> None:
        pass

class Ping(PingInterface):
    def execute(self, ip_address: str) -> None:
        if not ip_address.startswith("192."):
            print("Dirección IP no permitida para este método.")
            return

        self.executefree(ip_address)

    def executefree(self, ip_address: str) -> None:
        for _ in range(10):
            response = subprocess.run(["ping", "-c", "1", ip_address], stdout=subprocess.PIPE)
            print(response.stdout.decode('latin-1'))

class PingProxy(PingInterface):
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address: str) -> None:
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

# Ejemplo de uso:
ping_proxy = PingProxy()
ping_proxy.execute("192.168.0.254")  # Realiza ping a www.google.com
ping_proxy.execute("192.168.1.1")    # Realiza ping a la dirección si comienza con "192."
