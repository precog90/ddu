import subprocess
import platform
import os

from cat_factory import cat_service






def main():

    #print the header
    print_header("CAT FACTORY")
    #get or create output folders
    folder = get_or_create_output_folder()
    print("Found or Created {}".format(folder))
    # download cats
    download_cats(folder)
    display_cats(folder)


def print_header(banner_name):
    print()
    print()
    print("----------------------------------------------------")
    print("                {0}".format(banner_name))
    print("-----------------------------------------------------")
    print()

def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.abspath(os.path.join(base_folder, folder))
    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    cat_count = 8
    print("Contacting server downloading cats")
    for i in range(1, cat_count+1):
        name = 'lolcat {}'.format(i)
        print("Downloading cat" + name)
        cat_service.get_cat(folder, name)
    print("Done")



def display_cats(folder):
    #open folder
    print("Displaying cats in OS window")
    if platform.system() == 'Darwin':
        subprocess.call(['open',folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("Fucked up OS {}".format(platform.system()))


if  __name__ == '__main__':
        main()
