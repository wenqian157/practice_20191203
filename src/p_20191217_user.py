from p_20191217_library import Base


assert (hasattr(Base, 'foo')), 'broke'

class Derived(Base):
    def bar(self):
        return self.foo()


if __name__ == '__main__':
    derived = Derived()
    print(derived.bar())