# 영화감독 숌 
num = int(input())
title = 666

  #num이 0이 되는 순간까지.. n번째 시리즈 
while num:
  if '666' in str(title): 
    num-=1 
  
  # num이 0일 때는 증가 x 
  # 찍을 때 -1 해주거나 여기서 걸러내기 
  if num !=0:
    title+=1 


print(title)