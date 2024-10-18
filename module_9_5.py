class StepValueError(ValueError):
    pass



class Iterator:
    def __init__(self, start, stop, step = 1):
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')

        if step > 0 and start > stop:
            raise StepValueError(f'Шаг не может быть положительным для start={start} и stop={stop}')

        if step < 0 and start < stop:
            raise StepValueError(f'Шаг не может быть отрицательным для start={start} и stop={stop}')

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = 0


    def __iter__(self):
        self.pointer = self.start - self.step
        return self


    def __next__(self):
        self.pointer += self.step

        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration()

        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration()

        return self.pointer



try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)




for i in iter2:
    print(i, end=' ')
    print()
for i in iter3:
    print(i, end=' ')
    print()
for i in iter4:
    print(i, end=' ')
    print()

try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
        print()
except StepValueError as exc:
    print(exc.args[0])

