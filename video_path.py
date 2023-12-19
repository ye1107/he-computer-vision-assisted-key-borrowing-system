#plate_name = "plate_detection_2_1110607"
plate_name = "plate_detection_2"
date = "1110607"
video_name = "starbuck_car_moto"
img_path = "C:/Users/F728-B/Desktop/test_img/test_all.jpg"
video_path = "D:/MP4/original/new_video/" + video_name + ".mp4"
"""
cgu_car
cgu_moto
costco_car
costco_moto
nptu_car
nptu_car_2
nptu_car_3
nptu_moto_1
nptu_moto_2
ntsu_car
ntsu_car_moto
ntsu_moto
starbuck_car_moto
"""

"""
for date
2 = "1110607"
small = "1110517"
"""
"""
for path
2    plate_detection_2
small = plate_recognition
"""
print("v4影片")
print("darknet detector demo plate/" + plate_name + "/" + plate_name + "_" + date + ".data " + "plate/" + plate_name + "/" + plate_name + "_" + date + ".cfg " + "plate/" + plate_name + "/backup" + "/" + plate_name + "_" + date + "_final.weights " + video_path + " -out_filename " + video_name + ".mp4")
print("v4圖片")
print("darknet detector demo plate/" + plate_name + "/" + plate_name + "_" + date + ".data " + "plate/" + plate_name + "/" + plate_name + "_" + date + ".cfg " + "plate/" + plate_name + "/backup" + "/" + plate_name + "_" + date + "_final.weights" + " -ext_output " + img_path)
print("v7影片(大框)")
print("python detect.py --weights D:/yolov7/yolov7-main/runs/train/plate/plate_detection_v7_2/weights/best.pt --conf 0.25 --img-size 640 --source " + video_path)
print("v7圖片(大框)")
print("python detect.py --weights D:/yolov7/yolov7-main/runs/train/plate/plate_detection_v7_2/weights/best.pt --conf 0.25 --img-size 640 --source " + img_path)
print("v7影片(小框)")
print("python detect.py --weights D:/yolov7/yolov7-main/runs/train/plate/plate_recognition_v7_2/weights/best.pt --conf 0.25 --img-size 640 --source " + video_path)
print("v7圖片(小框)")
print("python detect.py --weights D:/yolov7/yolov7-main/runs/train/plate/plate_recognition_v7_2/weights/best.pt --conf 0.25 --img-size 640 --source " + img_path)