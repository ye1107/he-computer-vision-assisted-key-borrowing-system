import xml.etree.ElementTree as ET

xml_path = 'D:\\aug\\aug\\aug_big_xml\\'#xml位置
txt = open("D:/v7test/plate_detection_v7_2_6/txt/plate_detection_v7_2_6.txt", 'r')#txt位置
line = txt.read().splitlines()
#宣告區
cls_num = 0
correct = 0
notcorrect = 0
plate_num = 0
motorcycle_plate_num = 0
plate_num_correct = 0
motorcycle_plate_num_correct = 0
plate_num_wrong = 0
motorcycle_plate_num_wrong = 0
plate_num_empty = 0
motorcycle_plate_num_empty = 0
plate_precision = 0
motorcycle_plate_precision = 0
plate_recall = 0
motorcycle_plate_recall = 0

print(str(txt))#輸出txt檔名，好知道這是哪個模型
print("-----------------------------data---------------------------")#有錯的都在這下面

cls = str()

for i in range(len(line)):
    file_name = xml_path + (line[i].split('\t')[0])[25:-4] + '.xml'
    pred = line[i].split('\t')[1][8:]

    tree = ET.parse(file_name)
    root = tree.getroot()

    for child in root.iter('object'):
        cls = child.find('name').text

    if pred == cls:  # cls=原始xml的class，lable=辨識出的class
        correct += 1
    else:
        notcorrect += 1
        print(str(file_name)+'\t'+'cls:'+str(cls)+'\t'+'pred:'+str(pred))

    if cls == "plate":
        plate_num += 1
    elif cls == "motorcycle_plate":
        motorcycle_plate_num += 1

    if cls == "plate" and pred == "plate":
        plate_num_correct += 1

    elif cls == "plate" and pred == "motorcycle_plate":
        plate_num_wrong += 1

    if cls == "motorcycle_plate" and pred == "motorcycle_plate":
        motorcycle_plate_num_correct += 1

    elif cls == "motorcycle_plate" and pred == "plate":
        motorcycle_plate_num_wrong += 1

    if not pred and cls == 'plate':
        plate_num_empty += 1
    elif not pred and cls == 'motorcycle_plate':
        motorcycle_plate_num_empty += 1

    if cls:
        cls_num += 1

# for child in root.iter('object'):

#計算區
acc = (correct / len(line)) * 100
plate_fn = (plate_num_wrong + plate_num_empty)
motorcycle_fn = (motorcycle_plate_num_wrong + motorcycle_plate_num_empty)
plate_tn = (motorcycle_plate_num_correct + motorcycle_plate_num_empty)
motorcycle_tn = (plate_num_correct + plate_num_empty)
plate_tpr = (plate_num_correct / (plate_num_correct + plate_fn)) * 100
plate_fpr = (motorcycle_plate_num_wrong / (motorcycle_plate_num_wrong + plate_tn)) * 100
motorcycle_plate_tpr = (motorcycle_plate_num_correct / (motorcycle_plate_num_correct + motorcycle_fn)) * 100
motorcycle_plate_fpr = (plate_num_wrong / (plate_num_wrong + motorcycle_tn)) * 100
plate_precision = (plate_num_correct + motorcycle_plate_num_wrong)
motorcycle_plate_precision = (motorcycle_plate_num_correct + plate_num_wrong)
plate_recall = (plate_num_correct + plate_fn)
motorcycle_plate_recall = (motorcycle_plate_num_correct + motorcycle_fn)

#輸出區
print("-----------------------------acc----------------------------")
print("acc:" + str(acc) + '%')
print("總數(GT):" + str(cls_num))
print("辨識正確:", int(correct), "張")
print("辨識錯誤:", int(notcorrect), "張")
print("----------------------------plate---------------------------")
print("plate_total(GT):" + str(plate_num))
print("plate_tp:" + str(plate_num_correct))
print("plate_fn:" + str(plate_fn))
print("plate_fp:" + str(motorcycle_plate_num_wrong))
print("plate_tn:" + str(plate_tn)+'\n')
print("plate_empty:", str(plate_num_empty))
print("plate_wrong:" + str(plate_num_wrong))
print("----------------------motorcycle_plate----------------------")
print("motorcycle_plate_total(GT):" + str(motorcycle_plate_num))
print("motorcycle_plate_tp:" + str(motorcycle_plate_num_correct))
print("motorcycle_plate_fn:" + str(motorcycle_fn))
print("motorcycle_plate_fp:" + str(plate_num_wrong))
print("motorcycle_plate_tn:" + str(motorcycle_tn)+'\n')
print("motorcycle_plate_empty:" + str(motorcycle_plate_num_empty))
print("motorcycle_plate_wrong:" + str(motorcycle_plate_num_wrong))
print("--------------------------tpr&fpr---------------------------")
print("plate_tpr:" + str(plate_tpr) + '%')
print("plate_fpr:" + str(plate_fpr) + '%'+'\n')
print("motorcycle_plate_tpr:" + str(motorcycle_plate_tpr) + '%')
print("motorcycle_plate_fpr:" + str(motorcycle_plate_fpr) + '%')
print("---------------------precision&recall-----------------------")
print("plate_precision:" + str(plate_precision))
print("plate_recall:" + str(plate_recall)+'\n')
print("motorcycle_plate_precision:" + str(motorcycle_plate_precision))
print("motorcycle_plate_recall:" + str(motorcycle_plate_recall))
"""
print("--------------------------test------------------------------")
print("m_fn=me+mw:" , int(motorcycle_plate_num_wrong)+int(motorcycle_plate_num_empty))
print("m_e:" + str(motorcycle_plate_num_empty))
print("m_w:" + str(motorcycle_plate_num_wrong))
print("p_fn=pe+pw:" , int(plate_num_wrong)+int(plate_num_empty))
print("p_e:" + str(plate_num_empty))
print("p_w:" + str(plate_num_wrong))
"""
