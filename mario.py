def main():
    print_sqr(5)

def print_sqr(size):
    for i in range (size):
        print_row(size)
        
def print_row(width):
    print("#" * width)
    
main()