from pyhton_OOP.inheritance.hero.project.elf import Elf
# from project.elf import Elf


class MuseElf(Elf):
    def __str__(self):
        return f"{self.username} of type {__class__.__name__} has level {self.level}"