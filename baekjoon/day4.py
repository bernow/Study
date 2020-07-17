# Separator 옵션 사용
print('T', 'E', 'S', 'T', sep='')
print('2019', '12', '08', sep='-')
print('dbthd6', 'naver.com', sep='@')

# end 옵션 사용
print('Welcome To', end=' ')
print('the black paradise', end=' ')
print('piano notes')

# format 사용 [], {}, ()
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me'))
print("{a} are {b}".format(a='You', b='Me'))