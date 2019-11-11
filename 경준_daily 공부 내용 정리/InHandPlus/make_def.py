import json
import pandas as pd
import numpy as np

'''bbox[0] = 'ymin'
   bbox[1] = 'xmin'
   bbox[2] = 'ymax'
   bbox[3] = 'xmax'
# 0: ymin, 1: xmin, 2: ymax, 3: xmax'''
'''
def class_text_to_int(row_label):
if row_label == 'hand':
return 1
elif row_label == 'grab_bottle_hand':
return 2
elif row_label == 'face':
return 3
elif row_label == 'mouth':
return 4
elif row_label == 'open_mouth':
return 5
elif row_label == 'bottle':
return 6
elif row_label == 'open_bottle':
return 7
elif row_label == 'cap':
return 8
elif row_label == 'pill':
return 9
elif row_label == 'cup':
return 10
else:
None
'''
colum_list = ['json_soruce','filename', 'width', 'height', 'obj_name', 'xmin', 'ymin', 'xmax', 'ymax', 'score', 'obj_idx']

# row_list = []

# per_file_per_object_info_list = []


def json_per_obj_make(jsonfile):
    with open(jsonfile) as json_file:
        json_data = json.load(json_file)
        file_name_list = list(json_data)         
        for filename in file_name_list:
            '''파일 1개당 json 정보'''
            '''case_1: json 정보 있는 경우 _ case_2: json 정보 없는 경우'''
            file_json_info = json_data[filename]
            if not file_json_info:
                    json_source = jsonfile
                    obj_name = 'Null'
                    obj_idx = 'Null'
                    score = 'Null'
                    ymin = 'Null'
                    xmin = 'Null'
                    ymax = 'Null'
                    xmax = 'Null'
                    width = 'Null'
                    height = 'Null'
                    global df
                    df = pd.DataFrame(columns=colum_list)

                    df = df.append(pd.DataFrame([[filename+'_', width, height, obj_name, xmin, ymin, xmax, ymax, score, obj_idx]], columns=colum_list), ignore_index=True)
                    print(df)
            else:
                '''파일 1개당 감지된_되어야하는_object 갯수'''
                obj_cnt_list = list(file_json_info)
                print(obj_cnt_list)
                '''per_obj_cnt 수정 필요(삭제)'''
                per_obj_cnt = len(obj_cnt_list)
                for i in obj_cnt_list:
                    final_info = file_json_info[i]
                    print(final_info)
                    try:
                        json_source = jsonfile
                        obj_name = final_info['name']
                        obj_idx = final_info['obj']
                        score = final_info['score']
                        ymin = final_info['bbox'][0]
                        xmin = final_info['bbox'][1]
                        ymax = final_info['bbox'][2]
                        xmax = final_info['bbox'][3]
                        width = final_info['size'][0]
                        height = final_info['size'][1]
                        global df
                        df = pd.DataFrame(columns=colum_list)

                        df = df.append(pd.DataFrame([[filename+'_', width, height, obj_name, xmin, ymin, xmax, ymax, score, obj_idx]], columns=colum_list), ignore_index=True)
                    
                    except:
                        pass

        
        
        '''(위에서 json 정보 없는 경우에서 걸러짐) case_1: object 있는경우 // case_2: object 없는 경우'''
        
        '''json 내 obj, name, score, bbox, size'''


if __name__ == '__main__':
    print('This program is being run by itself')
    json_per_obj_make('object_list.json')
else:
    print('I am being imported from another module')