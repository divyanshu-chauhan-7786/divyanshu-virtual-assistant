# Fibonacci series is a sequence of integers where each number is the some of the to predicting numbers,
# defined by a mathmatical recurrence relationship.

def fibonacci(n):
    # The first two numbers in the Fibonacci series are 0 and 1.
    fib_sequence = [0, 1]
    
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    
    return fib_sequence


def main():
    print("fibonacci sequence generator  ")
    n =int(input("Enter your number of term :"))
    if n <= 0:
        print("Invalid input. Please enter a positive integer.")
    elif n <= 1:
        print("Fibonacci sequence upto", n, "term is : [0]")
    else:
        print("Fibonacci sequence upto", n, "term is :", fibonacci(n))
        print("Sum of the sequence is :", sum(fibonacci(n)))

if __name__ == '__main__':
  main()
