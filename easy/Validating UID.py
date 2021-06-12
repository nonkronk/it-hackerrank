"""
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least 2 uppercase English alphabet characters.
It must contain at least 3 digits (0 - 9).
It should only contain alphanumeric characters (a - z, A - Z & 0 - 9).
No character should repeat.
There must be exactly 10 characters in a valid UID.
Input Format

The first line contains an integer T, the number of test cases.
The next T lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354: 1 is repeating → Invalid
B1CDEF2354: Valid
"""

# Check UID valid or invalid
def check_uid(uid):
    # Count numeric char
    numbers = sum(c.isdigit() for c in uid)
    # Count upper char
    upper_chars = sum(c.isupper() for c in uid)
    if numbers < 3:
        return False
    elif upper_chars < 2:
        return False
    # Check UID length
    elif len(uid) != 10:
        return False
    # Check is UID alphanum
    elif uid.isalnum() == False:
        return False
    else:
        # Check repeated char
        for char in uid:
            if uid.count(char) > 1:
                return False
    return True
    # 

if __name__ == "__main__":
    for i in range(int(input())):
        uid = input()
        if check_uid(uid):
            print("Valid")
        else:
            print("Invalid")
