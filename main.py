class ATM:
    def __init__(self):
        self.__banknotes = [0, 0, 0, 0, 0]
        self.__denominations = [10, 50, 100, 200, 500]

    def deposit(self, banknotes_count: list[int]) -> None:
        """
        :type banknotes_count: List[int]
        :rtype: None
        """
        for i in range(5):
            self.__banknotes[i] += banknotes_count[i]

    def withdraw(self, amount: int) -> list[int]:
        """
        :type amount: int
        :rtype: List[int]
        """
        # Создаем временный список для хранения количества купюр, которые будут использованы
        to_withdraw = [0] * 5
        remaining_amount = amount

        # Обрабатываем купюры от крупных к мелким
        for i in range(4, -1, -1):
            # Определяем максимальное количество купюр текущего номинала, которые могут быть использованы
            max_use = min(self.__banknotes[i], remaining_amount // self.__denominations[i])
            to_withdraw[i] = max_use
            remaining_amount -= max_use * self.__denominations[i]

        # Если не удалось собрать нужную сумму, возвращаем [-1]
        if remaining_amount != 0:
            return [-1]

        # Обновляем количество купюр в банкомате
        for i in range(5):
            self.__banknotes[i] -= to_withdraw[i]

        return to_withdraw


# Пример использования:
obj = ATM()
obj.deposit([0, 0, 1, 3, 1])
print(obj.withdraw(600))  # [0, 0, 1, 0, 1]
obj.deposit([0, 1, 0, 1, 1])
print(obj.withdraw(600))  # [-1]
print(obj.withdraw(550))  # [0, 1, 0, 0, 1]
