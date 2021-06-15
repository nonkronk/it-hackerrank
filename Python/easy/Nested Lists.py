"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

Example
records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
The ordered list of scores is [20.0, 50.0], so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

alpha
beta
Input Format

The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output 0

Berry
Harry
Explanation 0

There are 5 students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""





def list_lowsecgrade(sorted_list):
    fs_grade = sorted_list[0][1]
    secgrade_list = []
    for i in range(len(sorted_list)):
        if sorted_list[i][1] > fs_grade:
            j = i + 1
            secgrade_list.append(sorted_list[i])
            for j in range(j, len(sorted_list)):
                if sorted_list[j][1] == secgrade_list[0][1]:
                    secgrade_list.append(sorted_list[j])
                else:
                    break
            break
    return secgrade_list

if __name__ == '__main__':
    grade_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade_list.append([name, score])
    grade_list.sort(key=lambda x:x[1]) # Sort ASC by grade
    lowsecgrade_list = list_lowsecgrade(grade_list)
    lowsecgrade_list.sort(key=lambda x: x[0])  # Sort ASC by name
    for i in lowsecgrade_list:
        print(i[0])

"""

While the pythonic answer could be:

n = int(input())
marksheet = [[[input()], float(input())] for _ in range(n)]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))

"""