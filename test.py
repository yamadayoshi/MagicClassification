out = "Fusing layers...\nModel Summary: 213 layers, 7015519 parameters, 0 gradients, 15.8 GFLOPs\nimage 1/1 /home/yoshi/Pictures/cards/grn-6-conclave-tribunal.jpg: 640x480 1 KHM, 1 Name, Done. (0.013s)\nSpeed: 0.3ms pre-process, 12.7ms inference, 1.2ms NMS per image at shape (1, 3, 640, 640)\nResults saved to ../../Apps/yolov5/runs/detect/exp38\n1 labels saved to ../../Apps/yolov5/runs/detect/exp38/labels"

try:
    result = list(filter(lambda f: "Results saved to" in f, out.split("\n")))[0].split("/")[-1]
except:
    result = ''

print(result)