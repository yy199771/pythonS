#coding:utf-8

#年限
year = 0
#年化利率
interestRate = 0
#起初金额
initialAmounti = 0
#追加金额
additionalAmount = 0
#总金额
sum = 0

#普通复利计算公式 #追加复利计算公式

def additionalInteres(initialAmounti,additionalAmount,interestRate,year):
    #additionalAmount：普通复利与追加复利的区别：0：表示普通复利，非0：表示追加复利。
    if additionalAmount is None:
        for i in range(year):
            sum = initialAmounti * (1 + interestRate) ** (i+1)
            print '第{0}年末本金加利息一共：{1}'.format(i+1,sum)
    else:
        for i in range(year):
            if i == 0:
                sum = initialAmounti * (1 + interestRate)
                print '第%i年末本金加利息一共：%f' %(i+1,sum)
            elif 0 < i < 8:
                sum = (sum + additionalAmount) * (1 + interestRate)
                print '第%i年末本金加利息一共：%f' %(i+1,sum)
            else:
                sum = sum * (1 + interestRate)
                print  '第%i年末本金加利息一共：%f' %(i+1,sum)


additionalInteres(100000,10000,0.088,25)
