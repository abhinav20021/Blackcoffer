import string
import re
import pandas as pd
import nltk
from nltk.tokenize import  word_tokenize
nltk.download('punkt')
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rising-it-cities-and-its-impact-on-the-economy-environment-infrastructure-and-city-life-by-the-year-2040-2/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))#To remove punctuation from files
with open("blackassign0001.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rising-it-cities-and-their-impact-on-the-economy-environment-infrastructure-and-city-life-in-future/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
for tag in div_bs4:
    s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0002.txt",'w') as file:
  file.write(regex.sub('', s))

from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/internet-demands-evolution-communication-impact-and-2035s-alternative-pathways/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
for tag in div_bs4:
    s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0003.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-in-upcoming-future/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0004.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/ott-platform-and-its-impact-on-the-entertainment-industry-in-future/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0005.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/ott-platform-and-its-impact-on-the-entertainment-industry-in-future/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0005.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/ott-platform-and-its-impact-on-the-entertainment-industry-in-future/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-cyber-crime-and-its-effects/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0006.txt",'w') as file:
  file.write(regex.sub('', s))
with open("blackassign0007.txt",'w') as file:
  file.write(regex.sub('', s))
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0005.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/the-rise-of-the-ott-platform-and-its-impact-on-the-entertainment-industry-by-2040/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0006.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-internet-demand-and-its-impact-on-communications-and-alternatives-by-the-year-2035-2/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0008.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-by-the-year-2040-2/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0009.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-cybercrime-and-its-effect-by-the-year-2040/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0010.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-internet-demand-and-its-impact-on-communications-and-alternatives-by-the-year-2035/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0011.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-3-2/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0012.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-e-health-and-its-impact-on-humans-by-the-year-2030/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0013.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030-2/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0014.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030-2/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0014.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0015.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-telemedicine-and-its-impact-on-livelihood-by-2040-2-2/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0016.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-chatbots-and-its-impact-on-customer-support-by-the-year-2040/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0017.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-e-health-and-its-imapct-on-humans-by-the-year-2030/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0018.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/how-does-marketing-influence-businesses-and-consumers/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0019.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/how-advertisement-increase-your-market-value/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0020.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/negative-effects-of-marketing-on-society/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0021.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/how-advertisement-marketing-affects-business/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0022.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rising-it-cities-will-impact-the-economy-environment-infrastructure-and-city-life-by-the-year-2035/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0023.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-ott-platform-and-its-impact-on-entertainment-industry-by-the-year-2030/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0024.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-ott-platform-and-its-impact-on-entertainment-industry-by-the-year-2030/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0025.txt",'w') as file:
  file.write(regex.sub('', s))

from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/rise-of-electric-vehicle-and-its-impact-on-livelihood-by-the-year-2040/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0026.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/oil-prices-by-the-year-2040-and-how-it-will-impact-the-world-economy/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0027.txt",'w') as file:
  file.write(regex.sub('', s))
from bs4 import BeautifulSoup
import requests
res=requests.get("https://insights.blackcoffer.com/an-outlook-of-healthcare-by-the-year-2040-and-how-it-will-impact-human-lives/")
soup=BeautifulSoup(res.content,"html.parser")
soup.pre.decompose()#To remove the pre tag
s=""
s+=soup.find('title').text[:-23]
div_bs4=soup.find_all('div',class_='td-post-content tagdiv-type')
#print(div_bs4)
for tag in div_bs4:
  s+=tag.text
regex = re.compile('[%s]' % re.escape(string.punctuation))
with open("blackassign0028.txt",'w') as file:
  file.write(regex.sub('', s))














#For creating positive words list and negative word list

with open("positive-words.txt","r") as file2:
  r=file2.read()
positive_words=r.split("\n")
print("Positive words:-"f'{positive_words}')
with open("negative-words.txt","rb") as file1:
  r2=file1.read()
r2=str(r2)[2:]
negative_words=r2.split("\n")
print("Negative words:-"f'{negative_words}')

#Creating Stop Words list

with open("StopWords_Auditor.txt","r") as file2:
  r=file2.read()
stop_words=r.split()
with open("StopWords_Names.txt","r") as file2:
  r=file2.read()
stop_words.append(r[:5])
stop_words.extend(r[90:].split())
with open("StopWords_Generic.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
with open("StopWords_GenericLong.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
with open("StopWords_DatesandNumbers.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
with open("StopWords_Geographic.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
with open("StopWords_Currencies.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
stop_words=[x.lower() for x in stop_words]

with open("StopWords_Auditor.txt","r") as file2:
  r=file2.read()
stop_words=r.split()
with open("StopWords_Names.txt","r") as file2:
  r=file2.read()
stop_words.append(r[:5])
stop_words.extend(r[90:].split())
with open("StopWords_Generic.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
with open("StopWords_GenericLong.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
with open("StopWords_DatesandNumbers.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
with open("StopWords_Geographic.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
with open("StopWords_Currencies.txt","r") as file2:
  r=file2.read()
stop_words.extend(r.split())
stop_words=[x.lower() for x in stop_words]
print(stop_words)
df = pd.read_excel("/content/Input.xlsx")
for i in range(100):
  df['URL_ID'][i]=df['URL_ID'][i]+".txt"

#Removing Stop words

def remove_stopwords(l):
  ans=[]
  for i in l:
    i=i.lower()
    if i not in stop_words and (i!="-" or i!="'" or i!='"') :
      ans.append(i)
  return ans

#Tokenizing the paragraphs and removing stop words

d={}
d_wstop={}
for i in range(100):
  with open(df["URL_ID"][i].lower(),"r") as file1:
    r=file1.read()
    l=word_tokenize(r)
    d_wstop[df["URL_ID"][i]]=l #Dictionary containing all the tokenized words
    d[df["URL_ID"][i]]=remove_stopwords(l) #Dictionary by removing stop words

#Defining scoring Functions


def positive_score(l):
  c=0
  for i in l:
    i=i.lower()
    if i in positive_words:
      c+=1
  return c
def negative_score(l):
  c=0
  for i in l:
    i=i.lower()
    if i in negative_words:
      c+=1
  return c
def count_pp(s):
  pronounRegex = re.compile(r'\b(I|we|my|ours|you|me|he|she|he|his|her|their|him|(?-i:us))\b',re.I)
  pronouns = pronounRegex.findall(s)
  return len(pronouns)
def avg_wordlength(l):
  c=0
  for i in l:
    c+=len(i)
  return round(c/len(l),2)
from nltk.tokenize import SyllableTokenizer
def count_syllable(l):
  c=0
  c1=0
  tk=SyllableTokenizer()
  for i in l:
    s=""
    for j in i:
      if j not in ['₹','ï','•','…','ü','″','—','”','“','–','’','‘']:
        s+=j
    c1+=len(tk.tokenize(s))
    if len(tk.tokenize(s))>2:
      c+=1
  return (c,c1)
def word_count(l):
  c=0
  for i in l:
    if i not in ['₹','ï','•','…','ü','″','—','”','“','–','’','‘']:
      c+=1
  return c

#Complex word percentage
per_cw=[0]*100
for i in range(100):
  per_cw[i]=round(((complex_c[i]/w_count[i])*100),2)
#For calculating sentences
t_s_l=[]
avg_sen_length=[0]*100#total sentence length
for i in range(100):
  with open(df["URL_ID"][i],"r") as file1:
    t_s_l.append(len(file1.readlines()))
  avg_sen_length[i]=round(w_count[i]/t_s_l[i],2)

#FOG Index
fog_in=[0]*100
for i in range(100):
  fog_in[i]=0.4*(avg_sen_length[i]+per_cw[i])

#Defining Output lists

positive=[]
negative=[]
polarity=[]
subjectivity=[]
personal_pronoun=[]
avg_word=[]
complex_c=[]
sy_c_pw=[]
w_count=[]

#Calculating the scores
for i in range(100):
  x=positive_score(d[df["URL_ID"][i]])
  y=negative_score(d[df["URL_ID"][i]])
  personal_pronoun.append(count_pp("".join(d_wstop[df["URL_ID"][i]])))
  positive.append(x)
  negative.append(y)
  polarity.append((x-y)/(x+y+0.000001))
  subjectivity.append(round((x+y)/(len(d[df["URL_ID"][i]])+0.000001),3))
  complex_c.append(count_syllable(d[df["URL_ID"][i]])[0])
  sy_c_pw.append(count_syllable(d[df["URL_ID"][i]])[1])
  avg_word.append(avg_wordlength(d[df["URL_ID"][i]]))
  w_count.append(word_count(d[df["URL_ID"][i]]))

#Output Data Frame
d2={'URL':df["URL_ID"],'positive_score':positive,'negative_score':negative,'polarity_score':polarity,"subjectivity":subjectivity,"personal_pronoun":personal_pronoun,"Average word Length":avg_word,"Complex word Count":complex_c,"Syllable count per word":sy_c_pw,"Word Count":w_count,"Average sentence length":avg_sen_length,"Percentage of complex words":per_cw,"Fog_index":fog_in}
df1=pd.DataFrame(d2)
df1.shape

#Creating an output file
datatoexcel = pd.ExcelWriter('Output.xlsx')
 # write DataFrame to excel
df1.to_excel(datatoexcel)
 # save the excel
datatoexcel.save()
     
