'''
BMI值計算公式:    BMI = 體重(公斤) / 身高2(公尺2)
例如：一個52公斤的人，身高是155公分，則BMI為 :
52(公斤)/1.552 ( 公尺2 )= 21.6
體重正常範圍為  BMI=18.5～24
'''
height = int(input('請輸入身高(cm):'))
weight = int(input('請輸入體重(kg):'))
bmi = weight / pow((height / 100), 2)
print('你的BMI為:', bmi) 
if bmi < 18:
    print('過輕')
elif bmi >= 18.5 and bmi < 24:
    print('正常')
elif bmi >= 24 and bmi < 27:
    print('過重')
elif bmi >= 27 and bmi < 30:
    print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('中度肥胖')  
elif bmi >= 35:
    print('重度肥胖')          
    