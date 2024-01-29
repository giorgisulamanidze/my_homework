#   N=1

# import csv

# def find_second_most_frequent_word(filename):

#    word_counts = {}  
#    with open(filename, 'r') as file:
#        reader = csv.reader(file) 
#        for row in reader:
#            word = row[0].lower()  
#            word_counts[word] = word_counts.get(word, 0) + 1 

#    words_by_count = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
#    for i in range(1, len(words_by_count)):
#        if words_by_count[i][0] != words_by_count[0][0]:
#            return words_by_count[i][0]

#    return None 

# if __name__ == "__main__":
#    filename = "article.txt"
#    second_most_frequent_word = find_second_most_frequent_word(filename)

#    if second_most_frequent_word:
#        print("The second most frequent word is:", second_most_frequent_word)
#    else:
#        print("All words have the same frequency in the document.")


#   N2
# import csv

# def copy_csv_to_txt(csv_file, txt_file):
#   """Copies information from a CSV file to a TXT file."""

#   with open(csv_file, 'r') as csvfile, open(txt_file, 'w') as txtfile:
#     reader = csv.reader(csvfile)
#     writer = txtfile.writelines

#     for row in reader:
#       writer(" ".join(row) + "\n")  

# if __name__ == "__main__":
#   csv_file = "names.csv"
#   txt_file = "names.txt"
#   copy_csv_to_txt(csv_file, txt_file)
#   print("Information from names.csv copied to names.txt")
