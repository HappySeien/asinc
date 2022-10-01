import sys

import pytest
import socket as s

from asinc_chat.services.JIMProtocol import MessageBuilder
from asinc_chat.client import Client

@pytest.fixture
def socket_old_style(request):
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    def socket_teardown():
        _socket.close()
    request.addfinalizer(socket_teardown)
    return _socket

@pytest.fixture
def socket():
    _socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    yield _socket
    _socket.close()

@pytest.fixture
def client():
    _client = Client()
    yield _client
    

@pytest.fixture
def my_std():
    orig_std = sys.stdin
    sys.stdout = 'User'
    yield sys.stdin
    sys.stdout = orig_std


@pytest.fixture
def responce():
    msg = MessageBuilder.create_presence_message('User')
    yield msg


def test_server_connect(socket):
    socket.connect(('localhost', 8888))
    assert socket


def test_responce_generating(responce):
    assert responce == MessageBuilder({'response': 200, 'alert': 'default'})
