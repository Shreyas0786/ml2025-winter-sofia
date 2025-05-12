from module5_mod import NumberProcessor

def main():
    processor = NumberProcessor()
    processor.get_input()
    X = int(input("Enter the number X to search for: "))
    result = processor.find_index(X)
    print(result)

if __name__ == "__main__":
    main()