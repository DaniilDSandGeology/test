import numpy as np

def random_predict(number: int=1) -> int:
    """_summary_

    Args:
        number (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """
    
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
        
    return count
    
# print(f"угадали число за {random_predict()} попыток")

def score_game(random_predict) -> int:
    """_summary_

    Args:
        random_predict (_type_): _description_

    Returns:
        int: _description_
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    print(f"ващ алшгоритм в средне  угдадыает число за {score} попыток")
    return (score)


if __name__ == '__main__':
    score_game(random_predict)
    
    