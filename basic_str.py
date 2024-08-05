import sys

import sympy


def define_str():
    """

    :return:
    """
    # 문자열의 정의
    # 한 줄 문자열: 쌍따옴표("),홑따옴표(') 모두 가능하다
    s1 = "Hello Python"     # 리터럴 생성
    s2 = str("Hello Python")    # 타입 함수 사용
    s3 = str(3.14159)   # 다른 타입을 변환하여 생성

    print(s1, type(s3))
    print(s2, type(s2))
    print(s3, type(s3))

    print("s1은 str?", isinstance(s1, str))
    print("s2는 str?", isinstance(s2, str))
    print("s3는 str?", isinstance(s3, str))

    # 여러 줄 문자열: """, '''
    s4 = """Life is too short, You need Python.
    파이썬은 데이터 처리가 중요한 시대에서 
    가장 널리 사용되는 언어입니다"""

    print(s4)

    # 여러 줄 문자열은 한 줄 주석만 있는 파이썬에서
    # 여러 줄 주석을 사용하고자 할 때도 사용할 수 있다
    """여러 줄 문자열을 사용한 여러 줄 주석
    메서드 정의 바로 아래 여러 줄 주석을 추가하면
    문서화 하 때 이용될 수 있고
    help 명령어로 해당 메서드의 주석을 볼 수 있다.
    docstring이라 한다."""

    # f-string : 문자열 포맷팅 방식 중 하나
    name, age = "홍길동", 28
    message = f"안녕하세요, {name}님. 당신은 {age}살 입니다."
    print(message)

    width, height = 10, 5
    message = f"사각형의 면적은 {width * height} 입니다."
    print(message)

def string_oper():
    """
    문자열 연산
    """
    str1 = "First String"
    str2 = "Second String"
    # 기존 객체의 이름을 쓰면 오류가 나니까 조심!
    # len(), 인덱싱 가능, 슬라이싱 가능, 포함여부 판별,
    # immutable이기 때문에 치환이 불가능하다

    # 문자열 객체는 길이(len())를 잡을 수 있다
    print(len(str1), len(str2))

    # 인덱싱 가능
    # 1.정방향 인덱싱
    print(str1[0], str1[1], str1[2], "...", str1[9], str1[10], str1[11])
    # 2.역방행 인덱싱
    print(str1[-12], str1[-11], str1[10],"...", str1[-3], str1[-2], str1[-1])

    # 문자열은 immutable -> 치환 불가
    # str1[0] = "f" # 'str' object does not support item assignment 변경 불가

    # 슬라이싱
    str1 = "First String"
    # [시작경계:끝경계(:콜론은 간격)]
    print(str1)
    print(str1[6:9])
    print(str1[2:5])
    print(str1[-6:-3])
    print(str1[-10:-7])

    print(str1[0:5])
    print(str1[:5]) # 시작부터 인덱스를 잡으면 생략가능

    print(str1[6:len(str1)])
    print(str1[6:]) # 끝까지 인덱스를 잡으면 이것도 생략가능

    print(str1[::2])    # 처음부터 끝까지 간격 2를 준다
    print(str1[::-1])   # 간격 값이 음수이면 역방향이다
    print(str1[::-2])

def search_methods():
    """
    문자열 검색 관련 예제
    """
    s = "I Like Python, I Like JAVA Also"
    # Like을 찾아봅시다 : index
    print("1st Index:", s.index("Like"))
    print("2nd Index:", s.index("Like",6))
    print("3rd Index:", s.index("Like", 21))

    # 역방향 검색
    print("RFIND:", s.rfind("Like"))    # 17
    print("RFIND:", s.rfind("Like",0,17))

    # 문자열이 특정 문자열로 시작되는가?
    url = "http://www.naver.com"
    surl = "https://www.google.com"
    ftp = "ftp://ftp.naver.com"

    print("STARTSWITH:", url.startswith("http://"))
    print("STARTSWITH:", surl.startswith("https://"))
    print("STARTSWITH:", ftp.startswith("http://", "https://")) #검색 대상ㅇ디 여러개


    # 문자열이 특정 문자열로 끝나는가?
    print("ENDSWITH:", url.endswith("naver.com"))
    print("ENDSWITH:", surl.endswith("naver.com"))

    # startswith, endswith에서 검색 범위를 제한
    print("STARTSWITH:", ftp.startswith("ftp.", 6,len(ftp)))
    # 보통 끝자리를 len(20) 이렇게 넣어버리는데 그러면 안됨 ftp를 넣어줘야 나중에 ftp값이 바뀌어도 안달라진다

