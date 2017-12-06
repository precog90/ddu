from python_kemptech_api import LoadMaster as loadmaster
from getpass import getpass
import csv
import os


def get_data_file():
    """This function returns full path of the file where data is stored"""
    base_folder = os.path.dirname(__file__)
    # print(base_folder)
    return os.path.join(base_folder, 'data', 'lb_ips.csv')
    # print(filename)


def load_file(filename):
    """This function loads the date from the filename"""
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin, delimiter=',')
        lb_ips = []
        for lb_ip in reader:
            lb_ips.append(lb_ip['lb_ip'])
        return lb_ips

def main():
    # lb_ip = '10.81.80.4'
    # lb_username = input("Enter the username: ")
    # lb_password = getpass("Enter the password: ")
    # print(lb_ip, username, password)

    # lm = loadmaster(lb_ip, lb_username, lb_password)
    # # print(type(lm))
    # lb_vs = lm.get_virtual_service(index=1)
    # for index, vs in enumerate(lb_vs):
    #     print(" {} : {}".format(index, vs))

    filename = get_data_file()
    lb_ips = load_file(filename)
    lb_vip_to_be_searched = input(" Enter the name of the VIP to check status: ")
    lb_username = input("Enter the username: ")
    lb_password = getpass("Enter the password: ")


    for lb_ip in lb_ips:
        lm = loadmaster(lb_ip, lb_username, lb_password)
        # lm.get_virtual_services()
        try:
            for vs in lm.get_virtual_services():
                if not vs:
                    print("No virtual services found")
                if vs.nickname == lb_vip_to_be_searched:
                    print("{} is on {} and {}".format(vs.nickname, lb_ip, vs.status))
        except:
            print("Unexpected error on {}".format(lb_ip))




if __name__ == '__main__':
    main()
