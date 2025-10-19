def is_balanced(s):
    """
    Проверяет, является ли строка сбалансированной по скобкам.

    Args:
        s: Строка, содержащая скобки.

    Returns:
        True, если строка сбалансирована, иначе False.
    """
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in opening_brackets:
            stack.append(
                char
            )  # если символ - открывающая скобка, то кладём открывающую скобку в стек
        elif char in closing_brackets:
            if not stack:  # Если стек пуст
                return False  # Закрывающая скобка без открывающей
            top = stack.pop()  # Достаём последнюю открывающую скобку
            if bracket_map[char] != top:
                return False  # Несоответствие скобок

    return not stack  # Сбалансирована, если стек пуст


def test_balanced_strings():
    """Тестирование функции is_balanced с различными случаями"""

    print("🧪 Запуск тестов проверки сбалансированности скобок...")

    # Тест 1: Сбалансированные строки
    print("\n✅ Тест 1: Сбалансированные строки")
    assert is_balanced("()") == True
    assert is_balanced("()[]{}") == True
    assert is_balanced("{[]}") == True
    assert is_balanced("") == True
    assert is_balanced("abc") == True  # Не содержит скобок, считается сбалансированной
    assert is_balanced("({[()]})") == True

    print("   Все сбалансированные тесты пройдены! ✓")

    # Тест 2: Несбалансированные строки
    print("\n❌ Тест 2: Несбалансированные строки")
    assert is_balanced("(]") == False
    assert is_balanced("([)]") == False
    assert is_balanced(")") == False
    assert is_balanced("(") == False
    assert is_balanced("((]") == False
    assert is_balanced("((())") == False
    assert is_balanced("))((") == False
    assert is_balanced("({[()]") == False
    assert is_balanced("((())}}") == False

    print("   Все несбалансированные тесты пройдены! ✓")

    print("\n🎉 Все тесты успешно пройдены! 🎉")


def run_examples():
    """Запуск примеров для демонстрации работы функции"""
    print("\n" + "=" * 50)
    print("📚 ДЕМОНСТРАЦИЯ РАБОТЫ ФУНКЦИИ")
    print("=" * 50)

    examples = [
        "()",
        "()[]{}",
        "{[]}",
        "(]",
        "([)]",
        "",
        "abc",
        "({[()]})",
        "((())",
        "({[()]",
    ]

    for example in examples:
        result = is_balanced(example)
        status = "✅ Сбалансировано" if result else "❌ Несбалансировано"
        print(f"'{example}' -> {status}")


if __name__ == "__main__":
    try:
        # Запуск тестов
        test_balanced_strings()

        # Демонстрация работы
        run_examples()

        print("\n" + "🎊 ВСЕ ПРОВЕРКИ ЗАВЕРШЕНЫ УСПЕШНО! 🎊")

    except AssertionError as e:
        print(f"\n💥 ОШИБКА В ТЕСТЕ: {e}")
    except Exception as e:
        print(f"\n⚠️ НЕИЗВЕСТНАЯ ОШИБКА: {e}")
