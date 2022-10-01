import unittest
from server import DESC
from client import Client
from services.JIMProtocol import MessageBuilder
from services.parse_cli_arguments import parse_cli_arguments


class TestServer(unittest.TestCase):
    """
    Тестирование сервера
    """

    def setUp(self) -> None:
        self.args = parse_cli_arguments(DESC)

    def tearDown(self) -> None:
        pass

    def test_parse_message(self):
        pass

    def test_send_response(self):
        pass 


if __name__ == '__main__':
    unittest.main()
    