import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')
def print_header(banner_name):
    """Prints header for the program."""
    print()
    print()
    print("----------------------------------------------------")
    print("                {0}".format(banner_name))
    print("-----------------------------------------------------")
    print()


def get_folder_from_user():
    """Input from the user about the searched folder and return absolute path of the folder."""
    folder = input("What folder do you want to search: ")
    if not folder or not folder.strip():
        return None
    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    """Input from the user about the searched text."""
    text = input("What are you searching for? ")
    return text.lower()


def search_file(folder, full_item, text):
    """ Searches for the string occurences in the file."""
    #matches = []
    line_num = 0
    with open(full_item, 'r', encoding='utf-8') as fin:
        for line in fin:
            line_num += 1
            if line.lower().find(text) >= 0:
                m = SearchResult(line=line_num, file=full_item, text=line.strip())
                #matches.append(m)
                yield m
        #return matches


def search_folders(folder, text):
    """Search text in the folder"""
    items = os.listdir(folder)
    #all_matches = []
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            #matches = search_folders(full_item, text)
            #all_matches.extend(matches)
            # for m in matches:
            #     yield m
            yield from search_folders(full_item, text)
        else:
            #matches = search_file(folder, full_item, text)
            #all_matches.extend(matches)
            # for m in matches:
            #     yield m
            yield from search_file(folder, full_item, text)

    #return all_matches


def main():
    """Main function"""
    count = 0
    print_header("FILE SEARCHER APP")
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we cant search that folder")
    text = get_search_text_from_user()
    if not text:
        print("We can't search the string")
    matches = search_folders(folder, text)
    for match in matches:
        count += 1
        #print("--------MATCH--------")
        #print("file : {}".format(match.file))
        #print("line: {}".format(match.line))
        #print("text: {}".format(match.text))

    print("Found {} matches".format(count))

if __name__ == '__main__':
    main()