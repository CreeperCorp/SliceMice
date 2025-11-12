import random

finalList = []
yourList = []
nonList = ""
ifContinue = 'yes'

while ifContinue == 'yes':
  yourList.append(input("What word do you want to add to your list?: "))
  ifContinue = input("Do you want to add anymore words to the list?(yes/no): ")


def mySlice(yourList, index1, index2):
    for item in range (index1, index2):
        finalList.append(yourList[item])
    return finalList

nonList = "".join(yourList)
maxLength = len(nonList)
randomLength = random.randint(3, maxLength)
startIndex = random.randint(0, maxLength - randomLength)
nonNonList = random.shuffle(nonList)
slicedWord = nonList[startIndex : startIndex + randomLength]
print(f"Word to create: {slicedWord}")
while slicedWord != finalList:
  startingIndex = int(input("What will be the starting index?(integer): "))
  endingIndex = int(input("What will be the ending index?(integer): "))
  print(mySlice(yourList, startingIndex, endingIndex))
  ifGiveUp = input("Do you give up?(yes/no): ")
  if (ifGiveUp == 'yes'):
    print("Ok")
    

random_substring = original_string[start_index : start_index + random_length]
print(random_substring)
