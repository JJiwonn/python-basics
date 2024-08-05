#Operator
# 기본적으로 하나의 python파일은 그 자체가 모듈이다(직접실행 혹은 다른곳에서 불러들일수있음)
def arith_oper():
    print("==== 산술 연산 ====")
    print(7/3)  # 파이썬 3에서는 int / int -> float
    print(7//3) # 정수 나눗셈의 몫 연산자
    print(7%3)  # 정수 나눗셈의 나머지 연산자

    # 나눗셈의 몫과 나멈지 동시에 구하는 방법
    print(divmod(7,3))
    # 결과값이 (2,1)으로 나옴 (몫, 나머지) 형태인데 이때 ()괄호는 파이썬의 튜플임
    data = divmod(7,3)
    print("7/3의 몫:", divmod(7,3)[0])
    print("7/3의 나머지:", divmod(7,3)[1])

    print(7**3) #지수승: 7의 3제곱
    print(pow(7,3)) #지수 함수: 7의 3제곱

    # 복합 관계식
    a = 6
    # a가 0 - 10 사이의 값인가?
    # 조건1: a > 0
    # 조건2: a < 10
    # 조건1 and 조건2
    print(0 < a and a < 10)
    print(0 < a <10)

    # 다양한 자료 구조의 대소 비교
    print("문자열의 대소:", "abcd" > "abd")
    print("튜플의 대소:", (1, 2, 3) > (1, 3, 4))

    # 동질성의 비교는 == 사용, 동일성의 비교 is 사용
    a = 10; b = 20; c = a
    print("a == b?", a == b)
    print("a is b?", a is b)
    print("a == c?", a == c)
    print("a is c?", a is c)

import keyword # import 키워드 -> 모듈을 불러오는 명령어
def var_ex():
    print("==== 변수 ====")
    # 변수는 문자, 숫자, 언더바의 조합으로 만들수 있다
    # 숫자로 시작할 수 없다
    # (파이썬의 키워드)(예약어)는 변수명으로 사용될 수 없다.
    # 파일명도 변수 명명 규칙에 맞춰 줘야 한다.
    print("예약어 목록:", keyword.kwlist)
    print("예약어 갯수:", len(keyword.kwlist))

def assignment_ex():
    print("===== 치환문 ====")
    # 변수 선언 절차 없다
    print("namespace:", dir()) # 이건 함수 네임스페이스이기에 결과값이 없다 []로 표시
    a = 2024 # 첫번째 할당 방생할 때 namespace에 추가된다
    b = a + 1
    print(a, b)
    print("namespace:", dir())

    # 여러 변수를 한꺼번에 할당할 수 있다
    c, d = 3.5, 5.3
    print("c, d =", c,d)
    # 값의 교환 (Swap)
    c,d = d,c
    print("c, d =", c,d)

    # 같은 값을 동시 할당
    x = y = z = 10
    print(x, y, z)

    # 파이썬은 동적 타이핑 언어
    a = 2024    # 값이 할당될 때 그때야 타입이 결정된다
                # -> 중간중간에 우리가 가지고 있는 타입이 무엇인지 확인해줘야한다
    print(a, "is", type(a))     # 현재 객체의 형식을 체크한다
    a = "Hello Python"
    print(a, "is", type(a))

    # 특정 변수가 특정 객체인지 여부를 판단하는 함수: isinstance
    print("a는 str의 객체?", isinstance(a, str))

    # 확장 치환문 : 산술, 비교연산자, 확장치환문으로 변경 가능
    a = 10
    a += 10 # a = a + 10
    print(a)

def bool_ex():
    print("==== bool 연습 =====")
    # 참(True), 거짓(False)
    # 내부적으로 거짓은 0, 나머지는 모두 참으로 판정한다
    # 조건 분기, 흐름 제어 활용되기 때문에 중요하다
    # boolean 판정을 내리고자 한다면
    #   논리 연산자 비교 연산자의 결과로
    #   bool 객체 함수를 통해 얻을 수 있다
    print(bool(0))
    a = 2024
    print(a > 0)    # 비교 연산자를 통한 논리값의 판정
    print(type(a))

    print(isinstance(True, bool))   # True
    print(isinstance(True, int))    # True
    print(True + True)

    # 자료의 형태에 의한 boolean 판정
    print(bool(2024), bool(0))  # int 값에 의한 boolean
    print(bool(3.14), bool(0))  # float 값에 의한 boolean
    print(bool("Python"), bool(""))  # str 값에 의한 boolean

    print(bool([1, 2, 3]), bool([])) # list 값에 의한 boolean
    print(bool({"key" : "value"}), bool({})) # dict 값에 의한 boolean
    print(bool(None))   # None -> 비어있음 -> Java null

    # 논리식의 계산 순서: Curcuit Break
    # OR일 경우, 첫번째 True 연산 결과를 취한다
    # AND일 경우, 둘 다 TRUE면 뒤쪽 결과를 취한다
    # AND일 경우, 전체 논리식이 거짓이라면 None을 반환한다
    print("CB 1:", [] or "logical") # False or True
    print("CB 2:", 'logical' or 'operator') # True or True
    print("CB 2-1:", 'logical' and 'operator')  # True and True
    print("CB 3:", '' or 'operator')    # False or True
    print("CB 3-2:", '' and 'operator') # False and True
    print("CB 4:", None and 1)  # False and True
    print("CB 5:", None or [])  # False or False


def type_hint():
    # 파이썬은 동적 타이핑 언어 -> 변수의 타입을 명시적으로 지정하지 않는다
    # 3.5부터 타입 힌트를 이용, 타입체크를 진행할 수 있다
    def add(a: int, b: int) -> int: # 두개의 int 입력 받아서 int를 리턴하는 함수
        return a + b

    print(add(10, 20))
    # 4316print(add("Python", 3.10))

    def greet(name: str) -> str: # str 입력받아서 str를 리턴하는 함수
        return 2024
        # return "Hello," +name

    untyped = "string"  # 타입 힌트가 적용되지 않은 변수
    print(untyped)
    untyped = 2024
    print(untyped)

    typed: str = "string"   # 타입 힌트가 적용된 변수
    print(typed)
    typed = 2024
    print(typed)

def int_ex():
    print("==== 정수형 연습 =====")

    a = 2024    # 리터럴 선언
    b = int(2024)   # 타입 함수 사용

    print(a, "is", type(a))
    print(b, "is", type(b))

    # 2진, 8진, 16진 정수 표현 가능
    b = 0b1101  # 0b
    o = 0o23    # 0o
    x = 0xFF   # 0x

    print(b, o, x)

    # 파이썬 3에서는 int와 long 구분이 없다ㅣ
    # long형 데이터 저장크기가 64bit 초과해서 적재할 수 있다
    i = 2 ** 2048
    print(i)
    print(i.bit_length())

    # 진법 변환 함수
    i = 48
    print(i, bin(i), oct(i), hex(i))

def float_ex():
    print("==== 실수형 연습 ====")
    a = 3.14159 # 리터럴로 생성
    print(a, "is", type(a))
    print(isinstance(a, float)) # a는 float인가?

    b = float(3.0)  # 타입함수로 생성
    print(b, "is", type(b))
    print(isinstance(b, float)) # b는 float인가?

    print(a.is_integer(), b.is_integer())
    # 여기서 b는 float인가 했을 때 True이고 isteger라고 했을 때도 True라고 했는데
    # 의미는 타입은 float인데 담긴 값은 3.0으로 정수이기에 둘다 True인것이다

    # 지수 표기법으로도 확인 가능
    c = 3e3     # 3 * 10 ** 3
    d = -2E-5   # -2 * 10 ** -5
    print(c,d)
    print(-2E-5 == -0.000002)   # 같은 표현으로 보면 됨

def complex_ex():
    print("==== 복소수 연습 ====")
    # 복소수 : 실수부 + 허수부j
    a = 4 + 5j
    print(a, "is", type(a))
    print(isinstance(a, complex))   # a는 복소수?

    b = 7 - 2j
    print(b, "is", type(b))
    print(isinstance(a, complex))

    print(a + b)    # 복소수는 산술연산이 가능
    print(b.real, b.imag)   # 실수부, 허수부
    print(a, "의 켤레복소수는", a.conjugate()) # 켤레 복소수

if __name__ == "__main__":
    # 다른 모듈로 import 되는 경우 __name__ == "python_basics"
    # 직접 싱행 될 경우(즉 최상위 모듈일 경우) __name__ == "__main__"
    # arith_oper() # 다른 모듈이 사용하지 못하고 최상위만 사용할 수 있음
    # var_ex()
    # assignment_ex() # 변수 치환연습
    # bool_ex()
    # type_hint()
    # int_ex()
    # float_ex()
    complex_ex()