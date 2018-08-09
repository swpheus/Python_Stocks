#tuple
t=('samsung','LG',"SK")
print(t)
print(t[0:2])
#dictionary
cur_price={"Daum KAKAO":80000,"naver":60000,"daeshin":300000}
print(cur_price)
#삭제
del cur_price['daeshin']
print(cur_price)
print(cur_price.keys())
print(cur_price.values())

#항상 변수를 통해 바인딩하는 편이좋다

socks_list=list(cur_price.values())

print(socks_list)

print('samsung' in cur_price.keys())

print('naver' in cur_price.keys())

