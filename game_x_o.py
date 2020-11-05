import sys
def show(list_):
  print(list_[0:3])
  print(list_[3:6])
  print(list_[6:9])

def winner(list_, player):
  for i in list(finish):
      k=0
      for j in i:
        if j in list_:
          k=k+1
          if k==3:
              print("You win "  + str(player) + "!!!")
              sys.exit()


def player(list_,char,player1):
  print(player1+"\n")
  str5 = input(char  + ":")
  if str5.isalnum()==False or str5.isalpha() or len(str5)>1 or int(str5) > 8:
   print("please write is one number")
  else:
    list_.append(str5)
    str3[int(str5)] = char
    list_.sort()
    show(str3)
    winner(list_,player1)
   

player1=[]
player2=[] 
finish=[['0','1','2'],['3','4','5'],['6','7','8'],['0','4','8'],['2','4','6'],['0','3','6'],['1','4','7'],['2','5','8']]
str3 = ["-","-","-","-","-","-","-","-","-"]
print(finish)
while True:
  player(player1,"x","player1")
  player(player2,"o","player2")
  if len(player1)==5:
      print("Game over, no winner!!!")
      sys.exit()
    


