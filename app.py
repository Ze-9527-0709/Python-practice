def count_up_to(max):
    count = 1
    while count < max:
        yield count
        count += 1


counter = count_up_to(3)

# type(counter)  # <class 'generator'>
for number in counter:
    print(number)


# def main():
#     max_count = int(input("Enter a number to count up to: "))
#     for number in count_up_to(max_count):
#         print(number)


# if __name__ == "__main__":
#     main()
