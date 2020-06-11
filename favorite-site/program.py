import webbrowser

def visit_sites():
    print("Opening your favorite sites...")
    try:
        with open("sites.txt") as sites:
            i = 0
            for site in sites:
                webbrowser.open_new_tab(site.strip())
                i += 1
                print(".", end=" ")
        print("\n%d Tabs Opened.\nEnjoy!" % i)
    except Exception as e:
        print("File Error : ", e)

if __name__ == "__main__":
    visit_sites()