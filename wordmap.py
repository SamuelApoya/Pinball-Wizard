
'''
Samuel Apoya
            CS 152
                  November 25, 2022
'''
def main():
    print("I will say a word and you will have to type any word that comes to your mind. ")

    words = ["goods " , "yes ", "no ", "come ", "sing ", "band ", "dance ", "can ", "bond ", "gang "]

    mapping ={}
    for word in words:
        response = input(word)

        mapping[word] = response

        for key in mapping.keys():

            print(key + "=" + mapping.get(key))

            
main()
            
    

  