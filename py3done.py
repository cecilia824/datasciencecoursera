# 命令 cd 目標資料夾-->打開py3.py #
import re
#要使用regular expression#
file123 = open('actual.txt')
#打開file#
count = 0
#因為要算總合先設一個變數#
for line in file123:
#for loop file內的每一行#
    line = line.strip()
    #去掉前後空格#
    x = re.findall('[0-9]+',line)
    #找出每一行內的數字#
    for y in x:
        #for loop找出來後的每一個數字#
        y = int(y)
        #轉化為整數#
        count = y + count
        #計算#
print(count)
#印出結果#
