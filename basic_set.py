evens = {0, 2, 4, 6, 8, 10 }    # 짝수 집합
odds = {1, 3, 5, 7, 9}  # 홀수 집합
numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} # 전체 집합
mthree = {0, 3, 6, 9 }  # 3의 배수 집합

def define_set():
    """
    집홥 정의 연습
    SET:- 순서가 없고(그래서 인덱싱, 슬라이싱 없음), 중복을 허용하지 않는다
        - len, in, not in만 사용가능
    """
    empty = set()   # 빈 set
    print(type(empty), type({}))

    # 길이와 포함 여부는 확인 가능
    print(numbers, "LENGTH:",len(numbers))
    print(2 in numbers, 2 in evens, 2 in odds, 2 in mthree)

    # 다른 순차형으로 set 만들기
    s = "Python Programming"
    chars = set(s.upper())
    print(s, chars)
    # 결과값 {'A', 'N', 'M', 'T', ' ', 'H', 'P', 'O', 'R', 'I', 'Y', 'G'}
    # 순서가 없고 중복을 허용 안하기 때문에 이러한 결과값이 나온다

    # list 등 순차 자료형의 중복값을 제거할 때 유용
    lst = "Python Programming Java Programming HTML Programming".split()
    print("lst:", lst)
    s = set(lst)
    print("set:", s, len(s))

    # list에서 중복 요소를 제거한 요소 갯수는?
    lst2 = list(s)
    print("lst2:", lst2)

def set_methods():
    """
    SET의 메서드들
    """
    print("numbers:", numbers, len(numbers))
    numbers.add(10)
    print("numbers:", numbers, len(numbers))
    numbers.add(10) # 중복을 허용하지 않는 자료형
    print("numbers:", numbers, len(numbers))

    print("evens:", evens)
    evens.add(3)    # 추가
    print("evens:", evens)
    evens.discard(3)    # 3 삭제
    print("evens:", evens)
    evens.discard(3)
    print("evens:", evens)
    # 삭제할 3이 없어도 discard는 오류 없이 출력해낸다
    if 3 in evens:
        evens.remove(3) # remove는 삭제할 데이터가 없으면 KeyError가 난다
        print("evens:", evens)

    evens.update({10})
    print("evens:", evens)

def set_oper():
    """
    SET의 집합 연산
    """
    numbers.add(10)
    print(numbers)
    print(evens, odds)

    # 합집합: | , union
    print(evens | odds == numbers)  # 짝수 집합 합집합 홀수 집합 == 전체집합
    print(evens.union(odds) == numbers)

    # 교집합: & , intersection
    print(evens & mthree == {0, 6})
    print(evens.intersection(mthree) == {0, 6})

    # 차집합: - , difference
    print(numbers - odds == evens)
    print(numbers.difference(evens) == odds)

    # 판별 함수
    print(numbers.issuperset(evens), numbers.issuperset(odds))  # 부모 집합 여부 판별
    print(evens.issubset(numbers), odds.issubset(numbers))  # 부분 집합 여부 판별

def loop():
    for num in numbers: # for () in 순차자료형 -> 이런 순서가 공식
        print(num, end="\t")
    else:
        print()


if __name__ == "__main__":
    # define_set()
    # set_methods()
    # set_oper()
    loop()