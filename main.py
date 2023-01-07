questions = [
  ["which language was used to create fb", "PHP", "JS", "Chinese", "None", 1],
  ["which language was used to create fb", "PHP", "JS", "Chinese", "None", 1],
  ["which language was used to create fb", "PHP", "JS", "Chinese", "None", 1],
  ["which language was used to create fb", "PHP", "JS", "Chinese", "None", 1],
  ["which language was used to create fb", "PHP", "JS", "Chinese", "None", 1],
  ["which language was used to create fb", "PHP", "JS", "Chinese", "None", 1],
  ["which language was used to create fb", "PHP", "JS", "Chinese", "None", 1],
  ["which language was used to create fb", "PHP", "JS", "Chinese", "None", 1]
]

levels = [1000, 3000, 6000, 10000, 20000, 30000, 40000, 60000, 1000000]
for i in range(0, len(questions)):
  question = questions[i]
  print(f"Question for Rs {levels[i]} ")
  print(f"a.{question[1]}   b.{question[2]}")
  print(f"c.{question[3]}   d.{question[4]}")
  # print(question[1])
  reply = int(input("enter your answer from 1-4 "))
  if (reply == question[-1]):
    print(f"Correct answer you have won Rs{levels[i]}")
    money = 0
    if (i == 4):
      money = 10000
    elif (i == 7):
      money = 30000
  else:
    print("wrong answer")
    break
print(f"you collected {money} ")
