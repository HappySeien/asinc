import unittest
from server import Server, DESC
from client import Client
from services.parse_cli_arguments import parse_cli_arguments


class TestServer(unittest.TestCase):
    """
    Тестирование сервера
    """
    args = parse_cli_arguments(DESC)
    server_ = Server(host=args.host, port=args.port)
    client_ = Client(host=args.host, port=args.port)

    def setUp(self) -> None:
        self.server_.run()

    def tearDown(self) -> None:
        self.server_.close()

    def test_parse_message(self):
        pass

    def test_send_response(self):
        pass



if __name__ == '__main__':
    unittest.main()
    