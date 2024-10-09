import random
number = random.randint(3, 20)
def password(num):
    pass_ = ''
    for i in range(1, num):
        for j in range(i + 1, num):
            if num % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_
print('Выпавшее число на камне:', number)
print('Пароль:', password(number))