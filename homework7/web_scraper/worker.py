import sys

from rq import Connection, Worker
'''
Я взял этот код со страницы https://python-rq.org/docs/workers/ (тут официальная документация rq). 
Использую его как есть.
'''

def worker_run():
    with Connection():
        qs = sys.argv[1:] or ['default']

        w = Worker(qs)
        w.work()


if __name__ == '__main__':
    worker_run()
