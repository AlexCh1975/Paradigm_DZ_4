"""
Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами). Можете
использовать любую парадигму, но рекомендую использовать
функциональную, т.к. в этом примере она значительно
упростит вам жизнь.

"""
import statistics
from math import sqrt
from math import pow

def calc_correlation(x, y):
    def calc_average_value(nums):
        return sum(map(lambda n: n, nums)) / len(nums)
    
    average_x = calc_average_value(x)
    average_y = calc_average_value(y)
    
    def calc_numerator(x, y):
        sum = 0
        for i, j in zip(x, y):
            sum += (i - average_x) * (j - average_y)
        return sum
    
    def calc_denominator(x, y):
        sum1 = 0
        sum2 = 0
        for i, j in zip(x, y):
            sum1 += pow((i - average_x), 2)
            sum2 += pow((j - average_y), 2)
        return sqrt(sum1 * sum2)

    return calc_numerator(x, y) / calc_denominator(x, y)


x = [1, 4, 8, 2]
y = [9, 2, 8, 3]
# x = [9, 2, 8, 3]
# y = [1, 4]
# x = [1, 4]
print(f'r(x,y)= {calc_correlation(x, y)}')

print(statistics.correlation(x, y))