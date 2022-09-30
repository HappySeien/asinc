import unittest
from server import Server, DESC
from services.parse_cli_arguments import parse_cli_arguments


class TestServer(unittest.TestCase):
    """
    Тестирование сервера
    """
    args = parse_cli_arguments(DESC)
    server_ = Server(host=args.host, port=args.port)

    def setUp(self) -> None:
        self.server_.run()

    def tearDown(self) -> None:
        self.server_.close()
