
"""
Это из урока №6 Динамические урлы. Делаем обработчик УРЛ.
В данном случае для archive по голдам, обязательно 4 цифры.
"""
class FordigitYearConverter:
    regex = "[0-9]{4}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value