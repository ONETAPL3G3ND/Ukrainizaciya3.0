import psutil
class ProcessController:
    @classmethod
    def kill_task_manager(cls):
        for proc in psutil.process_iter():
            if proc.name() == "Taskmgr.exe":
                print("Диспетчер задач найден. Закрываю диспетчер задач...")
                proc.kill()
                print("Диспетчер задач успешно закрыт.")
                return
        print("Диспетчер задач не найден.")

    @classmethod
    def kill_explorer_manager(cls):
        for proc in psutil.process_iter():
            if proc.name() == "explorer.exe":
                print("Explorer найден. Закрываю диспетчер задач...")
                proc.kill()
                print("Explorer успешно закрыт.")
                return
        print("Explorer не найден.")