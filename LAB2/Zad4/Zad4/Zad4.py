class Fibonacci:
    def __init__(self, steps):
        self.steps = steps   
        self.count = 0       
        self.a, self.b = 0, 1  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.count >= self.steps:
            raise StopIteration  
        value = self.a
        self.a, self.b = self.b, self.a + self.b 
        self.count += 1
        return value

fib = Fibonacci(10)

for num in fib:
    print(num)

