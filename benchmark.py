from time import time
from typing import List, Callable
import numpy as np

class Benchmark:
  @staticmethod
  def measure_time(func):
      def inner(*args):
        s = time()
        result = func(*args)
        return time() - s
      inner.__name__ = func.__name__
      return inner
  
  def __init__(self, funcs: List[Callable]):
    self.funcs = list(map(lambda f: Benchmark.measure_time(f), funcs))
  
  def print_results(self, times):
    min_idx = 0
    for i in range(len(times)):
      print(f'time = {times[i]}, func is {self.funcs[i].__name__}')
      if times[i] < times[min_idx]:
        min_idx = i
    print(f'the best time = {times[min_idx]}, the best func is {self.funcs[min_idx].__name__}')
  
  def start_tests(self, num_reps: int, *args):
    times = np.zeros(len(self.funcs))
    for i in range(num_reps):
      results = [f(*args) for f in self.funcs]
      times += np.array([res for res in results])
    times = times/num_reps
    self.print_results(times)

# ====== usage example =========

def using_mul(T):
  return np.sum(T*T)*np.sum(T*T)
  
def using_pow(T):
  return np.sum(T*T)**2

T = np.random.rand(1, 100000000)
bmark = Benchmark([using_mul, using_pow])
bmark.start_tests(5, T)
