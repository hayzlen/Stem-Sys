from kiessysteem import Kiessysteem

def main():
    print("[Start verkiezingsproces]")
    systeem = Kiessysteem()
    systeem.stemproces()
    print("\033[96m[Verkiezingsproces voltooid]\033[0m")
    


if __name__ == "__main__":
    main()
