import string
import random

def create_pwd(pass_len):
    res = [string.punctuation, string.ascii_letters, string.digits]
    ans = ''

    for i in range(pass_len):

        ans += random.choice(res[random.randint(0, 2)])

        # ans += (random.choice(string.ascii_letters))
        # if i % 2 == 0:
        #     lst.append(random.choice(string.punctuation))
        # else:
        #     lst.append(random.choice(string.digits))

    return ans

"""print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)"""

n = int(input("Tanid heden orontoi nuuts ug heregtei we: "))

print(create_pwd(n))
