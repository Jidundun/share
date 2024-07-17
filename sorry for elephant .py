cha = '\033[33m' + "코끼리끼리" + '\033[0m'

def start():
    choice = " "
    while not choice in "YN":
      print(f"{cha}와 대화하기") # 시작멘트
      print("Y = 시작")
      print("N = 종료")
      choice = input("어떻게 하시겠습니까?  [Y/N]").strip().upper()
      # 선택지
    if choice == "Y" :
       page1()
    elif choice == "N" :
       print("종료합니다.")
       quit()


def page1(): 
    print('\033[90m' + "코끼리끼리 : 뿌에에에에에에ㅔ에ㅔ에에ㅔㅔㅔㅔㅔㅇ ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ" + '\033[0m')

    choice = " "
    while not choice in "123" :
       print("어떤 행동을 취하시겠습니까?")
       print("1 = 무슨 일 이야???!?")
       print("2 = 아!! 시끄러워 ㅡㅡ (뭔 일인지 알아본다.)")
       print("3 = 무시한다.")
       choice = input('\033[92m' + "선택해주세요. [1/2/3]" + '\033[0m').strip().upper()
       #선택지
    if choice == "1" :
        page2()
    elif choice == "2" :  
        page2()
    elif choice == "3" :
        print('\033[31m' + "선택지로 다시 돌아갑니다 ^^" + '\033[0m')
        page1()


         
def page2():
    print('\033[90m' + "코끼리끼리 : 우리 무리가 다니는 길에 쓰레기 매립지가 생겨서 요즘 밥을 거기서 먹고있는데 배가 너무 아파!!! 뿌에에엥" + '\033[0m')
    choice = " "
    while not choice in "123":
      print("어떤 행동을 취하시겠습니까?") 
      print("1 = 왜 배가 아파?")
      print("2 = 밥을 왜 거기서 먹어?")
      print("3 = 무시하기")
      choice = input('\033[92m' + "선택해주세요. [1/2/3]" + '\033[0m').strip().upper()
      # 선택지
    if choice == "1" :
       page3_1()
    elif choice == "2" :
       page3_2()
    elif choice == "3" :
       print('\033[31m' + "선택지로 다시 돌아갑니다 ^^" + '\033[0m')
       page2()


def page3_1() :
    print('\033[90m' + "코끼리끼리 : 우리가 왜 배가 아프겠어?" + '\033[0m')
    choice = " "
    while not choice in "12":
      print("어떤 행동을 취하시겠습니까?") 
      print("1 = 우리가 쓰레기를 마구마구 버려서…?")
      print("2 = 내가 어떻게 알아.")
      choice = input('\033[92m' + "선택해주세요.  [1/2]" + '\033[0m').strip().upper()
      # 선택지
    if choice == "1" :
       print('\033[90m' + "코끼리끼리 : 맞아. 너희가 쓰레기를 함부로 버려서 피해를 입게 되었어." + '\033[0m')
       page4()
    elif choice == "2" :
       print('\033[90m' + "코끼리끼리 : 넌 정말 쓰레기구나?" + '\033[0m')
       print('\033[31m' + "선택지로 다시 돌아갑니다 ^^" + '\033[0m')
       page3_1()


def page3_2() :
   print('\033[90m' + "코끼리끼리 : 우리가 왜 거기서 먹었겠어?" + '\033[0m')
   choice = " "
   while not choice in "12" :
      print("어떤 행동을 취하시겠습니까?") 
      print("1 = 너가 다니는 길에 우리와 같은 사람들이 쓰레기 매립지를 만들어서 그런걸까..?")
      print("2 = 내가 어떻게 알아.")
      choice = input('\033[92m' + "선택해주세요.  [1/2]" + '\033[0m').strip().upper()
      # 선택지
   if choice == "1" :
       print('\033[90m' + "코끼리끼리 : 맞아. 너네 때문이야. 너네 때문에 내가 아픈거야!! 뿌에에에엥ㅠㅠㅠㅠㅠ" + '\033[0m')
       page4()
   elif choice == "2" :
       print('\033[90m' + "코끼리끼리 : 넌 정말 쓰레기구나?" + '\033[0m')
       print('\033[31m' + "선택지로 다시 돌아갑니다 ^^" + '\033[0m')
       page3_2()
  
def page4() : 
   choice = " "
   while not choice in "12" :
      print("어떤 행동을 취하시겠습니까?") 
      print("1 = 정말 미안해.. 우리가 도와줄 수 있는게 있을까?")
      print("2 = 결국 쓰레기를 먹은건 너잖아. 그게 왜 우리탓이지?")
      choice = input('\033[92m' + "선택해주세요.  [1/2]" + '\033[0m').strip().upper()
      # 선택지
   if choice == "1" :
       print('\033[33m' + "코끼리끼리 : 캠페인과 분리배출 등 환경 보호 활동을 하며 나를 지켜줄 수 있고 우리 동물들을 생각하며 환경친화적인 정책을 펼치며 도와줄 수 있어!!" + '\033[0m')
       print('\033[33m' + "하지만 가장 중요한건 너희 인간들의 생각이 환경을 위해야 한다고 바뀌어야 된다는 거야!!" + '\033[0m')
       print('\033[94m' + " -happy ending-" + '\033[0m')
   elif choice == "2" :
       print('\033[31m' + " -bad ending-" + '\033[0m')
     
#프로그램 시작
start()

       



