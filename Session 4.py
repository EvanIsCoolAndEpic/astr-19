class animal:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, has_fur):
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.has_fur = has_fur
    def describe(self):
        print(f"Arm length: {self.arm_length}")
        print(f"Leg length: {self.leg_length}")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has tail: {self.has_tail}")
        print(f"Has fur: {self.has_fur}")

def main():
    an = animal(1, 1, 2, True, True)
    an.describe()

if __name__ == '__main__':
    main()