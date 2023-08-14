N = int(input())
count = 0
ini_save=[]
add = True
for i in range(N):
    ini_save = []
    word = input()
    add = True
    for i in range(len(word)-1):
        if word[i] == word[i+1]:#앞뒤가 같아
            continue
        else:#앞 뒤가 달라
            ini_save.append(word[i])
            #print('ini_save',ini_save)
            if word[i+1] in ini_save:#중복된 철자입니까?
                add = False
                #print('false')
            else:#중복된 철자가아닙니다
                continue
    count += int(add)
    #print('count',count)

print(count)