import json
import os
from helper_functions import _get_files_with


# split with ': ' between the word and count

def convert_to_dictionary(filename):
    with open(filename) as f:
        word_lines = f.readlines()
    word_count = {}
    for line in word_lines:
        word_split = line.split(": ")
        word = word_split[0]
        count = word_split[1].replace("\n", "")
        if word in list(word_count.keys()):
            word_count[word].update(word_count[word] + count)
        else:
            word_count[word] = count
    return word_count


def get_source_word_count_info(source_name, topXwords):
    files = _get_files_with(f"results/{source_name}","*.txt")

    word_count_file = {}
    word_count_source = {source_name: {}}
    words_count = {}
    for file in files:
        word_count = convert_to_dictionary(file)
        word_count_file[os.path.basename(file)] = word_count
        for word in word_count:
            if word in list(words_count.keys()):
                words_count[word] += int(word_count[word])
            else:
                words_count[word] = int(word_count[word])
        word_count_source[source_name].update(words_count)
        # sort words in each file word count separately: word_count_file
        # sort words in source word count: word_count_source
    # get topXwords from source
    word_count_topX = {word: word_count_source[source_name][word] for word in list(word_count_source[source_name])[0:topXwords]}
#TODO: fix topoXwords count

    return word_count_file, word_count_source, words_count, word_count_topX
        
# read file
# file = "results/drake/Allegro hand - left__Wonik Robotics__end effector.txt"

def save_to_json(filename, object):
    with open(f"results/{filename}.json", 'w') as fp:
        json.dump(object, fp)


sources = ["drake","matlab","oem","random","robotics-toolbox","ros-industrial"]
word_count_all = {}
word_count_sources = {}
word_count_sources_topXwords = {}
topXwords = 10
for source in sources:
    word_count_file, word_count_source, words_count, word_count_topX = get_source_word_count_info(source, topXwords)
    for word in words_count:
        if word in list(word_count_all.keys()):
            word_count_all[word] += int(words_count[word])
        else:
            word_count_all[word] = int(words_count[word])
    word_count_sources.update(word_count_source)
    word_count_sources_topXwords.update(word_count_topX)
    # sort words in total from all datasets word count: word_count_all
    # extract top 20 words from each source



# save to json files
save_to_json("word_count_sources",word_count_sources)
save_to_json("word_count_all",word_count_all)
save_to_json("word_count_sources_topXwords", word_count_sources_topXwords)


words_to_count = ['world','flange']
for source in word_count_sources:
    for word in words_to_count:
        if word in word_count_sources[source]:
            print(f"{word} count in {source}: {word_count_sources[source][word]}")
        else:
            print(f"{word} not in {source}")

