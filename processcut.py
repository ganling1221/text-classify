#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os 
import jieba 
import re 

positive_examples = []
negative_examples = []
for file in os.listdir('positive'):
    file = open('./positive/'+file, 'r', encoding='gbk')
    for line in file.readlines():
        line1 = re.sub(r"[～·：+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！!，,.;:?。？、~@#￥%……&*（）]+", "", line) 
        positive_examples.append(line1.strip())
for file in os.listdir('negative'):
    file = open('./negative/'+file, 'r', encoding='gbk')
    for line in file.readlines():
        line1 = re.sub(r"[～·：+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！!，,.;:?。？、~@#￥%……&*（）]+","", line)
        negative_examples.append(line1.strip())
       
pos_list = [jieba.lcut(s,cut_all =False) for s in positive_examples]
neg_list = [jieba.lcut(s,cut_all =False) for s in negative_examples]

pos = open("pos.txt", mode='w')
for s in pos_list:
    pos.write(' '.join(s) + "\n")
pos.close()
neg = open("neg.txt", mode='w')
for s in neg_list:
    neg.write(' '.join(s)+"\n")
neg.close()
