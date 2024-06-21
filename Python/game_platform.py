def calculate_final_speed(initial_speed, inclinations):
    for inclination in inclinations:
        if inclination < 0:
            initial_speed += abs(inclination)
        else:
            initial_speed -= abs(inclination)
        if initial_speed <= 0:
            return 0
    return initial_speed


if __name__ == '__main__':
    print(calculate_final_speed(60, [0, 30, 0, -45, 0]))
