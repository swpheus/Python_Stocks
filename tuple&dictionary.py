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

naver_closing_price=[474500, 461500, 501000, 500500, 488500]

print(naver_closing_price)

max_price = max(naver_closing_price)
print(max_price)

min_price=min(naver_closing_price)
print("가격차:",max_price-min_price)

print("수요일 종가:",naver_closing_price[2])

naver_closing_price2={'09/07':474500, '09/08':461500, '09/09':501000, '09/10': 500500, '09/11':488500}
print(naver_closing_price2)
print("9월9일 가격",naver_closing_price2['09/09'])

day1=10000
day2=13000
(day1-day2) ==(day1*0.3)
