from celery import Celery, signature, group

if __name__ == '__main__':
    celery = Celery()
    celery.config_from_object('config')

    result = celery.send_task("tasks.add", [2, 2])

    print(result.ready())
    print(result.get(timeout=3))
    print(result.ready())

    add = signature("tasks.add")
    r1 = add.apply_async((1, 2))
    print(r1.get())

    r2 = add.delay(9, 2)
    print(r2.get())

    g1 = group(
            signature('tasks.add', args=(99, 99)),
            signature('tasks.factorial', args=(5,)),
    )

    result_set = g1.delay()

    print(result_set.get())
