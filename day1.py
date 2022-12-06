import io, sys;

class ELF:
    def __init__(self, elements):
        self.elements = elements
        self.count()

    def count(self):
        x = 0
        for line in self.elements:
            x += line
        self.inventory = x


class MAIN:
    def __init__(self):
        self.elves = []
        self.read_input()

    def read_input(self):
        with open("input.txt", "r") as input_file:
            self.lines = input_file.read().split("\n")

        arr = []
        for line in self.lines:
            if line != "":
                arr.append(int(line))
            else:
                self.elves.append(ELF(arr))
                arr = []
                continue


    def max_calories(self):
        inventory_values = [elf.inventory for elf in self.elves]

        max_inventory = max(inventory_values)

        for index, elf in enumerate(self.elves):
            if elf.inventory == max_inventory:
                max_index = index
                break

        print(f"The maximum is at the {max_index} block, with {max_inventory} calories")

    def max_calories_n_sum(self, n):
        inventory_values = [elf.inventory for elf in self.elves]
        max_arr = []

        for max_values in range(n):
            max_inventory = max(inventory_values)
            max_arr.append(max_inventory)

            inventory_values.remove(max_arr[max_values])
        
        print(f"The {n} maximums add up to {sum(max_arr)} calories")


main = MAIN()
main.max_calories()
main.max_calories_n_sum(3)
