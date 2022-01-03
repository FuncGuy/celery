import time

from celery.result import AsyncResult

from main import add
result = add.delay(1, 2)

while True:
    _result2 = AsyncResult(result.task_id)
    status = _result2.status
    print(status)
    if 'SUCCESS' in status:
        print('result after 5 sec wait {result2}'.format(result2=_result2.get()))
        break
    time.sleep(5)