import json


def use_dict():
    user_info = {'firstName': 'Rust', 'lastName': 'Fisher'}
    books = ['Python入门']
    books.append('Python进阶')
    result = {'userInfo': user_info, 'books': books}
    result['desc'] = '可以直接添加一个key-value进去'
    print(result)
    return result


def to_json1(input_dict):
    print('input:', input_dict)
    jsonTxt = json.dumps(input_dict)
    print(jsonTxt)


def to_json2(input_dict):
    print('input:', input_dict)
    jsonTxt = json.dumps(input_dict, ensure_ascii=False)
    print(jsonTxt)


def list_json_demo():
    tom_hanks = {'firstName': 'Tom', 'lastName': 'Hanks', 'movies': ['Cast Away']}
    info = use_dict()
    list = [tom_hanks, info]
    jsonTxt = json.dumps(list, ensure_ascii=False)
    print(jsonTxt)
    return jsonTxt


def json_to_dict1(jsonTxt):
    obj1 = json.loads(jsonTxt)
    print(obj1)


if __name__ == '__main__':
    # res1 = use_dict()
    # to_json1(res1)
    # to_json2(res1)
    jsonTxt = list_json_demo()
    json_to_dict1(jsonTxt)
