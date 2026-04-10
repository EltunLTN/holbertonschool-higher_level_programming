# Python - Abstract Base Classes (ABC)

Bu qovluq Python-da aşağıdakı OOP anlayışlarını praktiki göstərir:

- `abc` modulu ilə abstract class və abstract method
- Duck typing
- Built-in tiplərdən inheritance
- Custom iterator yazmaq
- Multiple inheritance və MRO
- Mixins istifadə etmək

## Qovluq Məzmunu

### `task_00_abc.py`
- `Animal` adlı abstract class yaradır (`ABC`-dən miras alır).
- `sound()` methodu abstract olaraq təyin edilir.
- `Dog` və `Cat` sinifləri bu methodu implement edir.

### `task_01_duck_typing.py`
- `Shape` adlı abstract class (`area()` və `perimeter()`).
- `Circle` və `Rectangle` sinifləri bu interfeysi reallaşdırır.
- `shape_info(shape)` funksiyası duck typing ilə obyektin tipinə baxmadan
	`area()` və `perimeter()` çağırır.

### `task_02_verboselist.py`
- `VerboseList` built-in `list` sinifindən miras alır.
- `append`, `extend`, `remove`, `pop` methodları override olunub və
	əməliyyatlar barədə mesaj çap edir.

### `task_03_countediterator.py`
- `CountedIterator` custom iterator sinifidir.
- `__next__()` hər çağırışda sayğacı artırır.
- `get_count()` iterasiya zamanı neçə element oxunduğunu qaytarır.

### `task_04_flyingfish.py`
- `Fish` və `Bird` sinifləri yaradılıb.
- `FlyingFish(Fish, Bird)` multiple inheritance istifadə edir.
- `fly`, `swim`, `habitat` methodları override olunur.
- Faylda `FlyingFish.mro()` ilə method resolution order göstərilir.

### `task_05_dragon.py`
- `SwimMixin` və `FlyMixin` mixin sinifləridir.
- `Dragon(SwimMixin, FlyMixin)` sinifi bu qabiliyyətləri birləşdirir.
- `roar()` ilə əlavə davranış verilir.

## İşə Salma

Hər faylı ayrıca bu cür işə sala bilərsiniz:

```bash
python3 task_01_duck_typing.py
python3 task_04_flyingfish.py
python3 task_05_dragon.py
```

Windows PowerShell üçün:

```powershell
python task_01_duck_typing.py
python task_04_flyingfish.py
python task_05_dragon.py
```

## Öyrənilən Əsas Mövzular

- Abstract class ilə müqavilə (contract) yaratmaq
- Polymorphism və duck typing tətbiqi
- Inheritance-də method override
- Iterator protocol (`iter`, `next`, `__next__`)
- Multiple inheritance zamanı MRO davranışı
- Mixins ilə davranışı modulyar şəkildə əlavə etmək
,