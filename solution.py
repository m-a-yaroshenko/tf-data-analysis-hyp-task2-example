from scipy.stats import ks_2samp
import pandas as pd
import numpy as np
import scipy.stats as stats


chat_id = 257112106 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, pvalue = ks_2samp(x, y)
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.01
    crit = np.sqrt(-0.5 * np.log(alpha/2) / len(x))
    return True if stat > crit else False # Ваш ответ, True или False
