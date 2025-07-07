# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Sucessful")
#         break
# else:
#     print("Failed")
count = 0
for i in range(1, 10):
    if i % 2 == 0:
        count += 1
        print(i)
else:
    print(f"We have {count} even numbers")
