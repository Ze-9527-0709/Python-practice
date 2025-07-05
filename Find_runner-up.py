# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score.
# You are given  scores. Store them in a list and find the score of the runner-up.

# Input Format

# The first line contains .
# The second line contains an array   of  integers each separated by a space.

# Constraints

# 2 <= n <= 10
# -100 <= arr[i] <= 100

def runner_up(array_students):
    array_students = list(array_students)  # Remove duplicates
    array_students.sort(reverse=True)  # Sort the list
    for score in range(len(array_students)):
        if array_students[score] != array_students[score + 1]:
            runner_up = array_students[score + 1]
            break
        else:
            continue
    print(runner_up)


if __name__ == "__main__":
    n = int(input("Enter the number of students: "))
    arr = list(map(int, input("Enter the scores separated by space: ").split()))
    runner_up(arr)
