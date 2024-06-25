"""Реализация двусвязного списка."""
from typing import Optional, Any


class ObjList():
    """Класс объекта двусвязного списка."""

    def __init__(self, data: Optional[Any]) -> None:
        """."""
        self.__next: Optional[ObjList] = None
        self.__prev: Optional[ObjList] = None
        self.__data: Optional[Any] = data

    def set_next(self, obj: Optional['ObjList']) -> None:
        """Изменение приватного свойства __next."""
        self.__next = obj

    def set_prev(self, obj: Optional['ObjList']) -> None:
        """Изменение приватного свойства __prev."""
        self.__prev = obj

    def get_next(self) -> Optional['ObjList']:
        """Получение значение приватного свойства __next."""
        return self.__next

    def get_prev(self) -> Optional['ObjList']:
        """Получение значения приватного свойства __prev."""
        return self.__prev

    def set_data(self, data: Optional[Any]) -> None:
        """Изменение приватного свойства __data."""
        self.__data = data

    def get_data(self) -> Optional[Any]:
        """Получение значения приватного свойства __data."""
        return self.__data


class LinkedList():
    """Класс реализация двусвязного списка."""

    def __init__(self) -> None:
        """."""
        self.head: Optional[ObjList] = None
        self.tail: Optional[ObjList] = None

    def add_object(self, obj: ObjList) -> None:
        """Добавление нового объекта obj в конец связного списка."""
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remote_obj(self) -> None:
        """Удаление последнего объекта из связного списка."""
        if self.tail is None:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            new_last = self.tail.get_prev()
            new_last.set_next(None)
            self.tail = new_last

    def get_data(self) -> Optional[list[Optional[ObjList]]]:
        """Получение списка всех объектов связного списка."""
        data: list[Optional[ObjList]] = []
        obj = self.head
        while obj is not None:
            data.append(obj.get_data())
            obj = obj.get_next()
        return data


if __name__ == '__main__':

    ob = ObjList("данные 1")

    lst = LinkedList()

    lst.add_object(ObjList("данные 1"))
    lst.add_object(ObjList("данные 2"))
    lst.add_object(ObjList("данные 3"))

    print(lst.get_data())

    lst.remote_obj()
    print(lst.get_data())

    lst.remote_obj()
    print(lst.get_data())

    lst.remote_obj()
    lst.remote_obj()
    lst.remote_obj()

    print(lst.get_data())

    lst.add_object(ObjList("данные 3"))
    print(lst.get_data())
