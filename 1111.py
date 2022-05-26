class Human:
    is_human: bool = True

    _id: int = 0

    def __init__(self, fname: str, lname: str) -> None:
        self.lname = lname
        self.fname = fname
        self.id = Human._id
        Human._id += 1

def __iter__(self):
    return iter(self.fname)

print('vasya', 'knopkin')
print('petya', 'pupkin')
for i in vasya:
    print(i)
