from constants.common import CommonConstants

class ClientInstance:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role


class ClientManager:
    def __init__(self) -> None:
        self.client_list = []

    def add_client(self, name, role):
        client = ClientInstance(name, role)
        self.client_list.append(client)

    def get_all_client_name(self):
        return [i.name for i in self.client_list if i.name==CommonConstants.CLIENT]

    def get_all_worker_name(self):
        return [i.name for i in self.client_list if i.name==CommonConstants.WORKER]
