#!/usr/bin/env python
# coding: utf-8

# # Importando dados do twitter em tempo real
# 
# - Vamos usar a biblioteca tweepy: <br>
#     https://docs.tweepy.org/en/stable/
# 

# In[1]:


import tweepy as tw
import pandas as pd
import sqlite3


# In[2]:


bearer_token = 'AAAAAAAAAAAAAAAAAAAAAChZZAEAAAAAAlQCiYRgRGTjzRQ1po57pv%2F01wY%3DliOreN8sZlFXNFUHUqd1Muv18zkmzHjtHpO2UhN5XqqTmxVMOj'
consumer_key = 'OWCAlenDa9vqb6BzuJui2HDlN'
consumer_secret = 'xFxybviIyTUjyJdUJDjrAMI9xfPhSsfn4kDfdlU2i0Q194ZeMv'
access_token = '1488328327081476100-pWRPZHouemNznjQxH7EWuCzZFUnUpA'
access_token_secret = 'm7NTr2M9g8RyOMqeb52QmmiU9dYCo7NzLM1RdJWPJqlnV'


# In[3]:


cliente = tw.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)


# In[4]:


con = sqlite3.connect('BD_Bbb.db')


# In[5]:


cur = con.cursor()


# In[6]:


print("Para fazer a pesquisa")
print("copie e cola o exemplo ao lado e depois adultera a data e a hora no momento q esta abrindo o programa para de inicio e de saida do programa")
print("_______________________________________________________________________________________________________________________________")
start = input('exemplo = 2022-02-25T06:01:01Z')
end = input('exemplo = 2022-02-25T13:01:01Z')


# In[7]:


resposta = cliente.search_recent_tweets(query='BBB',max_results=100,start_time=start,end_time=end)


# In[8]:


dados = resposta.data


# In[9]:


base = []


# In[10]:


for i in dados:
    
    linha = [0 for j in range(18)]
    
    linha[0] = i.text
    
    texto = i.text
    
    if('RT' in texto):
        posicao = texto.find(':')
        texto = texto[posicao+2:]
        linha[17] = 1
        
    linha[1] = 1 if ('laís caldas' in texto.lower() or 'lais caldas' in texto.lower() or 'laís' in texto.lower() or 'lais' in texto.lower()) else 0
    linha[2] = 1 if ('jessilane alves' in texto.lower() or 'jessilane' in texto.lower()) else 0
    linha[3] = 1 if ('eliezer' in texto.lower()) else 0
    linha[4] = 1 if ('eslovênia marques' in texto.lower() or 'eslovênia' in texto.lower() or 'eslovenia marques' in texto.lower() or 'eslovenia' in texto.lower()) else 0
    linha[5] = 1 if ('lucas bissoli' in texto.lower() or 'lucas' in texto.lower()) else 0
    linha[6] = 1 if ('arthur aguiar' in texto.lower() or 'arthur' in texto.lower()) else 0
    linha[7] = 1 if ('natália' in texto.lower() or 'natalia' in texto.lower()) else 0
    linha[8] = 1 if ('vinícius' in texto.lower() or 'vinicius' in texto.lower() or 'vyni' in texto.lower()) else 0
    linha[9] = 1 if ('pedro scooby' in texto.lower() or 'pedro' in texto.lower()) else 0
    linha[10] = 1 if ('paulo andré' in texto.lower() or 'paulo' in texto.lower() or 'paulo andre' in texto.lower()) else 0
    linha[11] = 1 if ('jade picon' in texto.lower() or 'jade' in texto.lower()) else 0
    linha[12] = 1 if ('douglas silva' in texto.lower() or 'douglas' in texto.lower()) else 0
    linha[13] = 1 if ('linn da quebrada' in texto.lower() or 'linn' in texto.lower()) else 0
    linha[14] = 1 if ('tiago abravanel' in texto.lower() or 'tiago' in texto.lower()) else 0
    linha[15] = 1 if ('larissa atalarissa' in texto.lower() or 'atalarissa' in texto.lower() or 'larissa' in texto.lower()) else 0
    linha[16] = 1 if ('gustavo' in texto.lower() or 'gustavo' in texto.lower()) else 0
    
    
    base.append(linha)


# In[11]:


baseBBB = pd.DataFrame(base)
baseBBB.columns = ['texto','lais','jessilane','eliezer','eslovênia','lucas','arthur','natália','vinícius','scooby','paulo','jade','douglas','lina','tiago','atalarissa','gustavo','RT']


# In[12]:


baseView = baseBBB.drop(['texto','RT'],axis=1)


# In[13]:


comentarios = baseView.sum().sort_values(ascending=False).to_list()


# In[14]:


participantes = baseView.sum().sort_values(ascending=False).index.to_list()


# In[15]:


base2 = pd.DataFrame(zip(participantes,comentarios))
base2.columns = ['pessoas','comentarios']


# In[16]:


total_comentarios = base2['comentarios'].sum()


# In[17]:


base2['perc'] = base2['comentarios']/total_comentarios


# In[18]:


base2['perc_acum'] = base2['perc'].cumsum()


# In[19]:


base2['perc_form'] = base2['perc'].map("{:.1%}".format)
base2['perc_acum_form'] = base2['perc_acum'].map("{:.1%}".format)


# In[20]:


previsao = base2[['pessoas','comentarios','perc_form','perc_acum_form']]
print(previsao)


# In[21]:


arquivo = open('bot_bbb.txt', 'w')
arquivo.write(f"{previsao}\n")
arquivo.close()      


# In[31]:


cur.execute('CREATE TABLE registros (texto TEXT,RT TEXT)')  


# In[ ]:





# In[ ]:





# In[ ]:




