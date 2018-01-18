from AgendaPi import main

from src import PythonAgendaPiServer
from multiprocessing.managers import SyncManager
import signal

if __name__ == "__main__":

    def interupt_manager():
        signal.signal(signal.SIGINT, signal.SIG_IGN)
    manager = SyncManager()
    manager.start(interupt_manager)
    try:
        server = PythonAgendaPiServer.create_server()
        PythonAgendaPiServer.register()
        server.serve()

    finally:
        PythonAgendaPiServer.unregister()
        print('finally AgendaPi shutting down')
        manager.shutdown()
