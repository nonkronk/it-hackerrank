/*
Higher Than 75 Marks
https://www.hackerrank.com/challenges/more-than-75-marks/problem

Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

Input Format

The STUDENTS table is described as follows:  The Name column only contains uppercase (A-Z) and lowercase (a-z) letters.

Sample Input

ID Name Marks
1 Ashley 81
2 Samantha 75
4 Julia 76
3 Belve 84

Sample Output

Ashley
Julia
Belvet
Explanation

Only Ashley, Julia, and Belvet have Marks > 75. If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.
*/

SELECT Name FROM STUDENTS
WHERE Marks > 75
ORDER BY RIGHT(Name,3), ID;