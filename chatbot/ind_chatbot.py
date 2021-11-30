from newspaper import Article
import random # untuk membangkitkan nilai random
import nltk # tools untuk NLP
import string # untuk fungsi string
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics.pairwise import cosine_similarity 
import numpy as np
import warnings
warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)

article = Article('https://warstek.com/kabel-laut/')
article.download()
article.parse()
article.nlp()
corpus = article.text
print(corpus)

# Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) #A list of senetences

# Print the list of sentences
print(sentence_list)

#a function to return a random greeting response to a users greeting
def greeting_response(text):
    text = text.lower()
    
    #Bots greeting respone
    bot_greetings = ['halo','hai','yuhuu','*eyebrows up*']
    
    #Users greeting
    user_greetings = ['Haloo','Eh iyaa Haii','Hai','greetings','wassup']
    
    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)
        
    #Random response to greeting
    def gratitude_response(text):
        text=text.lower()
   
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    
    x = list_var        
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                #swap
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
                
    return list_index
# Creat Bots Response
def bot_response(user_input):
    user_input=user_input.lower()
    sentence_list.append(user_input)
    bot_response= ''
    cm=CountVectorizer().fit_transform(sentence_list)
    similarity_scores=cosine_similarity(cm[-1],cm)
    similarity_scores_list=similarity_scores.flatten()
    index=index_sort(similarity_scores_list)
    index=index[1:]
    response_flag=0
    
    j=0
    for i in range(len(index)):
        if similarity_scores_list[index[i]]>0.0:
            bot_response=bot_response+' '+sentence_list[index[i]]
            response_flag=1
            j=j+1
        if j>2:
            break

        if response_flag==0:
            bot_response=bot_response+" "+"Maaf, Saya tidak paham dengan yang anda tanyakan"

        sentence_list.remove(user_input) 

        return bot_response
#Start Chat
print("Doc Bot: Mau nanya apa kamu tentang kabel laut")

exit_list=['exit','bye','keluar','quit', 'sampai jumpa']

while(True):
    user_input=input()
    if user_input.lower() in exit_list:
        print('Doc Bot: Bye Bye Sampai jumpa lagi')
        break
    else:
        if greeting_response(user_input)!= None:
            print('Doc Bot: '+ greeting_response(user_input))
        else:
            print('Doc Bot: '+ bot_response(user_input))