def modify_replace_methods():
    """
    문자열 수정, 치환 관련 메서드 연습
    """
    s = "          Alice and the Heart Queen          "
    print("STRIP:[", s.strip(),"]", sep="")
    print("LSTRIP:[", s.lstrip(),"]", sep="")
    print("RSTRIP:[", s.rstrip(),"]", sep="")

    s = "----------Alice and the Heart Queen-----------"
    print("STRIP -:[", s.strip("-"), "]", sep="")

    s = "I Like Java"
    # Java -> Python 치환 (치환한다고해서 내부데이터가 변경된것은 아니기에 필요하면 재할당해줘야함)
    print("REPLACE:", s.replace("Java","Python"))
    print("원본:", s) # str은 immutable이기에 변경되지 않는다

def align_method():
    """
    문자열 정렬 관련 메서드
    """
    s = "Alice and the Heart Queen"
    print("CENTER:[", s.center(60),"]", sep="")
    print("CENTER:[", s.center(60,"^"), "]", sep="")
    print("LJUST:[", s.ljust(60,"#"),"]", sep="")
    print("RJUST:[", s.rjust(60,"!"),"]", sep="")

    print("ZFILL:", "1234".zfill(5))    #5자리 확보, 내용을 채운 후 빈 공간에 0을 채춤
    print("ZFILL:", "123456".zfill(5))  #확보한 5자리는 최소 공간, 넘쳐도 잘리지는 않음

def split_join_method():
    """
    문자열 분할과 합치기 관련 메서드
    """
    s = "Ham and Cheese and Breads and Ketchup"
    print("SPLIT:", s.split())  # 공백 문자를 기준으로 분리

    ingr = s.split(" and ")     # "공백and공백"을 기준으로 분리
    print("SPILT:", ingr)
    print("JOIN:", ",".join(ingr))  # ingr리스트를 콤마(,)를 중심으로 합침

    print(s.split(" and ", 2))  # 앞에서 2개만 분리
    print(s.rsplit(" and ", 2)) # 뒤에서 2개만 분리

    # 줄 단위 구분 : split("\n")과 동일하다

    lines ="""\
    Java Programming
    Python Programming
    HTML Coding
    """
    print("split:", lines.split())
    print("split:", lines.split("\n"))

    print("splitlines:", lines.splitlines(True)) # 개행문자 유지
    print("splitliens:", lines.splitlines(False)) # 개행문자 유지안함

def check_methods():
    """
    str 데이터의 형태 판별
    """
    print('1234'.isdigit())     # 숫자 형태?
    print('abcd'.isalpha())     # 알파벳 형태?
    print("python3".isalnum())  # 숫자+알파벳 형태?
    print("python 3".isalnum()) # 공백포함되어있어서 False
    print(" \r\n\t".isspace())  # 공백문자 형태? 공백문자(스페이스, 탭, 개행문자 등)
    print("".isspace())         # 공백이 없어서 False

    print("PYTHON".isupper())   # 대문자인가?
    print("python".islower())   # 소문자인가?
    print("Python Programmong".istitle())   # 신문형태기사제목같은 형태인가?


def string_format():
    """
    문자열 포맷팅 연습
    """
    # C 스타일 문자열 포맷
    # %s, %c, %d, %f, %x, %o, %%(%자체를 출력하고자 할때)
    fmt = "%d개의 %s 중에서 %d개를 먹었다"
    print(fmt %(10,"사과",3))

    print("현재 이자율은 %f%%입니다." % 3.4)
    print("현재 이자율은 %.2f%%입니다." %3.4)

    # named formating(이름을 붙여주는 것)
    fmt = "%(total)d개의 %(fruit)s 중에서 %(eat)d개를 먹었다"
    print(fmt % {"total":10, "fruit": "사과", "eat": 3})
    print(fmt % {"fruit": "사과", "eat": 3, "total": 10})

    # format 메서드
    fmt = "{}개의 {} 중에서 {}개를 먹었다"
    print(fmt.format(10, "사과", 3))
    print("{0}개의 {1} 중에서 {2}개를 먹었다".format(10,"사과", 3))

    # placeholder의 named parameter를 이용
    fmt = "{total}개의 {fruit} 중에서 {eat}개를 먹었다"
    print(fmt.format(eat=3, total=10, fruit="바나나"))

    # dict 작성된 데이터가 있을 경우
    data = {"total": 10, "eat": 3, "fruit": "메론"}
    print(fmt.format_map(data))

    # f-string
    # 포맷팅 문자열 앞에 f
    # {} 내부에 데이터, 변수명, 표현식 -> 해당 결과 바인딩 -> 최종 출력물
    total, fruit, eat = 10, "바나나", 3
    print(f"{total}개의 {fruit}중에서 {eat}개를 먹었다")
    # 플레이스 폴더 내부에 연산식 활용 가능
    total, fruit, eat = 10, "banana", 3
    print(f"{total}개의 {fruit.upper()}중에서 {eat}개를 먹어서 {total - eat}개가 남았다")
if __name__ == "__main__":
    # define_str()
    # string_oper()
    # search_methods()
    # modify_replace_methods()
    # align_method()
    # split_join_method()
    # check_methods()
    string_format()