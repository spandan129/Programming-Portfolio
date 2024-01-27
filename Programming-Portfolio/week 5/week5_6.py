""" Write a program that takes the name of a file as a command-line argument, and
creates a backup copy of that file. The backup should contain an exact copy of the
contents of the original and should, obviously, have a different name.
Hint: By now, you should be getting the idea that there is a built-in way to do the
heavy lifting here! Take a look at the "Brief Tour of the Standard Library" in the docs"""

from shutil import copyfile
from sys import argv

if __name__ == '__main__':
    try:
        filename_in = argv[1]
        filename, extension = filename_in.split('.')

        filename_out = f'{filename}-backup.{extension}'

        copyfile(filename_in, filename_out)
    except IndexError:
        print('No filename supplied. Nothing to do.')
    except ValueError:
        print('Argument does not look like a filename. Cannot find file extension.')
    except FileNotFoundError:
        print(f'Cannot open "{filename_in}". Bailing out.')