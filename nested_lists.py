# Given the names and grades for each student in a class of  students
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade
# order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is .
# There are two students with that score: .

def sort_students(names_scores):
    scores = []
    for student in names_scores:
        scores.append(student[1])
    sort_scores = sorted(set(scores))
    second_lowest = sort_scores[1]

    names_second_lowest = []
    for student in names_scores:
        if student[1] == second_lowest:
            names_second_lowest.append(student[0])
    names_second_lowest = sorted(names_second_lowest)

    for name in names_second_lowest:
        print(name)


if __name__ == '__main__':
    names_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names_scores.append([name, score])

    sort_students(names_scores)
