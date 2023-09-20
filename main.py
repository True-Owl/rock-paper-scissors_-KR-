import time, random, sys


def hgj (sentence, timesl):
    """
    sentence = 출력할 문자, timesl = 글자가 출력되는 시간간격(단위:초)
    """
    for i in range(len(sentence)):
        print(sentence[i], end="")
        time.sleep(timesl)
    print('\n')

def PrintScore():
    print(f'AI:{score_ai} / player:{score_player}')


ai = ['AI: 가위!','AI: 바위!', 'AI: 보자기!']
score_ai = 0
score_player = 0
while 1:
    cho = random.choice(ai)

    hgj('\n가위 / 바위 / 보자기 중에서 선택해주세요. (나가기는 아무 문자나 입력)\n',0.02)
    player = input('player: ')
    hgj(cho,0.03)


    if player == '가위':
        if cho == 'AI: 가위!':
            
            hgj('무승부!',0.03)
            score_ai += 1
            score_player += 1
            PrintScore()
        
        elif cho == 'AI: 바위!':
            
            hgj('AI이(가) 승리하였습니다.',0.03)
            score_ai += 1
            PrintScore()

        else:
            
            hgj('player이(가) 승리하였습니다.',0.03)
            score_player += 1
            PrintScore()

    elif player == '바위':

        if cho == 'AI: 가위!':
            
            hgj('player이(가) 승리하였습니다.',0.03)
            score_player += 1
            PrintScore()
        
        elif cho == 'AI: 바위!':
            hgj('무승부!',0.03)
            
            score_ai += 1
            score_player += 1
            PrintScore()

        else:
            
            hgj('AI이(가) 승리하였습니다.',0.03)
            score_ai += 1
            PrintScore()

    elif player == '보자기':

        if cho == 'AI: 가위!':
            
            hgj('AI이(가) 승리하였습니다.',0.03)
            score_ai += 1
            PrintScore()
        
        elif cho == 'AI: 바위!':
            
            hgj('player이(가) 승리하였습니다.',0.03)
            score_player += 1
            PrintScore()

        else:
            hgj('무승부!',0.03)
            
            score_ai += 1
            score_player += 1
            PrintScore()

    else:
        hgj('잘못된 입력입니다!\n프로그램을 종료합니다.\n\n다시 시작해주세요.',0.02)
        PrintScore()
        sys.exit()