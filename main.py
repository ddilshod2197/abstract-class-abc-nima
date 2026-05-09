from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class ConcreteClass(AbstractClass):
    def abstract_method(self):
        return "Abstract method implemented"

class NotAbstractClass:
    def not_abstract_method(self):
        return "Not abstract method implemented"

obj1 = ConcreteClass()
print(obj1.abstract_method())  # Abstract method implemented

try:
    obj2 = NotAbstractClass()
    obj2.abstract_method()
except AttributeError:
    print("NotAbstractClass does not have abstract_method")

try:
    obj3 = AbstractClass()
    obj3.abstract_method()
except TypeError:
    print("AbstractClass is abstract and cannot be instantiated")
```

Kodda AbstractClass klassi abstract klass sifatida yaratilganligi ko'rsatilgan. AbstractClass klassi AbstractMethod abstract metodni o'z ichiga oladi. AbstractMethod abstract metod bo'lib, uning implementatsiyasi mavjud emas. AbstractMethodni implementatsiya qilish uchun ConcreteClass klassi AbstractClass klassidan meros qilib oladi. NotAbstractClass klassi abstract metodni o'z ichiga olmasligi sababli abstract klass emas. AbstractClass klassi abstract metodni o'z ichiga olganligi sababli abstract klass bo'lib, uning obyekti yaratishga ruxsat yo'q.
