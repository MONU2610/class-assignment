def find_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first two-digit number: "))
num2 = int(input("Enter the second two-digit number: "))

if 10 <= num1 <= 99 and 10 <= num2 <= 99:
    hcf_result = find_hcf(num1, num2)
    print(f"The HCF of {num1} and {num2} is: {hcf_result}")
else:
    print("Please enter valid two-digit numbers.")