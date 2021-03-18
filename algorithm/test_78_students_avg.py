#백준 평균을 넘겠지 https://www.acmicpc.net/problem/4344

case = int(input())
for i in range(case):
  student_score = list(map(int,input().split()))
  all_avg = sum(student_score[1:])/student_score[0]
  count =0

  for s in range(1,len(student_score)):
    if student_score[s]>all_avg:
      count+=1
  ok_avg = count/student_score[0]*100
  print('{:.3f}%'.format(ok_avg))
  