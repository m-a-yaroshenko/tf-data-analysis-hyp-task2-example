import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    statistic, critical_values, pvalue = anderson_ksamp([x, y])
    alpha = 0.01
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return True if statistic > critical_values[2] else False # Ваш ответ, True или False
