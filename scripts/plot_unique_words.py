from wordcloud import WordCloud
import json
import operator
import matplotlib.pyplot as plt


filename = "total_words_count.json"
with open(filename, 'r') as f:
    total_word_count = dict(json.load(f))


keyword_count = dict( sorted(total_word_count.items(), key=operator.itemgetter(1),reverse=True)) # sort descending

wordcloud = WordCloud(width = 1000, height = 500, background_color='white', max_words=1000,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(keyword_count)
plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.savefig("keywords"+".jpg", bbox_inches='tight')
plt.show()
plt.close()