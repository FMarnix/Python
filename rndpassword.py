import string
import random

def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercasse + string.digits
    size=8
    return join(random.choice(chars) for x in range(size, 20))

    print(randompassword())
