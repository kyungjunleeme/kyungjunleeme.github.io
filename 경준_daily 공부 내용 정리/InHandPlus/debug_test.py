import json
import pandas as pd
from pandas import DataFrame
import numpy as np

'''bbox[0] = 'ymin'
   bbox[1] = 'xmin'
   bbox[2] = 'ymax'
   bbox[3] = 'xmax'
# 0: ymin, 1: xmin, 2: ymax, 3: xmax'''
# colum_list = ['filename', 'obj_list', 'obj_sum_cnt']
# ans_obj_list=[]
object_list = []

# row_list = []

# per_file_per_object_info_list = []

df = DataFrame(columns=('filename', 'obj_sum_cnt','obj_list'))





def mk_file_list(source_file):
    with open(source_file) as json_file:
        json_data = json.load(json_file)
        file_name_list = list(json_data)
        for idx, filename in enumerate(file_name_list):
            file_info = json_data[filename]
            object_list[:]=[]
            print(file_info)
            obj_cnt_list = list(file_info)
            obj_cnt = len(obj_cnt_list)
            print(obj_cnt_list)
            for obj_idx in obj_cnt_list[:]:
                try:
                    pop_ele = obj_cnt_list.pop(len(obj_idx)-1)
                    object_list.append(file_info[pop_ele]['name'])
                    if not obj_cnt_list:
                        print(filename, obj_cnt, object_list)
                        print(df)
                        df.loc[idx] = [filename, obj_list, obj_sum_cnt]
                    else:
                        print('아직' + obj_idx+"발(+1)"+'발 남았다')
                except:
                    ''' pop_ele에 원소 없으면 오류 발생할테니 '''
                    continue

if __name__ == '__main__':
    mk_file_list('object_list_test.json')
