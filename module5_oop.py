class NumberProcessor:
    def __init__(self):
        self.numbers = []
    
    def get_input(self):
        N = int(input("Enter a positive integer N: "))
        print(f"Now enter {N} numbers one by one:")
        for i in range(N):
            num = int(input(f"Enter number {i+1}: "))
            self.numbers.append(num)
    
    def find_index(self, X):
        for i in range(len(self.numbers)):
            if self.numbers[i] == X:
                return i + 1 
        return -1

def main():
    processor = NumberProcessor()
    processor.get_input()
    X = int(input("Enter the number X to search for: "))
    result = processor.find_index(X)
    print(result)

if __name__ == "__main__":
    main()