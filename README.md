# Measure-Time-Benchmark
Benchmark class is used to compare the performance of different implementations of the same algorithm <br />
Usage example:
```py
def using_mul(T):
  return np.sum(T*T)*np.sum(T*T)
  
def using_pow(T):
  return np.sum(T*T)**2

T = np.random.rand(1, 100000000)
bmark = Benchmark([using_mul, using_pow])
bmark.start_tests(5, T)
```
Output is
```
time = 0.5824954986572266, func is using_mul
time = 0.2765678405761719, func is using_pow
the best time = 0.2765678405761719, the best func is using_pow
```
