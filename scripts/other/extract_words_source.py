import pandas as pd
import os
from helper_functions import _get_files_with

def _strip_out(words, filters=[]):
    for filter in filters:
        words = [word.split(filter) for word in words] # filter out strip
        words = [word for word_list in words for word in word_list]
    return words

def _remove_numbers(words):
    only_words = []
    for word in words:
        if word[-1] == "e":
            try:
                float(word[:-1])
            except:
                only_words.append(word)
        else:
            try:
                float(word)
            except:
                only_words.append(word)
        
    return only_words

search_dir = "urdf_files/"
sources = [name for name in os.listdir(search_dir) if os.path.isdir(f"{search_dir}/{name}")]
df_source_words = pd.DataFrame(columns=["source","word count"])

word_count_sources = {source: 0 for source in sources}
for source in sources:
    urdf_files = _get_files_with(f"{search_dir}/{source}", "*.urdf")
    word_count_source = {}
    for urdf_file in urdf_files:
        with open(urdf_file) as f:
            urdf = f.read()

        all_lines = urdf.splitlines()
        words = []
        for a in all_lines:
            a = a.strip("<")
            a = a.strip(">")
            words.append(a.split(" "))

        words = [word.lower() for word_list in words for word in word_list]
        words = _strip_out(words, ["/",">","<","=","[","]","!",'"',"-",",","?",".","(",")","_",":","$",";","\\","#"],)
        words = [word for word in words if len(word) > 0] # filter out ''
        words = _remove_numbers(words)

        word_count = {}
        unique_words = set(words)
        for kw in unique_words:
            if kw in word_count_source:
                word_count_source[kw] += words.count(kw)
            else:
                word_count_source[kw] = words.count(kw)
    word_count_sources.update({source: word_count_source})
    df_source_words = pd.concat([df_source_words, pd.Series({'source': source, 'word count': word_count_source}).to_frame().T], ignore_index=True)

specific_words = ["world","flange"]
specific_words_cols = specific_words.copy()
specific_words_cols.insert(0,"source")
data = [[c1,0,0] for c1 in sources]
df_source_specific_words = pd.DataFrame(data, columns=specific_words_cols)


for source in sources:
    for word in specific_words:
        if word in word_count_sources[source]:
            df_source_specific_words.loc[df_source_specific_words.source == source,word] = int(word_count_sources[source][word])


df_source_words.to_csv("df_source_words.csv",index=False)
df_source_specific_words.to_csv("df_source_specific_words.csv",index=False)