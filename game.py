import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input("Угадай число:"))
    if predict_number > number:
        print("ваше число больше")
    elif predict_number < number:
        print("ваше число меньше")
    else:
        print(f"вы угадали число за {count} попыток")
        break