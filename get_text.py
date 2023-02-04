# %%
from bs4 import BeautifulSoup
from tqdm import tqdm
import unicodedata

import os,sys
set_name = "2006_2008"
ori_folder = "E:/Dataset/FinNLP/Project_10k/rawdata/10k_files/" + set_name
save_folder = "E:/Dataset/FinNLP/Project_10k/all_text_in_data"

file_names = os.listdir( ori_folder )
done_file_names = os.listdir( save_folder )

miss_list = []

for file_name in tqdm(file_names):
    if file_name in done_file_names:
        continue
    web_path = ori_folder + "/"  + file_name

    try:
        soup=BeautifulSoup(open(web_path,encoding='utf-8'),features='html.parser')  #features值可为lxml
        content = soup.find_all(text=True)
        # content = soup.get_text() 不能用这个


        text = []
        for item in content:
            item = unicodedata.normalize('NFKC', item)
            item = item.replace("\n","")
            if item not in ['\n', ' ', '']:
                item = item.replace("\n","")
                item = item.replace("  "," ")
                text.append(item)

        save_path = save_folder + "/"  + file_name
        # save_path = save_folder + "/"  + file_name.replace("html","txt")
        with open(save_path,'w',encoding='utf-8')as file:
            file.write(" ".join(text))
    except:
        miss_list.append(web_path)
        continue

# %%
import pickle
save_folder = "D:/Projectach/金融_NLP_RA/10K_code"
pickle.dump(miss_list, open(f'{save_folder}/{set_name}.pickle', 'wb'))
