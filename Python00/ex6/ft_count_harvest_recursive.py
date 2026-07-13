def recursive_harvest(days):
    if days < 1:
        return
    recursive_harvest(days - 1)
    print(f"Day {days}")


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    recursive_harvest(days)
    print("Harvest time!")
