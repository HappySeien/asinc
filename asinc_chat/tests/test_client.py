import unittest
from server import Server
from client import Client, DESC
from services.parse_cli_arguments import parse_cli_arguments


class ClientTest(unittest.TestCase):
    """
    Тесты клиента
    """
    args = parse_cli_arguments(DESC)
    server_ = Server(host=args.host, port=args.port)
    client_ = Client(host=args.host, port=args.port)
    
    def setUp(self) -> None:
        self.server_.run()

    def tearDown(self) -> None:
        pass

    def test_parse_response(self):
        pass

    def test_send_message(self):
        pass


if __name__ == '__main__':
    unittest.main()
    