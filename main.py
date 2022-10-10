# Get values and store in both lists
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

# Compare strings to see if num2 is a substring of num1
i = 0
j = 0
isSubstring = False
for i in range(len(num2)):
    for j in range(len(num1)):
        if num2[i] == num1[j]:
            isSubstring = True

# Print true or false
if isSubstring == True:
    print("True")
else:
    print("False")