import numpy as np
def optimalBST(n , p):
    C = np.zeros([n + 2 , n + 1], np.float64) # 最优值
    R = np.zeros([n + 2 , n + 1], np.int)# 最优解
    for i in range(1 , n + 1):
        C[i][i-1] = 0
        C[i][i] = p[i]
        R[i][i] = i

    C[n+1][n] = 0

    for d in range(n): # 表示 i 与 j 相隔的距离
        # 下面的循环就是说，同一个距离，能有多少种可能，分别计算这些可能
        '''
        第二重循环的分析：
        1、当 d = 1 ， 也就是 i 与 j 距离 1 时，根据笔算，我们会有 3 种可能，
        其中 3 = 4 - 1 那么 i 由 1 ~ 3
        2、当 d = 2 ， 也就是 i 与 j 距离 2 时，根据笔算，我们会有 3 种可能，
        其中 2 = 4 - 2 那么 i 有 1 ~ 2
        同理，即可得到第二重循环的变换，对应的就是 i 在相应 d 的变化
        '''
        for i in range(1 , n-d + 1):
            j = i + d
            min_num = 100000000
            mink = i
            sum = 0
            '''
            第三重循环的分析：
            有第一 、 二 重循环，我们得到了 i 和 j 的取值，所以，在第三重循环中，
            我们只要根据公式求解出对应的 k 就好，在结束第二重循环后，填表就好。
            '''
            for k in range(i , j + 1):
                sum += p[k]
                if C[i][k - 1] + C[k +1][j] < min_num:
                    min_num = C[i][k - 1] + C[k+1][j]
                    mink = k

            C[i][j] = min_num + sum # 将找到的最优值填表
            R[i][j] = mink # 将找到的最优解填表
    return C , R

def main(n , p):
    return optimalBST(n , p)

if __name__ == '__main__':
    n = 4
    p = [0 , 0.1 , 0.2 , 0.4 , 0.3]
    C , R = main(n , p)
    print(C)
    print(R)