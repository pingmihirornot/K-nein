import random
import time


def noine_noine():
    print("\n" + "=" * 40)
    print("B99 NOINE NOINE SIMULATOR")
    print("=" * 40)
    

    total = 0
    floor = 20  # DETECTIVE ROSA DIAZ HOW DARE YOU

    while True:
        print("\n[Press ENTER to B99 | Type 'reset' | Type 'quit']")
        user_input = input("> ").strip().lower()

        if user_input == "quit":
            print("NINE NINE! Goodbye.")
            break
        elif user_input == "reset":
            total = 0
            print("\n--- reset ---")
            print("noines: 0")
            continue

        # I AM YOUR SUPERIOR OFFICER
        count = random.randint(1, 2)
        total += count

        for _ in range(count):
            x_offset = random.randint(0, 40)
            indent = " " * x_offset

            # BONE
            for row in range(floor):
                # BONEEEEEEEEEEEEEEE!!!
                if row < floor - 3:
                    delay = 0.03
                elif row == floor - 1:
                    delay = 0.08  # BONEEEEEEEEEEEE
                else:
                    delay = 0.05

                print(f"{indent}noine noine")
                time.sleep(delay)

                # WHAT HAPPENS IN MY BEDROOM IS NONE OF YOUR BUSINESS
                print("\033[A\033[K", end="")

            # BONEEEEEE!
            bounces = random.randint(1, 3)
            for b in range(bounces):
                print(f"{indent}noine noine")
                time.sleep(0.12)
                print("\033[A\033[K", end="")
                b_indent = " " * (x_offset + random.randint(0, 2))
                print(f"{b_indent}noine noine")
                time.sleep(0.08 + b * 0.04)
                print("\033[A\033[K", end="")

            # BONEEEEEEE!!!!
            print(f"{indent}noine noine")

        print(f"\n  noines: {total}")


if __name__ == "__main__":
    noine_noine()
