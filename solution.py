# 다음(Daum)의 주가가 89,000원이고 네이버(Naver)의 주가가 751,000원이라고 가정하고, 어떤 사람이 다음 주식 100주와 네이버 주식 20주를 가지고 있을 때 그 사람이 가지고 있는 주식의 총액을
# 계산하는 프로그램을 작성하세요.

daum = 89000
naver = 751000

total = daum * 100 + naver * 20

print(total)

# 문제 2-1에서 구한 주식 총액에서 다음과 네이버의 주가가 각각 5%, 10% 하락한 경우에
# 손실액을 구하는 프로그램을 작성하세요.

loss = (daum * 0.05 * 100) + (naver * 0.1 * 20)
print(loss)

# 우리나라는 섭씨 온도를 사용하는 반면 미국과 유럽은 화씨 온도를 주로 사용합니다. 화씨 온도(F)를
# 섭씨 온도(C)로 변환할 때는 다음과 같은 공식을 사용합니다. 이 공식을 사용해 화씨 온도가 50일 때의 섭씨 온도를 계산해 보세요.
f = 50
c = (f - 32) / 1.8
print(c)

print("pizza\n"*10)
