def define_dict():
    """
    dict 정의
    """
    # 타입 함수를 이용한 생성
    dct = dict()    # 빈 dict
    print(dct, type(dct))
    # 리터럴 생성
    dct = {}        # 빈 dict
    print(dct, type(dct))
    # 키워드 인수로 생성
    dct = dict(one=1, two=2)
    print(dct, type(dct))
    # 키, 값 쌍 튜플의 목록으로 생성
    dct = dict([("one",1), ("two",2), ("three",3)])
    print(dct, type(dct))

    # 키 목록과 값 목록이 별도로 있을 때 두 목록을 합쳐서 dict 생성
    keys = ('one', 'two', 'three', 'four')
    values = (1, 2, 3)
    dct = dict(zip(keys, values))   # 키 목록과 값 목록을 합쳐서 dict에 전달
    print(dct, type(dct))



if __name__ == "__main__":
    define_dict()