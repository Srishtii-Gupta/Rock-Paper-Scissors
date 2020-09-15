import random

draws=0;
wins=0;
losses=0;
is_ended=False
prompt= "Choose Rock(r), Paper(p), Scissors(s), or 'q' to quit:"
while True:
    user_choice=input(prompt)
    while user_choice not in ['r','p','s','q']:
        user_choice=input(prompt)
    if user_choice=='q':
        break
    else:
       computer_choice=random.choice(['r','p','s'])
       if computer_choice=='r':
        move='rock'
       elif computer_choice=='p':
        move='paper'
       else:
        move='scissors'
       print('Computer_choice gives a '+move)
       if computer_choice==user_choice:
           print('Draw')
           draws=draws+1
       elif(computer_choice=='r' and user_choice=='p') or \
           (computer_choice=='p' and user_choice=='s') or \
           (computer_choice=='s' and user_choice=='r'):
          print('You win')
          wins+=1
       else:
           print('You lose')
           losses+=1
print('you have '+str(wins)+ 'wins ' +str(draws)+'draws '+ str(losses)+ 'losses')