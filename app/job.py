# https://sky.pro/wiki/python/zapusk-funktsii-kazhdye-60-sek-v-python-alternativa-cronjob/
from threading import Timer
from time import sleep

class Job:

    def cancel(self):
        self.tt.cancel()
        self.tt = None

    def repeater(self, interval, function):
        self.tt = Timer(interval, self.repeater, [interval, function])
        self.tt.start()
        function()

    # @staticmethod
    # def repeater(interval, function):
    #     Timer(interval, Job.repeater, [interval, function]).start()
    #     function()

    # Пример использования: функция `my_task` будет вызываться каждые 2 секунды.

def my_task():
    print("Задача выполнена")


if __name__ == '__main__':
    # job = Job(2, my_task)
    # job.start()
    # sleep(5)
    # job.cancel()
    job = Job()
    job.repeater(2, my_task)
    sleep(10)
    job.cancel()