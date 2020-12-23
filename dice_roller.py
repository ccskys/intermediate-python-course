import random


def main():
    # print('You rolled a die')
    # roll = random.randint(1, 6)
    # print(f'You rolled a {roll}')
    dice_rolls = 2
    dice_sum = 0
    for i in range(0, dice_rolls):
        roll = random.randint(1, 6)
        dice_sum = dice_sum + roll
        print(f'You roller a {roll}')
    print(dice_sum)


if __name__ == "__main__":
    main()
