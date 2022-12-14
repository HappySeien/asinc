import dis


class ServerVerifier(type):
    def __init__(self, clsname, bases, clsdict):
        methods = []
        attributes = []
        for element in clsdict:
            try:
                res = dis.get_instructions(clsdict[element])
            except TypeError:
                pass
            else:
                for el in res:
                    if el.opname == 'LOAD_GLOBAL':
                        if el.argval not in methods:
                            methods.append(el.argval)
                    elif el.opname == 'LOAD_ATTR':
                        if el.argval not in attributes:
                            attributes.append(el.argval)
        if 'connect'.lower() in methods:
            raise TypeError("Северный класс не может использовать метод 'connect'")
        if not ('socket_transport'.lower() in attributes and 'create_socket'.lower() in methods):
            raise TypeError('Некорректная инициализация сокета')
        super.__init__(clsname, bases, clsdict)
