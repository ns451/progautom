class Fibonacci:
    
    def __init__(self, n):
        self.n = n

    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    def numero_aureo(self):
        return self.fib(self.n + 1) / self.fib(self.n)

f = Fibonacci(20)
print(f.numero_aureo())
