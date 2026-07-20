# Author = Kiran
# Date = 20th July, 2026
"""

"""
count= 0
with open("03_practice.txt", "r") as f:
    data = f.read()
    print(data)

    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]

# Another method
    nums = data.split(",")
    for val in nums:
        if(int(val)%2 == 0):
            count += 1


print(count)