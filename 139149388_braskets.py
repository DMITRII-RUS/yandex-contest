# 139149388

text = input()  # Ввод исходной строки из скобок.


def is_correct_bracket_seq(brackets) -> bool:
    items = []
    if len(brackets) == 0:
        return True
    for item in brackets:
        if item in '([{':  # Если это открывающая скобка, добавляем в список.
            items.append(item)
        elif item in ')]}':   # Если это закрывающаяся скобка, то:
            if not items:  # Если items пуст или если это не скобки - False.
                return False
            last_bracket = items.pop()  # Последняя скобка.
            if item == ')' and last_bracket != '(':
                return False   # Если нарушен порядок скобок '()', то False.
            if item == ']' and last_bracket != '[':
                return False    # Если нарушен порядок скобок '[]', то False.
            if item == '}' and last_bracket != '{':
                return False    # Если нарушен порядок скобок '{}', то False.
    return len(items) == 0 # Проверяем, что все скобки закрыты.


if __name__ == '__main__':
    print(is_correct_bracket_seq(text))
