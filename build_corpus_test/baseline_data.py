import jieba
import jieba.analyse
import random
corpus_path = '/home/researcher/projects/T5fortextgeneration/baseline_easy_normal_hard_data/hard_data.txt'
save_path = '/home/researcher/projects/T5fortextgeneration/baseline_easy_normal_hard_data/hard_src_tgt.txt'
random.seed(0)

def organazation_src_tgt(corpus_path,save_path):
    with open(corpus_path,"r") as f, open(save_path,"w") as w:
        for line in f:
            line = line.strip()
            sen = line
            label = 'haha'
            random_num = random.randint(1,4)                #随机抽取关键字的数量
            keywords = jieba.analyse.textrank(sen,topK=random_num)           #textrank的效果要更好
            if len(keywords) == 0:              #未抽取到关键词
                continue
            true_order = []
            for keyword in keywords:
                index = sen.find(keyword)
                temp_tuple = (keyword,index)
                true_order.append(temp_tuple)
            true_order.sort(key = lambda elem:elem[1])      #将关键字顺序调整为按照原句顺序
            word_list = []
            for word,index in true_order:
                word_list.append(word)
            write_template(word_list,label,sen,w)

def write_template(word_list,label,sen,w):
    num = len(word_list)
    if num == 1:
        w.write("<a>{}<b>;".format(word_list[0]))   #▁<extra_id_0> id为250099,▁<extra_id_1> id为250098
    elif num == 2:
        w.write("<a>{}<b>{}<c>;".format(word_list[0],word_list[1]))
    elif num == 3:
        w.write("<a>{}<b>{}<c>{}<d>;".format(word_list[0],word_list[1],word_list[2]))
    elif num ==4:
        w.write("<a>{}<b>{}<c>{}<d>{}<e>;".format(word_list[0],word_list[1],word_list[2],word_list[3]))
    
    write_tgt(word_list,sen,label,w)

def write_tgt(word_list,sen,label,w):
    begin = 0
    segments = []
    for word in word_list:
        index = sen.find(word)
        segment = sen[begin:index]
        begin = index + len(word)
        segments.append(segment)
    segments.append(sen[begin:])
    num = len(segments)
    if num == 2:
        print(f'<a>{segments[0]}<b>{segments[1]}', file=w)
    elif num == 3:
        print(f'<a>{segments[0]}<b>{segments[1]}<c>{segments[2]}', file=w)
    elif num == 4:
        print(f'<a>{segments[0]}<b>{segments[1]}<c>{segments[2]}<d>{segments[3]}', file=w)
    elif num == 5:
        print(f'<a>{segments[0]}<b>{segments[1]}<c>{segments[2]}<d>{segments[3]}<e>{segments[4]}',file=w)
          
    
    
    
    

if __name__ == '__main__':
    organazation_src_tgt(corpus_path,save_path)
    

            