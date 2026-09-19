#this will serialise the badapple LR video and output
from itertools import batched

import cv2
import numpy as np


cam = cv2.VideoCapture("BadAppleLR.mp4")
currentframe = 0
with open('badapple.h','w') as f:
    f.write("const uint32_t BadApple[][4] = \n { \n")
    while (True):
        ret, frame = cam.read()
        if ret:
            #convert the frame to matrix
            # conc = ''.join([''.join(''.join([str(elem)]) for elem in row) for row in frame])
            # val = [hex(int(conc[i:i+32], 2)) for i in range(0, len(conc), 32)]
            # print(val)

            matx = np.asarray(frame)
            matx = matx[:,:,0]
            bin = matx > 128
            bin_full = bin.astype(int)
            bin_full = list(batched(bin_full.flatten(), 32))

            chunk1 = list(bin_full[0])
            chunk1 = ''.join(map(str, list(map(int, chunk1))))
            chunk1 = hex(int(chunk1, 2))

            chunk2 = list(bin_full[1])
            chunk2 = ''.join(map(str, list(map(int, chunk2))))
            chunk2 = hex(int(chunk2, 2))

            chunk3 = list(bin_full[2])
            chunk3 = ''.join(map(str, list(map(int, chunk3))))
            chunk3 = hex(int(chunk3, 2))

            f.write("{ \n")
            f.write('\t' + chunk1 + ',' + '\n')
            f.write('\t' + chunk2 + ',' + '\n')
            f.write('\t' + chunk3 + ',' + '\n')
            f.write('\t' + "33" + '\n')
            f.write("}, \n")
            currentframe = currentframe + 1
        else:
            f.write("}; \n")
            break
    cam.release()
    cv2.destroyAllWindows()