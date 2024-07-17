class Worker:
    def do_some_work(self):
        print("Let me do some work here")

    def undo_work(self):
        print("Sorry, I will have to undo my work!")

class Command:
    def work(self):
        pass
    def redo(self):
        pass

    def undo(self):
        pass

class ImportantCommand(Command):

    def __init__(self, worker) -> None:
        self.worker = worker

    def work(self):
        worker.do_some_work()

    def redo(self):
        worker.do_some_work()

    def undo(self):
        worker.undo_work()

class SillyCommand(Command):

    def __init__(self, worker) -> None:
        super().__init__()

    def work(self):
        worker.undo_work()

    def redo(self):
        return worker.undo_work()
    
    def undo(self):
        return worker.do_some_work()

class RemoteControl:
    def submit(self, commands: list[Command]):
        for command in commands:
            command.work()
    
if __name__ == "__main__":
    proxy = RemoteControl()
    worker = Worker()
    mycommand = ImportantCommand(worker)
    sillycommand = SillyCommand(worker)
    proxy.submit([mycommand, sillycommand])
