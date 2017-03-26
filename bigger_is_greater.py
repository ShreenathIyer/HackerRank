def lexi(words):
    flag = 0
    done = 0
    for word in words:
        if len(word) == 1:
            print "no answer"
            done = 1
        else:
            word = list(word)
            for char in range(len(word)-2, -1, -1):
                if word[char] >= word[char + 1]:
                    flag = 0
                else:
                    flag = 1
                    break
            if flag == 1:
                if len(word) == 2:
                    temp = word[char]
                    word[char] = word[char + 1]
                    word[char + 1] = temp
                    curr_word = ''.join(word)
                    print curr_word
                else:
                    curr_char = word[char]
                    next_char = word[char + 1]
                    for point in range(char, len(word), 1):
                        if word[point] > curr_char and word[point] <= next_char:
                            next_char = word[point]
                            pos = point
                    word[char] = next_char
                    word[pos] = curr_char
                    for i in range(char + 1, len(word)):
                        for j in range(char + 1, len(word) - 1):
                            if word[j] > word[j + 1]:
                                temp = word[j]
                                word[j] = word[j + 1]
                                word[j + 1] = temp
                    curr_word = ''.join(word)
                    print curr_word
            else:
                print "no answer"
                done = 1
        flag = 0
        done = 0

if __name__  ==  "__main__":
    t = raw_input().strip().split(' ')
    t = int(t[0])
    words = []
    for i in range(0, t):
        w = raw_input().strip().split(' ')
        words.extend(w)
    lexi(words)