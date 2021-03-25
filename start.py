import os
import sys

from constants.common import CommonConstants


class BootLoader:
    def __init__(self) -> None:
        os.environ[CommonConstants.WORKON_HOME] = os.path.dirname(os.path.abspath(__file__))
        sys.path.append(os.path.join(os.getenv(CommonConstants.WORKON_HOME), 'bin'))
        os.chdir(os.getenv(CommonConstants.WORKON_HOME))
        self.server_local_storage_dir = os.path.join(os.getenv(CommonConstants.WORKON_HOME), CommonConstants.ROLE, CommonConstants.SERVER, CommonConstants.LOCAL_STORAGE)
        self.client_local_storage_dir = os.path.join(os.getenv(CommonConstants.WORKON_HOME), CommonConstants.ROLE, CommonConstants.CLIENT, CommonConstants.LOCAL_STORAGE)
        self.worker_local_storage_dir = os.path.join(os.getenv(CommonConstants.WORKON_HOME), CommonConstants.ROLE, CommonConstants.WORKER, CommonConstants.LOCAL_STORAGE)
        self.role_input_times = 0

    def get_role_handler(self, role):
        if role == CommonConstants.SERVER:
            pass  # TODO 增加服务器端处理类
        elif role == CommonConstants.CLIENT:
            pass  # TODO 增加客户端处理类
        elif role == CommonConstants.WORKER:
            pass  # TODO 增加工人处理类

    def _role_validating(self, role):
        if self.role_input_times < 3:
            if role in [CommonConstants.SERVER, CommonConstants.SERVER_ABBR]:
                return CommonConstants.SERVER
            elif role in [CommonConstants.CLIENT, CommonConstants.CLIENT_ABBR]:
                return CommonConstants.CLIENT
            elif role in [CommonConstants.WORKER, CommonConstants.WORKER_ABBR]:
                return CommonConstants.WORKER
            else:
                self.role_input_times += 1
                self.get_role_handler(input('Role can only be server/client/worker or s/c/w, please input again: '))
        else:
            print('Role input invalid, exit...')
            sys.exit(0)

    def run(self):
        role = input("Please select ROLE( [server/client/worker] or [s/c/w] ): ")
        Handler = self.get_role_handler(self._role_validating(role))
        if role in [CommonConstants.CLIENT, CommonConstants.WORKER]:
            self.host = input("Please input server host: ")
            self.port = input("Please input server port: ")
        elif role in [CommonConstants.SERVER]:
            self.port = input("Please input listener port: ")
        h = Handler()


if __name__ == "__main__":
    b = BootLoader()
    b.run()
