# main_script.py
import fibonacci_module

def main():
    n = 100  # Number of Fibonacci numbers to generate
    fibonacci_numbers = fibonacci_module.generate_fibonacci_numbers(n)

    print("First {} Fibonacci numbers:".format(n))
    for number in fibonacci_numbers:
        print(number)

if __name__ == "__main__":
    main()
