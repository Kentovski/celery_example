from celery.task import task
import math

@task
def add(a, b):
    return a + b

@task
def factorial(n):
    return math.factorial(n)
