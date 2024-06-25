"""Иммитация локальной сети."""


class Server:
    """Класс описания работы серверов в сети."""

    count: int = 1

    def __init__(self) -> None:
        """."""
        self.ip: int = Server.count
        Server.count += 1


class Data:
    """Класс описания пакета информации."""

    def __init__(self, data: str, ip: int) -> None:
        """."""
        self.data: str = data
        self.ip: int = ip


class Router:
    """Класс описания работы роутера в сети."""

    def __init__(self):
        """."""
        self.buffer = []
        self.servers = []

    def link(self, server: Server):
        """Присоединение сервера к роутеру."""
        if server not in self.servers:
            self.servers.append(server)

    def unlink(self, server: Server):
        """Отсоединение сервера от роутера."""
        if server in self.servers:
            self.servers.remove(server)

    def upload_data(self, data: Data):
        """Загрузка данных на сервер."""
        self.buffer.append(data)

    def send_data(self):
        """Отправка всех пакетов из буфера роутера серверам."""
        for data in self.buffer:
            for server in self.servers:
                if server.ip == data.ip:
                    print(f"""Данные: {data.data} на ip-адрес
                          {server.ip} - отправлены!""")


if __name__ == '__main__':

    router = Router()

    sv1 = Server()
    sv2 = Server()

    data1 = Data('строка с данными', sv1.ip)
    data2 = Data('строка с данными2', sv2.ip)

    router.link(sv1)
    router.link(sv2)

    router.upload_data(data1)
    router.upload_data(data2)

    router.send_data()
