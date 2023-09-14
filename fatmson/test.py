if True:    
    print("hello")
    print("sAAAAAAAAAAA")
    print("a")


# Tanımsız Değişken Hatası
print(z)

# Dizin Hatası
my_list = [1, 2, 3]
print(my_list[5])


# Anahtar Hatası
my_dict = {'name': 'John', 'age': 30}
print(my_dict['city'])

# Değer Hatası
x = int("hello")

# Sıfıra Bölme Hatası
result = 5 / 0

# Dosya Bulunamadı Hatası
with open("nonexistent.txt", "r") as file:
    content = file.read()

# Modül Bulunamadı Hatası
if True:
    print("r----------------------------------------------")
    import nonexistent_module
    print("s0000000000000000000000000000000000000")

# Özellik Hatası
class MyClass:
    def __init__(self):
        self.value = 42

obj = MyClass()
print(obj.size)
