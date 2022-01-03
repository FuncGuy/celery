import time

from celery import Celery
app = Celery('tasks', backend='redis://127.0.0.1:6379', broker='redis://127.0.0.1:6379')

@app.task(name='tasks.add')
def add(x, y):
    total = x + y
    print('{} + {} = {}'.format(x, y, total))
    time.sleep(10)
    return total

