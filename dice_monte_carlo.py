import random
import numpy as np

def main():
    experiments = [100, 1000, 10000, 100000]

    for test in experiments:
        result = simulate_dice_rols(test)
        print(f"Result for {test} numbers of test:")
        print_experiment_result(result)


def simulate_dice_rols(number):
    experiments = []
    for _ in range(number):
        first_dice = random.randint(1, 6)
        second_dice = random.randint(1, 6)
        experiments.append(first_dice + second_dice)

    possible_variants = [i for i in range (2, 13)]
    result = {i: 0 for i in possible_variants}

    for item in result.items():
        variant = item[0]

        variant_count = 0
        for value in experiments:
            if variant == value:
                variant_count += 1
        
        
        # calculate percent
        result[variant] = (variant_count / len(experiments)) * 100


    # average = sum(results) / len(results)
    return result


def print_experiment_result(result):
    for item in result.items():
        print(f"{item[0]}: {item[1]:.2f}%")
    print("\n")


if __name__ == "__main__":
    main()
