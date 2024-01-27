from statistics import mean

NUMBER_OF_TEMPS = 6

def tem(s):
    return s[:-1] if len(s) > 1 else s

def read_temperatures(number_of_temps=NUMBER_OF_TEMPS):
    temps = []

    while len(temps) < number_of_temps:
        try:
            temp_c_str = input('Enter a Centigrade Temperate (end it with C): ')

            if temp_c_str.endswith(('C', 'c')):
                temps.append(float(tem(temp_c_str)))
            else:
                print('No "C" at the end of the input. Why not try again?')
        except ValueError:
            print('Invalid input. Why not try again?')

    return temps

def print_results(temps_list):
    print()
    print(f'Max Temp:  {max(temps_list):6.2f}C.')
    print(f'Min Temp:  {min(temps_list):6.2f}C.')
    print(f'Mean Temp: {mean(temps_list):6.2f}C.')
    print()


if __name__ == '__main__':

    print_results(read_temperatures(NUMBER_OF_TEMPS))