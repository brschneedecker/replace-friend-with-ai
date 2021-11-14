# importing required modules
import argparse
import lm
import os
  
def valid_path(path):
    return os.path.exists(path)

def main():

    # create a parser object
    parser = argparse.ArgumentParser(description = "Chats AI") 

    # add argument
    parser.add_argument("n", 
                        nargs = 1, 
                        metavar = "n",
                        type = int,  
                        help = "Number of tokens to consider in N-grams model")

    # add argument
    parser.add_argument("path", 
                        nargs = 1, 
                        metavar = "path", 
                        type = str, 
                        help = "Location of corpus")

    # parse the arguments from standard input
    args = parser.parse_args()

    n = args.n[0]
    path = args.path[0]
    full_path = os.path.join(os.getcwd(), path)

    if valid_path(path):
        print("Training the model...")
        model = lm.create_ngram_model(args.n[0], args.path[0])
    else:
        print("Invalid path {}".format(full_path))


    while True:
        num_tokens_str = input("Please enter the message length in tokens or 'q' to quit: ")

        if num_tokens_str == 'q':
            print("Goodbye")
            break

        try:
            num_tokens = int(num_tokens_str)
            print(model.random_text(num_tokens), "")
        except ValueError:
            print("{} is not a valid input, try again\n".format(num_tokens_str))


if __name__ == "__main__":
    main()