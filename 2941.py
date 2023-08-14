#크로아티아 알파벳
#=으로 끝나는 경우
#-로 끝나는 경우
#★★★★★ j로 끝나는 경우 ★★★★★
word = input()
ini_count = len(word)
'''
ini_count -= word.count('c=')
ini_count -= word.count('c-')
ini_count -= word.count('dz=')
ini_count -= word.count('d-')
ini_count -= word.count('lj')
ini_count -= word.count('nj')
ini_count -= word.count('s=')
ini_count -= word.count('z=')
'''
for i in ['c=','c-','dz=','d-','lj','nj','s=','z=']:
    ini_count -= word.count(i)    
print(ini_count)