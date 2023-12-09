def happy_new_year():
    count_down=10
    while count_down >=1:
        print(count_down)
        count_down-=1
    print("Happy New Year!")

def square_integers(numbers):
    squared_list = [num ** 2 for num in numbers if isinstance(num, int)]
    return squared_list

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

