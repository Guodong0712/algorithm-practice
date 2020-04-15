""" 麻国栋  107551952581   edit Distance problem / Levenshtein distance"""
import numpy as np
def editDistance(x , y , len_x , len_y):
    distance_list = np.zeros([len_x , len_y]) # 表

    for i in range(0 , len_x):
        for j in range(0 , len_y):
            if i == 0 :
                distance_list[i][j] = j
            elif j ==0 :
                distance_list[i][j] = i

            else:
                delete = distance_list[i - 1][j] + 1
                insert = distance_list[i][j - 1] + 1
                const = 1
                if x[i - 1] == y[j - 1]:
                    const = 0
                replace = distance_list[i - 1][j - 1] + const
                min_value = min([delete , insert , replace])
                distance_list[i][j] = min_value

    print(distance_list)

if __name__ == '__main__':
    x = 'get' # 字符串的 index 是从 0 开始的
    y = 'greet'

    editDistance(x , y , len(x) + 1 , len(y) + 1)