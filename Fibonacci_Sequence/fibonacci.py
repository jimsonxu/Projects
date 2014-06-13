#!/usr/bin/python3

def get_nth_fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return get_nth_fib(n-2) + get_nth_fib(n-1)

# Returns a list of the Fibonacci sequence starting at 0, up to the nth Fibonacci number
def get_fib_seq(n):
    seq = []
    for i in range(n):
        n_fib = get_nth_fib(i)
        seq.append(get_nth_fib(i))

    return seq

def main():
    number = input("Which fibonacci number would you like to go up to? ")
    print(get_fib_seq(int(number)))

if __name__ == '__main__':
    main()
