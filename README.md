# inverted-index-generation-and-boolean-retrieval-model-for-hindi
This repository is a part of information Retrieval which consist of inverted index generation script written in python which generates inverted index and save it in a text file. 
The dataset file used in this model is a freely available 'dand_prakriya.xlsx' file.
..................................Below are the description of each files...................................
# Dand_Prakriya.xlsx
This is the dataset file which contains indian government rule in each shell (both in hindi and english).
# hindi_tokeniser.py
This python file read the xlsx file and do following two things. 
     1. Tokenisetion
     2. Stop word removal
     3. Token counting
     4. Generates the hindi_tokens.txt file.
# hindi_inverted_index_generator.py
This model takes each token and extract those documents in which that token appears and apend those
document ids to the dictionary with token as 'key' and document ids as 'values'.
and finally save the key-value pairs from dictionay onto a file named 'hindi_inverted_index.txt'.

# booleanModelForHindi.py
This model extract the relavent document from the Dand_Prakriya.xlsx file based on boolean quary.
quary can be of three types.
   1.'token1' AND 'token2'
   2.'token1' OR 'token2'
   3.'token1' NOT 'token2'
