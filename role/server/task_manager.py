class TaskInstance:
    def __init__(self, id_) -> None:
        self.id = id_


class TaskManager:
    TASKID = 0

    def __init__(self) -> None:
        self.task_list = []

    def regist_task(self):
        """Add task to list, waiting to be applied 
        """
        pass

    def allocate_task(self):
        """Give a task to worker, waitng finish report
        """
        pass

    def pay_over_task(self):
        """Delivery finished task to client
        """
        pass
