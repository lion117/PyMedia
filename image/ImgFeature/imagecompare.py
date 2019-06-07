#coding:gbk

import sys
import time,logging
from functools import wraps
import cv2
import numpy as np
logger = logging.getLogger()
_debug = False
def dprint(*st):
    if _debug:
        print st

def timefun(func):
    '''
    usage:
        Decorator print the execution time.
        @timefun
        def func():
            dosomething()

    '''
    # if _debug is not True:
    #     return
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__," time cost:" ,end-start)
        return result
    return wrapper

def matchTemp_img(im,tempim):
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
    method = methods[1]
    try:
        res = cv2.matchTemplate(tempim,im,method)#使用模板匹配最佳位置
    except:
        # cv2.imwrite(r"c:\tempim.png",tempim)
        # cv2.imwrite(r"c:\im.png",im)
        sys.exit()
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc,min_val
    else:
        top_left = max_loc,max_val
    # w,h = tempim.shape[::-1]
    # bottom_right = (top_left[0][0] + w, top_left[0][1] + h)
    # cv2.rectangle(im,top_left[0], bottom_right, (255,0,0), 2)
    # cv2.imwrite("c:\\xxx.png",im)
    return top_left

def filter_matches(kp1, kp2, matches, ratio = 0.8):#https://www.zhihu.com/question/23371175
    mkp1, mkp2 = [], []
    for m in matches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            m = m[0]
            mkp1.append( kp1[m.queryIdx] )
            mkp2.append( kp2[m.trainIdx] )
    p1 = np.float32([kp.pt for kp in mkp1])
    p2 = np.float32([kp.pt for kp in mkp2])
    kp_pairs = zip(mkp1, mkp2)
    return p1, p2, kp_pairs

def explore_match(win, img1, img2, kp_pairs, status = None, H = None):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
    vis[:h1, :w1] = img1
    vis[:h2, w1:w1+w2] = img2
    vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

    if H is not None:
        corners = np.float32([[0, 0], [w1, 0], [w1, h1], [0, h1]])
        corners = np.int32(cv2.perspectiveTransform(corners.reshape(1, -1, 2), H).reshape(-1, 2) + (w1, 0))
        dprint('corners::',corners)
        cv2.polylines(vis, [corners], True, (0, 0, 255))

    if status is None:
        status = np.ones(len(kp_pairs), np.bool)
    p1 = np.int32([kpp[0].pt for kpp in kp_pairs])
    p2 = np.int32([kpp[1].pt for kpp in kp_pairs])+(w1, 0)

    green = (0, 255, 0)
    blue = (255, 0, 0)
    red = (0, 0, 255)
    white = (255, 255, 255)
    kp_color = (51, 103, 236)
    for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
        if inlier:
            col = blue#匹配的特征点
            cv2.circle(vis, (x1, y1), 2, col, -1)
            cv2.circle(vis, (x2, y2), 2, col, -1)
        else:
            col = red
            r = 2
            thickness = 1#未匹配的特征点
            cv2.line(vis, (x1-r, y1-r), (x1+r, y1+r), col, thickness)
            cv2.line(vis, (x1-r, y1+r), (x1+r, y1-r), col, thickness)
            cv2.line(vis, (x2-r, y2-r), (x2+r, y2+r), col, thickness)
            cv2.line(vis, (x2-r, y2+r), (x2+r, y2-r), col, thickness)
    vis0 = vis.copy()
    for (x1, y1), (x2, y2), inlier in zip(p1, p2, status):
        if inlier:
            cv2.line(vis, (x1, y1), (x2, y2), green)

    cv2.imshow(win, vis)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

sift = cv2.xfeatures2d.SIFT_create()
#sift = cv2.SURF() SURF/ORB由于图片太小，特征点太少
#sift = cv2.ORB()
bf = cv2.BFMatcher(cv2.NORM_L2)#It is good for SIFT, SURF etc .http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html?highlight=bfmatcher
#bf = cv2.BFMatcher(cv2.NORM_HAMMING2)
def compare_SIFT(im1,im2):
    kp1,des1 = sift.detectAndCompute(im1,None)
    kp2,des2 = sift.detectAndCompute(im2,None)
    #print 'kp2',kp2
    if kp2 == []:
        dprint('kp2 does not have the keypoint')
        return
    matches = bf.knnMatch(des1, des2, k=2)#KNNMatch，可设置K = 2 ，即对每个匹配返回两个最近邻描述符，仅当第一个匹配与第二个匹配之间的距离足够小时，才认为这是一个匹配。
    #print matches
    dprint ('kp1:',len(kp1))
    dprint( 'kp1:',len(kp2))
    p1,p2,kp_pairs = filter_matches(kp1,kp2,matches)
    dprint( "matches",len(kp_pairs))
    ratio = 0
    if min(len(kp1),len(kp2)):
        #ratio = (100*len(kp_pairs)/max(len(kp1),len(kp2)))
        ratio = (100*len(kp_pairs)/len(kp1))
    else:
        dprint("can't find SIFT point.")
    dprint ('sift match ratio--------->%.2f%%'%ratio)
    if len(kp_pairs)!=0:
        pass
    #explore_match('matches',im1,im2,kp_pairs)
    if _debug and len(kp_pairs)!=0:
        H,status = None,None
        if len(p1)>4:
            H,status = cv2.findHomography(p1, p2, cv2.RANSAC, 5.0)#先不考虑分辨率变化的情况，暂不使用RANSAC
            kp_pairs = [kpp for kpp, flag in zip(kp_pairs, status) if flag]
            dprint( "RANSAC kp_pairs:",status.sum())
        #explore_match('matches',im1,im2,kp_pairs,status,H)

    if ratio>100:
        cv2.imwrite(r"c:\xxx.png",im2)
    return ratio
def FindImgFromImg(img1,img2):
    '''

    :param img1: 小图
    :param img2: 大图
    :return: 大图中找小图，找到最佳匹配，返回匹配率及坐标
    '''
    bestpos,val = matchTemp_img(img1,img2)
    dprint("val",val)
    x,y = bestpos
    dprint ('find the best point: x:%s,y:%s'%(x,y))
    #print 'img2:shape',img2.shape#shape为(长,宽)
    imgtemp = img2[y:y+img1.shape[0],x:x+img1.shape[1]]#cv2 crop ：y1:y2,x1:x2
    #print 'img1',img1.shape
    if compare_SIFT(img1,imgtemp) > 30:
        return True,bestpos#匹配则返回位置
    else:
        return False,(None,None)#不匹配则返回False


if __name__ == "__main__":
    # imread(image,0)灰度图模式加载一副彩图
    _debug = True
    img1 = cv2.imread(r"C:\Users\billduan\Desktop\small.png",0)
    img2  = cv2.imread(r"C:\Users\billduan\Desktop\big.png",0)
    FindImgFromImg(img1,img2)


