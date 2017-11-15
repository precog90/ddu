import journal
# from journal import load
# from journal import *

def main():
    print_header("JOURNAL APP")
    run_event_loop()


def print_header(banner_name):
    print()
    print("----------------------------------------------------")
    print("                {0}".format(banner_name))
    print("-----------------------------------------------------")
    print()


def run_event_loop():
    print("What you wanna do with your journal?")
    cmd = "non_empty"
    journal_name = 'default'
    journal_data = journal.load(journal_name)
    while cmd != 'x' and cmd:
        cmd = input("[L]ist entries, [A]dd an entry, E[x]it: ")
        cmd = cmd.lower().strip(" ")
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entries(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we do'nt understand {0}".format(cmd))
    print("Done , Good Bye")
    journal.save(journal_name, journal_data)


def list_entries(data):
    entries = reversed(data)
    for index, entry in enumerate(entries):
        print("* [{}] : {}".format(index+1, entry))


def add_entries(data):
    text = input("Type your entry:")
    journal.add_entry(text, data)
    #data.append(text)

main()
