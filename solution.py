import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha=0.01
    statistic, pvalue = ks_2samp(x, y)
    critical_value = np.sqrt((-1/2)*np.log(alpha/2)/(len(x)+len(y)))
    return True if statistic > critical_value else False # Ваш ответ, True или False
