#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#            Phật phù hộ, không bao giờ BUG
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


import cv2
import argparse

from ultralytics import YOLO
import supervision as sv
import numpy as np




def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="YOLOv8 live")
    parser.add_argument(
        "--webcam-resolution", 
        #default=[1280, 720], 
        default=[640, 640], 
        nargs=2, 
        type=int
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    frame_width, frame_height = args.webcam_resolution

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    model = YOLO("best_2.pt")

    box_annotator = sv.BoxAnnotator(
        thickness=1,
        text_thickness=1,
        text_scale=1
    )


    while True:
        ret, frame = cap.read()

        result = model(frame, agnostic_nms=True, conf=0.6)[0]

        detections = sv.Detections.from_yolov8(result)
        
        
        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f} "
            for _, confidence, class_id, _
            in detections
        ]
        frame = box_annotator.annotate(
            scene=frame, 
            detections=detections, 
            labels=labels
        )
        radius = 5
        color = (255, 0, 0)
        
        '''Đánh trọng tâm của vật'''
        '''
        for item in detections:
            x = int((item[0][2] + item[0][0])/2)
            y = int((item[0][3] + item[0][1])/2)
           

            print(x, y)
            print(item[0])
            cv2.circle(frame, (x, y), radius, color, -1)
            #cv2.circle(frame, (x2, y2), radius, color, -1)
        '''
        max_acreage_box = 0
        x, y = 0, 0
        for item in detections:
            acreage_box = (item[0][2] - item[0][0]) * (item[0][3] + item[0][1])
            if (acreage_box > max_acreage_box):
                max_acreage_box = acreage_box
                x = int((item[0][2] + item[0][0])/2)
                y = int((item[0][3] + item[0][1])/2)
        cv2.circle(frame, (x, y), radius, color, -1)

            
        
        

        cv2.imshow("yolov8", frame)

        if (cv2.waitKey(30) == 27):
            break



if __name__ == "__main__":
    main()
