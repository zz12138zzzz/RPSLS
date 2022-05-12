import random
def name_to_number(name):
 if name=='石头':
    number=0
 elif name=='史波克':
    number=1
 elif name=='布':
    number=2
 elif name=='蜥蜴':
    number=3
 elif name=='剪刀':
    number=4
 return number
def number_to_name(number):
  if number==0:
      name='石头'
  elif number==1:
      name='史波克'
  elif number==2:
      name='布'
  elif number==3:
      name='蜥蜴'
  else:
      name='剪刀'
  return name
def rpsls(player_choice):
    comp_number=random.randint(0,4)
    computer_choice = number_to_name(comp_number)
    print("计算机的选择为：%s" % computer_choice)
    player_choice_number=name_to_number(player_choice)
    if player_choice_number==comp_number:
      print("您和计算机出的一样呢")
    elif player_choice_number-comp_number==1 or player_choice_number-comp_number==2:
      print("您赢了")
    elif comp_number==3 and player_choice_number==0:
      print("您赢了")
    elif comp_number==4 and player_choice_number==0:
      print("您赢了")
    elif comp_number==4 and player_choice_number==1:
      print("您赢了")
    else:
      print("计算机赢了")
    return
print("欢迎使用RPSLS游戏")
player_choice=input("请输入您的选择：")
if player_choice=='石头' or player_choice=='剪刀' or player_choice=='史波克' or player_choice=='布' or player_choice=='蜥蜴':
 print("------------")
 print("您的选择为：%s" % player_choice)
 rpsls(player_choice)
else:
 print('Error: No Correct Name')




