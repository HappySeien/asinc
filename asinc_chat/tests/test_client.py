import unittest
from client import Client, DESC
from services.parse_cli_arguments import parse_cli_arguments


class ClientTest(unittest.TestCase):
    """
    Тесты клиента
    """
    args = parse_cli_arguments(DESC)
    client_ = Client(host=args.host, port=args.port)
    
    def setUp(self) -> None:
        self.client_.run()

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
    