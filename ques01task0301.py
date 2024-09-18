from collections import Counter
import csv

with open('q1Output_combinedText.txt', 'r') as file:
    text = file.read()
    
words = text.split()

word_counts = Counter(words)

top_30_words = word_counts.most_common(30)

with open('q1t3_1_Output_top_30_words.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])  # Write header
    writer.writerows(top_30_words)  # Write top 30 words and their counts

print(top_30_words)