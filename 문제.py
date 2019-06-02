import random
que_li=[]
ans_li={}
while True:
    que=input('문제를 입력해주세요 ')
    if que=='stop':
        break
    else:
        ans=input('답을 입력해주세요 ')
        que_li.append(que)
        ans_li[que]=ans
        print('추가한 문제:', len(que_li), '개\n')
        continue
random.shuffle(que_li)
try:
    howmuch=int(input('\n몇 개의 문제를 선택할까요? '))
except:
    print('\n올바른 값을 입력해주세요')
    exit()
score=0
if howmuch<=len(que_li):
    for i in range(0, howmuch):
        act_que=que_li[i]
        act_ans=ans_li[act_que]
        print('\n', act_que)
        answer=input('답? ')
        if answer == act_ans:
            print('정답')
            score=score+1
        else:
            print('오답')
    print('\n당신의 점수는', score, '점 입니다.')
else:
    print('\n문제 수보다 많은 문제를 낼 수 없습니다.')

