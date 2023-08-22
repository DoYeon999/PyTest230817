from tkinter import *

## 함수 선언 부분 ##


def loadImage(fname):
    global inImage, XSIZE, YSIZE
    fp = open(fname, 'rb')

    for i in range(0, XSIZE):
        tmpList = []
        for k in range(0, YSIZE):
            data = int(ord(fp.read(1)))
            tmpList.append(data)
            # 1) ord(fp.read(1)) 변수 출력
            print(f"1) ord(fp.read(1)): {data}")
        inImage.append(tmpList)

    fp.close()


def displayImage(image):
    global XSIZE, YSIZE
    rgbString = ""
    for i in range(0, XSIZE):
        tmpString = ""
        for k in range(0, YSIZE):
            data = image[i][k]
            tmpString += "#%02x%02x%02x " % (data, data, data)
            # 2) data 변수 출력
            # print(f"2) data: {data}")
        # 5) tmpString 변수 출력
        # print(f"5) tmpString: {tmpString}")
        rgbString += "{" + tmpString + "} "
    # 4) inImage 변수 출력
    # print(f"4) inImage: {inImage}")
    # 6) rgbString 변수 출력
    # print(f"6) rgbString: {rgbString}")


## 전역 변수 선언 부분 ##
window = None
canvas = None
XSIZE, YSIZE = 256, 256
inImage = []

## 메인 코드 부분 ##
window = Tk()
window.title("흑백 사진 보기")
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE/2, YSIZE/2), image=paper, state="normal")

filename = 'RAW/tree.raw'
loadImage(filename)

displayImage(inImage)

canvas.pack()
window.mainloop()

# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 43
# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 44
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 45
# 1) ord(fp.read(1)): 46
# 1) ord(fp.read(1)): 47
# 1) ord(fp.read(1)): 48
# 1) ord(fp.read(1)): 48
# 1) ord(fp.read(1)): 50
# 1) ord(fp.read(1)): 50
# 1) ord(fp.read(1)): 51
# 1) ord(fp.read(1)): 51
# 1) ord(fp.read(1)): 52
# 1) ord(fp.read(1)): 54
# 1) ord(fp.read(1)): 54
# 1) ord(fp.read(1)): 55
# 1) ord(fp.read(1)): 55
# 1) ord(fp.read(1)): 57
# 1) ord(fp.read(1)): 59
# 1) ord(fp.read(1)): 60
# 1) ord(fp.read(1)): 61
# 1) ord(fp.read(1)): 64
# 1) ord(fp.read(1)): 65
# 1) ord(fp.read(1)): 68
# 1) ord(fp.read(1)): 69
# 1) ord(fp.read(1)): 71
# 1) ord(fp.read(1)): 73
# 1) ord(fp.read(1)): 75
# 1) ord(fp.read(1)): 77
# 1) ord(fp.read(1)): 79
# 1) ord(fp.read(1)): 80
# 1) ord(fp.read(1)): 81
# 1) ord(fp.read(1)): 81
# 1) ord(fp.read(1)): 81
# .
# .
# .
# 2) data: 51
# 2) data: 51
# 2) data: 52
# 2) data: 52
# 2) data: 53
# 2) data: 53
# 2) data: 54
# 2) data: 55
# 2) data: 55
# 2) data: 56
# 2) data: 57
# 2) data: 59
# 2) data: 61
# 2) data: 62
# 2) data: 65
# 2) data: 67
# 2) data: 69
# 2) data: 72
# 2) data: 74
# 2) data: 77
# 2) data: 79
# 2) data: 81
# 2) data: 82
# 2) data: 81
# 2) data: 81
# 2) data: 81
# 2) data: 80
# 2) data: 79
# 2) data: 76
# 2) data: 74
# 2) data: 74
# 2) data: 73
# 2) data: 74
# 2) data: 72
# 2) data: 72
# 2) data: 72
# 2) data: 72
# 2) data: 71
# 2) data: 70
# 2) data: 69
# 2) data: 70
# 2) data: 68
# 2) data: 67
# 2) data: 65
# 2) data: 65
# 2) data: 66
# 2) data: 66
# 2) data: 67
# 2) data: 68
# 2) data: 70
# 2) data: 72
# 2) data: 72
# 2) data: 73
# 2) data: 72
# 2) data: 73
# 2) data: 73
# 2) data: 74
# 2) data: 74
# 2) data: 75
# 2) data: 76
# 2) data: 77
# 2) data: 78
# 2) data: 79
# 2) data: 79
# 2) data: 80
# 2) data: 83
# 2) data: 84
# 2) data: 84
# 2) data: 85
# 2) data: 84
# 2) data: 83
# 2) data: 82
# 2) data: 79
# 2) data: 76
# 2) data: 73
# 2) data: 71
# 2) data: 69
# 2) data: 66
# 2) data: 62
# 2) data: 65
# 2) data: 70
# 2) data: 64
# 2) data: 61
# 2) data: 60
# 2) data: 63
# 2) data: 63
# 2) data: 67
# 2) data: 68
# 2) data: 37
# 2) data: 38
# 2) data: 39
# 2) data: 41
# 2) data: 44
# 2) data: 44
# 2) data: 46
# 2) data: 47
# 2) data: 48
# 2) data: 50
# 2) data: 51
# 2) data: 51
# 2) data: 51
# 2) data: 51
# 2) data: 50
# 2) data: 48
# 2) data: 46
# 2) data: 45
# 2) data: 44
# 2) data: 42
# 2) data: 42
# 2) data: 40
# 2) data: 39
# 2) data: 41
# 2) data: 43
# 2) data: 46
# 2) data: 46
# 2) data: 46
# 2) data: 51
# 2) data: 54
# 2) data: 55
# 2) data: 54
# 2) data: 54
# 2) data: 53
# 2) data: 50
# 2) data: 46
# 2) data: 44
# 2) data: 43
# 2) data: 39
# 2) data: 32
# 2) data: 30
# 2) data: 29
# 2) data: 30
# 2) data: 29
# 2) data: 29
# 2) data: 29
# 2) data: 30
# 2) data: 29
# 2) data: 30
# 2) data: 31
# 2) data: 30
# 2) data: 30
# 2) data: 31
# 2) data: 32
# 2) data: 31
# 2) data: 30
# 2) data: 31
# 2) data: 31
# 2) data: 31
# 2) data: 31
# 2) data: 31
# 2) data: 31
# 2) data: 31
# 2) data: 30
# 2) data: 29
# 2) data: 28
# 2) data: 29
# 2) data: 29
# 2) data: 29
# 2) data: 29
# 2) data: 30
# 2) data: 29
# 2) data: 29
# 2) data: 29
# 2) data: 29
# 2) data: 29
# 2) data: 30
# 2) data: 30
# 2) data: 31
# 2) data: 34
# 2) data: 37
# 2) data: 41
# 2) data: 44
# 2) data: 46
# 2) data: 49
# 2) data: 52
# 2) data: 54
# 2) data: 56
# 2) data: 56
# 2) data: 56
# 2) data: 58
# 2) data: 58
# 2) data: 59
# 2) data: 60
# 2) data: 62
# 2) data: 63
# 2) data: 65
# 2) data: 65
# 2) data: 65
# 2) data: 66
# 2) data: 66
# 2) data: 68
# 2) data: 68
# 2) data: 70
# 2) data: 70
# 2) data: 71
# 2) data: 71
# 2) data: 72
# 2) data: 71
# 2) data: 72
# 2) data: 72
# 2) data: 72
# 2) data: 73
# 2) data: 72
# 2) data: 72
# 2) data: 71
# 2) data: 71
# 2) data: 72
# 2) data: 70
# 2) data: 70
# 2) data: 69
# 2) data: 69
# 2) data: 69
# 2) data: 69
# 2) data: 69
# 2) data: 69
# 2) data: 70
# 2) data: 70
# 2) data: 70
# 5) tmpString: #434343 #404040 #3b3b3b #363636 #313131 #2d2d2d #292929 #282828 #2a2a2a #2b2b2b #2b2b2b #2c2c2c #2c2c2c #2c2c2c #2d2d2d #2d2d2d #2e2e2e #2d2d2d #2d2d2d
# #2e2e2e #2e2e2e #2d2d2d #2c2c2c #2c2c2c #2c2c2c #2b2b2b #2c2c2c #2b2b2b #2c2c2c #2c2c2c #2c2c2c #2d2d2d #2e2e2e #2e2e2e #2f2f2f #303030 #313131 #323232 #333333 #333333 #333333 #343434 #343434 #353535 #353535 #363636 #373737 #373737 #383838 #393939 #3b3b3b #3d3d3d #3e3e3e #414141 #434343 #454545 #484848 #4a4a4a #4d4d4d #4f4f4f #515151 #525252 #515151 #515151 #515151 #505050 #4f4f4f #4c4c4c #4a4a4a #4a4a4a #494949 #4a4a4a #484848 #484848 #484848 #484848 #474747 #464646 #454545 #464646 #444444 #434343 #414141 #414141 #424242 #424242 #434343 #444444 #464646 #484848 #484848 #494949 #484848 #494949 #494949 #4a4a4a #4a4a4a #4b4b4b #4c4c4c #4d4d4d #4e4e4e #4f4f4f
# #4f4f4f #505050 #535353 #545454 #545454 #555555 #545454 #535353 #525252 #4f4f4f #4c4c4c #494949 #474747 #454545 #424242 #3e3e3e #414141 #464646 #404040 #3d3d3d #3c3c3c #3f3f3f #3f3f3f #434343 #444444 #252525 #262626 #272727 #292929 #2c2c2c #2c2c2c #2e2e2e #2f2f2f #303030 #323232 #333333 #333333 #333333 #333333 #323232 #303030 #2e2e2e #2d2d2d #2c2c2c #2a2a2a #2a2a2a #282828 #272727 #292929 #2b2b2b #2e2e2e #2e2e2e #2e2e2e #333333 #363636 #373737 #363636 #363636 #353535 #323232 #2e2e2e #2c2c2c #2b2b2b #272727 #202020 #1e1e1e #1d1d1d #1e1e1e #1d1d1d #1d1d1d #1d1d1d #1e1e1e #1d1d1d #1e1e1e #1f1f1f #1e1e1e #1e1e1e #1f1f1f #202020 #1f1f1f #1e1e1e #1f1f1f #1f1f1f
# #1f1f1f #1f1f1f #1f1f1f #1f1f1f #1f1f1f #1e1e1e #1d1d1d #1c1c1c #1d1d1d #1d1d1d #1d1d1d #1d1d1d #1e1e1e #1d1d1d #1d1d1d #1d1d1d #1d1d1d #1d1d1d #1e1e1e #1e1e1e #1f1f1f #222222 #252525 #292929 #2c2c2c #2e2e2e #313131 #343434 #363636 #383838 #383838 #383838 #3a3a3a #3a3a3a #3b3b3b #3c3c3c #3e3e3e #3f3f3f #414141 #414141 #414141 #424242 #424242 #444444 #444444 #464646 #464646 #474747 #474747 #484848 #474747 #484848 #484848 #484848 #494949 #484848 #484848 #474747 #474747 #484848 #464646 #464646 #454545 #454545 #454545 #454545 #454545 #454545 #464646 #464646 #464646
# .
# .
# .
# 5) tmpString: #404040 #3d3d3d #393939 #353535 #303030 #2c2c2c #282828 #292929 #292929 #2a2a2a #2b2b2b #2b2b2b #2c2c2c #2c2c2c #2d2d2d #2d2d2d #2e2e2e #2d2d2d #2d2d2d
# #2d2d2d #2e2e2e #2e2e2e #2d2d2d #2d2d2d #2c2c2c #2c2c2c #2c2c2c #2d2d2d #2d2d2d #2e2e2e #2e2e2e #2e2e2e #2f2f2f #2f2f2f #303030 #313131 #323232 #323232 #333333 #343434 #353535 #343434 #343434 #343434 #353535 #353535 #353535 #363636 #363636 #383838 #393939 #3b3b3b #3d3d3d #3f3f3f #414141 #444444 #464646 #4a4a4a #4c4c4c #4e4e4e #505050 #515151 #525252 #515151 #525252 #515151 #4f4f4f #4d4d4d #4b4b4b #4a4a4a #4a4a4a #4a4a4a #494949 #494949 #484848 #484848 #464646 #454545 #454545 #454545 #424242 #424242 #404040 #414141 #404040 #414141 #434343 #434343 #444444 #464646 #484848 #484848 #494949 #494949 #494949 #494949 #494949 #4b4b4b #4c4c4c #4c4c4c #4d4d4d #4e4e4e
# #4e4e4e #505050 #515151 #535353 #535353 #545454 #545454 #535353 #535353 #505050 #4d4d4d #4b4b4b #484848 #454545 #424242 #3d3d3d #444444 #484848 #424242 #3e3e3e #3d3d3d #3e3e3e #3f3f3f #454545 #424242 #242424 #252525 #262626 #282828 #2a2a2a #2b2b2b #2d2d2d #2e2e2e #303030 #313131 #313131 #323232 #323232 #323232 #313131 #2f2f2f #2d2d2d #2d2d2d #2c2c2c #292929 #282828 #272727 #272727 #282828 #2a2a2a #2d2d2d #2d2d2d #2e2e2e #323232 #363636 #363636 #353535 #353535 #343434 #313131 #2e2e2e #2d2d2d #2b2b2b #282828 #212121 #1e1e1e #1d1d1d #1e1e1e #1e1e1e #1d1d1d #1e1e1e #1d1d1d #1e1e1e #1e1e1e #1e1e1e #1e1e1e #1e1e1e #1f1f1f #1e1e1e #1f1f1f #1d1d1d #1f1f1f #1e1e1e
# #1f1f1f #1e1e1e #1e1e1e #1e1e1e #1f1f1f #1e1e1e #1d1d1d #1d1d1d #1c1c1c #1c1c1c #1c1c1c #1d1d1d #1d1d1d #1d1d1d #1d1d1d #1d1d1d #1c1c1c #1d1d1d #1e1e1e #1d1d1d #1e1e1e #212121 #232323 #272727 #292929 #2d2d2d #2f2f2f #313131 #343434 #363636 #373737 #373737 #393939 #3a3a3a #3b3b3b #3d3d3d #3e3e3e #3f3f3f #414141 #424242 #424242 #424242 #434343 #444444 #444444 #444444 #444444 #444444 #444444 #464646 #454545 #454545 #454545 #454545 #454545 #454545 #454545 #454545 #454545 #454545 #444444 #444444 #444444 #434343 #444444 #444444 #434343 #454545 #454545 #454545 #464646
# .
# .
# .
# 5) tmpString: #3c3c3c #3a3a3a #363636 #323232 #2f2f2f #2b2b2b #272727 #282828 #282828 #2a2a2a #2a2a2a #2b2b2b #2b2b2b #2c2c2c #2c2c2c #2d2d2d #2d2d2d #2d2d2d #2e2e2e
# #2e2e2e #2e2e2e #2e2e2e #2d2d2d #2e2e2e #2d2d2d #2e2e2e #2d2d2d #2d2d2d #2e2e2e #2e2e2e #2e2e2e #2e2e2e #2e2e2e #2f2f2f #313131 #313131 #313131 #323232 #333333 #333333 #333333 #333333 #343434 #333333 #343434 #343434 #343434 #343434 #353535 #363636 #373737 #393939 #3b3b3b #3d3d3d #3f3f3f #414141 #444444 #474747 #4a4a4a #4c4c4c #4e4e4e #4f4f4f #505050 #505050 #505050 #4e4e4e #4e4e4e #4e4e4e #4b4b4b #494949 #494949 #484848 #474747 #474747 #474747 #474747 #454545 #444444 #444444 #434343 #414141 #404040 #3f3f3f #404040 #3f3f3f #414141 #424242 #424242 #444444 #464646 #474747 #484848 #484848 #484848 #484848 #484848 #484848 #484848 #494949 #494949 #494949 #4a4a4a
# #4c4c4c #4e4e4e #4f4f4f #525252 #525252 #545454 #535353 #525252 #515151 #4f4f4f #4e4e4e #4c4c4c #494949 #464646 #424242 #3e3e3e #434343 #474747 #414141 #3c3c3c #3d3d3d #3e3e3e #404040 #484848 #3e3e3e #212121 #232323 #242424 #262626 #272727 #2a2a2a #2c2c2c #2d2d2d #2e2e2e #2f2f2f #303030 #303030 #313131 #313131 #303030 #2e2e2e #2d2d2d #2c2c2c #2b2b2b #292929 #282828 #272727 #262626 #262626 #2a2a2a #2c2c2c #2d2d2d #2d2d2d #303030 #353535 #363636 #353535 #343434 #333333 #303030 #2d2d2d #2c2c2c #2b2b2b #272727 #222222 #1f1f1f #1f1f1f #1e1e1e #1d1d1d #1d1d1d #1e1e1e #1d1d1d #1e1e1e #1e1e1e #1d1d1d #1e1e1e #1e1e1e #1e1e1e #1e1e1e #1e1e1e #1e1e1e #1e1e1e #1e1e1e
# #1e1e1e #1e1e1e #1e1e1e #1d1d1d #1d1d1d #1d1d1d #1d1d1d #1c1c1c #1b1b1b #1b1b1b #1c1c1c #1c1c1c #1c1c1c #1d1d1d #1c1c1c #1c1c1c #1c1c1c #1d1d1d #1e1e1e #1d1d1d #1e1e1e #1f1f1f #222222 #242424 #272727 #2a2a2a #2c2c2c #2f2f2f #323232 #353535 #363636 #373737 #383838 #3a3a3a #3c3c3c #3e3e3e #3f3f3f #414141 #424242 #424242 #434343 #424242 #434343 #434343 #434343 #434343 #424242 #424242 #414141 #424242 #404040 #414141 #404040 #414141 #424242 #424242 #424242 #434343 #424242 #424242 #424242 #424242 #424242 #414141 #424242 #434343 #434343 #454545 #454545 #464646 #464646
# 4) inImage: [[79, 81, 83, 85, 86, 86, 87, 86, 85, 85, 85, 82, 80, 78, 76, 74, 71, 71, 71, 72, 72, 76, 83, 89, 99, 105, 109, 114, 118, 122, 123, 126, 128, 130, 133, 136, 137, 140, 143, 146, 150, 154, 158, 160, 163, 165, 167, 167, 167, 168, 169, 169,
# 168, 165, 163, 161, 160, 159, 158, 155, 152, 149, 146, 144, 142, 141, 138, 135, 131, 130, 128, 128, 129, 128, 129, 128, 129, 130, 131, 132, 133, 135, 136, 136, 137, 138, 139, 139, 139, 138, 138, 137, 136, 134, 133, 131, 130, 129, 128, 130, 134, 137, 139, 142, 145, 148, 151, 155, 158, 161, 163, 165, 167, 167, 169, 170, 171, 172, 171, 171, 170, 171, 170, 169, 168, 168, 166, 166, 165, 165, 162, 162, 162, 161, 161,
# 161, 161, 161, 160, 160, 160, 158, 158, 157, 157, 156, 156, 157, 157, 156, 156, 157, 156, 156, 154, 155, 155, 155, 154, 154, 155, 156, 155, 155, 155, 155, 155, 154, 155, 155, 155, 155, 154, 154, 154, 154, 154, 153, 154, 153, 153, 154, 153, 153, 154, 154, 155, 155, 155, 155, 155, 156, 155, 155, 154, 155, 157, 156, 156, 157, 157, 159, 159, 159, 160, 161, 161, 161, 163, 163, 163, 165, 165, 166, 165, 167, 167, 167,
# 168, 169, 169, 170, 170, 170, 171, 170, 171, 171, 171, 170, 172, 171, 171, 172, 171, 171, 170, 170, 169, 169, 169, 170, 170, 170, 170, 170, 171, 171, 170, 170, 170, 171, 171, 170, 171, 171], [80, 82, 84, 87, 87, 87, 88, 87, 86, 84, 83, 79, 76, 75, 72, 71, 70, 69, 70, 71, 72, 72, 76, 81, 89, 96, 100, 103, 108, 111, 114, 115, 117, 121, 124, 126, 128, 133, 135, 140, 144, 148, 152, 155, 157, 159, 161, 161, 161, 162, 163, 162, 161, 158, 156, 154, 153, 151, 149, 149, 145, 142, 138, 135, 135, 133, 128, 124, 121, 118, 116, 116, 116, 117, 118, 118, 119, 118, 120, 121, 122, 124, 127,
# 128, 129, 130, 131, 133, 132, 132, 131, 130, 128, 127, 126, 123, 121, 120, 121, 123, 126, 129, 132, 136, 139, 142, 146, 150, 153, 156, 159, 162, 163, 166, 167, 168, 170, 170, 171, 171, 169, 169, 168, 166, 166, 164, 163, 162, 162, 161, 159, 158, 157, 157, 157, 157, 158, 158, 158, 157, 157, 156, 155, 155, 155, 154, 155, 156, 155, 156, 156, 156, 155, 155, 154, 154, 155, 155, 154, 155, 155, 155, 155, 155, 155, 156,
# 155, 156, 155, 155, 154, 154, 154, 154, 154, 154, 153, 153, 154, 152, 153, 153, 153, 153, 153, 153, 153, 154, 154, 155, 155, 155, 155, 154, 154, 154, 156, 156, 156, 157, 157, 158, 158, 160, 159, 160, 160, 161, 162, 163, 164, 164, 164, 165, 165, 165, 165, 167, 167, 168, 168, 168, 169, 169, 169, 169, 170, 170, 171, 170, 171, 171, 172, 171, 171, 170, 169, 168, 168, 168, 168, 168, 168, 168, 169, 170, 170, 170, 171,
# 171, 171, 171, 172, 170, 170, 170], [80, 82, 84, 86, 87, 88, 88, 86, 86, 84, 82, 79, 77, 74, 72, 71, 70, 69, 68, 69, 69, 69, 71, 75, 81, 87, 92, 95, 99, 101, 103, 103, 106, 109, 113, 117, 119, 124, 129, 136, 139, 143, 146, 150, 152, 154, 154, 154, 155, 155, 157, 156, 154, 151, 150, 147, 146, 145, 143, 141, 138, 133, 130, 126, 124, 123, 119, 114, 109, 105, 103, 102, 102, 103, 105, 107, 107, 107, 108, 111, 114, 115, 117, 119, 120, 120, 122, 124, 125, 125, 123, 122, 120, 118, 116, 114, 112, 111,
# 112, 115, 118, 121, 125, 128, 133, 136, 139, 143, 147, 152, 153, 157, 159, 163, 165, 166, 168, 169, 169, 168, 168, 167, 165, 163, 162, 159, 158, 157, 157, 154, 154, 154, 153, 153, 153, 153, 153, 153, 154, 153, 154, 152, 153, 153, 153, 153, 153, 154, 154, 155, 155, 154, 154, 154, 153, 154, 155, 154, 154, 154, 154, 154, 155, 154, 154, 155, 154, 154, 154, 154, 154, 153, 154, 153, 154, 153, 153, 153, 153, 153, 153,
# 153, 154, 154, 153, 152, 153, 154, 153, 153, 152, 152, 154, 154, 154, 154, 153, 155, 155, 155, 155, 156, 157, 158, 158, 159, 159, 160, 160, 161, 162, 163, 163, 163, 165, 165, 166, 166, 167, 167, 168, 168, 168, 169, 169, 169, 170, 170, 170, 169, 171, 171, 170, 171, 169, 168, 167, 167, 166, 165, 165, 165, 166, 167, 168, 167, 169, 170, 171, 170, 170, 170, 170, 171, 170, 171], [82, 84, 86, 87, 88, 88, 88, 87, 87, 84, 82, 79, 77, 75, 73, 72, 69, 70, 68, 68, 68, 68, 69, 72, 74, 79, 85, 86, 89, 92, 91, 93, 95, 98, 102, 106, 112, 118, 125, 132, 136, 138, 142, 145, 147, 149, 149, 149, 148, 149, 150, 150, 148, 145, 143, 140, 139, 137, 135, 132, 129, 123, 119, 115, 112, 110, 108, 103, 96, 91, 89, 89, 88, 91, 93, 95, 95, 94, 95, 99, 102, 104, 105, 108, 110, 112, 113, 116, 117, 117, 116, 116, 114, 111, 109, 107, 103, 101, 102, 104, 109, 113, 116, 121, 126, 130, 134, 138, 142, 146, 149, 153, 157, 160, 163, 165, 167, 168, 168, 167, 166, 164, 162, 159, 158, 156, 154, 153, 152, 150, 149, 149, 148,
# 148, 148, 149, 149, 149, 150, 149, 149, 150, 149, 150, 150, 150, 150, 150, 152, 153, 153, 153, 152, 153, 152, 154, 154, 153, 153, 153, 153, 153, 154, 153, 153, 153, 152, 153, 152, 152, 153, 152, 152, 151, 151, 152, 151, 152, 152, 152, 151, 152, 152, 152, 152, 152, 152, 153, 153, 152, 152, 152, 152, 152, 153, 153, 152, 152, 153, 153, 154, 154, 155, 156, 156, 157, 158, 158, 158, 159, 159, 161, 162, 162, 163, 163,
# 164, 164, 165, 165, 166, 167, 167, 167, 168, 168, 168, 168, 170, 168, 169, 170, 170, 169, 168, 167, 165, 164, 163, 162, 162, 163, 164, 165, 166, 168, 168, 169, 170, 170, 171, 170, 170, 171, 170, 170], [83, 84, 86, 87, 88, 88, 88, 87, 87, 85, 82, 79, 76, 74, 74, 71, 70, 69, 68, 67, 68, 67, 68, 70, 70, 73, 78, 80, 81, 82, 82, 83, 84, 89, 93, 98, 106, 113, 121, 127, 132, 136, 138, 141, 143, 145, 145, 142, 141, 141, 143, 144, 141, 138, 134, 133, 130, 128, 126, 122, 119, 112, 107, 102, 100, 98, 96, 90, 83, 76, 75, 75, 75, 78, 79, 81, 82, 82, 85, 87, 90, 92, 95, 99, 100, 102, 104, 107, 109, 109, 108, 107, 105, 104, 101, 98, 94, 92, 92, 95, 99, 104, 108, 113, 119, 123, 128, 133, 137, 142, 145, 149, 152, 157, 159, 162, 164, 165, 165, 164, 163, 162, 158, 156, 155, 151, 148, 147, 146, 145, 144, 143, 143, 142, 143, 143, 144, 145, 145, 145, 144, 144, 146, 146, 146, 147, 149, 149, 150, 151, 151, 151, 151, 150, 151, 152, 152, 152, 152, 152, 151, 151, 151, 152, 152, 152, 152, 152, 152, 151, 150,
# 150, 149, 150, 149, 150, 150, 150, 150, 151, 151, 151, 152, 153, 152, 152, 152, 152, 151, 152, 152, 153, 152, 153, 152, 152, 152, 152, 152, 152, 152, 154, 155, 154, 155, 156, 156, 157, 157, 159, 157, 158, 161, 161, 161, 163, 163, 163, 163, 165, 165, 165, 166, 166, 167, 166, 167, 166, 168, 168, 168, 169, 169, 167, 166, 163, 163, 161, 159, 158, 160, 161, 162, 164, 164, 166, 167, 168, 169, 169, 170, 170, 170, 170,
# 170, 170], [84, 86, 87, 87, 87, 87, 87, 86, 86, 85, 83, 80, 77, 75, 73, 72, 71, 70, 68, 68, 68, 67, 68, 69, 70, 70, 71, 74, 74, 75, 74, 76, 78, 82, 85, 92, 101, 110,
# 118, 124, 128, 132, 136, 137, 139, 141, 140, 138, 135, 135, 135, 135, 134, 131, 126, 124, 121, 118, 116, 111, 108, 101, 94, 89, 87, 85, 82, 77, 70, 64, 62, 62, 62, 64, 66, 68, 70, 71, 73, 76, 78, 82, 85, 88, 90, 93, 94, 98, 100, 100, 101, 99, 97, 96, 94, 91, 85, 82, 81, 85, 90, 95, 99, 103, 109, 115, 120, 126, 130, 135, 140, 144,
# 149, 153, 156, 160, 161, 162, 161, 161, 160, 158, 156, 152, 150, 147, 144, 143, 141, 139, 138, 138, 137, 137, 137, 138, 139, 140, 139, 140, 141, 142, 142, 144, 145, 145, 147, 147, 147, 148, 149, 150, 151, 149, 149, 149, 150, 151, 150, 149, 150, 150, 149, 149, 149, 150, 150, 149, 149, 148, 147, 148, 148, 148, 148, 147, 147, 148, 148, 149, 151, 150, 150, 152, 151, 151, 151, 152, 151, 151, 151, 150, 150, 151, 151,
# 153, 152, 152, 151, 152, 152, 152, 154, 154, 154, 155, 155, 156, 156, 157, 157, 158, 159, 158, 161, 161, 161, 162, 161, 163, 165, 164, 165, 164, 165, 164, 166, 167, 167, 167, 168, 167, 166, 166, 163, 160, 159, 158, 158, 157, 157, 156, 159, 160, 161, 163, 165, 166, 167, 169, 169, 169, 170, 170, 169, 170], [84, 86, 86, 86, 86, 86, 87, 86, 86, 85, 81, 79, 77, 76, 73, 71, 70, 69, 68, 66, 67, 67, 68, 68, 69, 68, 70,
# 69, 70, 71, 72, 72, 74, 78, 83, 90, 98, 108, 115, 120, 124, 129, 133, 135, 136, 137, 135, 132, 129, 128, 129, 128, 126, 123, 118, 115, 111, 108, 105, 100, 95, 89, 82, 77, 74, 73, 70, 64, 58, 54, 51, 50, 50, 52, 55, 57, 59, 61, 63, 66, 69, 72, 75, 78, 82, 84, 87, 90, 92, 93, 93, 92, 90, 90, 86, 82, 78, 75, 73, 77, 81, 85, 90, 95, 102, 108, 114, 120, 125, 130, 135, 141, 145, 149, 152, 155, 158, 158, 157, 157, 156, 153, 152, 148, 146, 143, 141, 138, 136, 134, 133, 133, 132, 132, 132, 133, 133, 134, 135, 135, 137, 138, 139, 141, 142, 143, 143, 144, 144, 145, 146, 147, 147, 147,
# 147, 147, 148, 147, 148, 147, 147, 147, 146, 146, 146, 146, 146, 146, 146, 146, 144, 145, 146, 146, 144, 145, 145, 145, 146, 147, 148, 148, 150, 151, 151, 151, 151, 151, 152, 151, 151, 150, 150, 151, 150, 151, 151, 151, 150, 151, 152, 151, 152, 153, 153, 154, 155, 155, 155, 155, 156, 157, 157, 158, 159, 159, 159, 160, 161, 162, 163, 163, 163, 162, 163, 163, 163, 164, 164, 166, 165, 165, 164, 161, 160, 158, 157,
# 155, 155, 154, 153, 153, 155, 156, 157, 160, 162, 163, 166, 166, 168, 169, 170, 169, 169, 169], [85, 86, 86, 85, 86, 85, 86, 86, 86, 84, 82, 80, 77, 74, 72, 71, 71, 69, 67, 65, 66, 67, 68, 69, 68, 67, 67, 68, 67, 68, 70, 71, 76, 81, 86, 92, 99, 107, 113, 117, 121, 126, 130, 131, 132, 132, 130, 126, 123, 122, 121, 119, 117, 113, 107, 104, 100, 98, 93, 89, 84, 77, 71, 67, 63, 61, 5
# 6) rgbString: {#4f4f4f #515151 #535353 #555555 #565656 #565656 #575757 #565656 #555555 #555555 #555555 #525252 #505050 #4e4e4e #4c4c4c #4a4a4a #474747 #474747 #474747 #484848 #484848 #4c4c4c #535353 #595959 #636363 #696969 #6d6d6d #727272 #767676 #7a7a7a #7b7b7b #7e7e7e #808080 #828282 #858585 #888888 #898989 #8c8c8c #8f8f8f #929292 #969696 #9a9a9a #9e9e9e #a0a0a0 #a3a3a3 #a5a5a5 #a7a7a7 #a7a7a7 #a7a7a7 #a8a8a8
# #a9a9a9 #a9a9a9 #a8a8a8 #a5a5a5 #a3a3a3 #a1a1a1 #a0a0a0 #9f9f9f #9e9e9e #9b9b9b #989898 #959595 #929292 #909090 #8e8e8e #8d8d8d #8a8a8a #878787 #838383 #828282 #808080 #808080 #818181 #808080 #818181 #808080 #818181 #828282 #838383 #848484 #858585 #878787 #888888 #888888 #898989 #8a8a8a #8b8b8b #8b8b8b #8b8b8b #8a8a8a #8a8a8a #898989 #888888 #868686 #858585 #838383 #828282 #818181 #808080 #828282 #868686 #898989 #8b8b8b #8e8e8e #919191 #949494 #979797 #9b9b9b #9e9e9e #a1a1a1 #a3a3a3 #a5a5a5 #a7a7a7 #a7a7a7 #a9a9a9 #aaaaaa #ababab #acacac #ababab #ababab #aaaaaa #ababab #aaaaaa #a9a9a9 #a8a8a8 #a8a8a8 #a6a6a6 #a6a6a6 #a5a5a5 #a5a5a5 #a2a2a2 #a2a2a2 #a2a2a2
# #a1a1a1 #a1a1a1 #a1a1a1 #a1a1a1 #a1a1a1 #a0a0a0 #a0a0a0 #a0a0a0 #9e9e9e #9e9e9e #9d9d9d #9d9d9d #9c9c9c #9c9c9c #9d9d9d #9d9d9d #9c9c9c #9c9c9c #9d9d9d #9c9c9c #9c9c9c #9a9a9a #9b9b9b #9b9b9b #9b9b9b #9a9a9a #9a9a9a #9b9b9b #9c9c9c #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9a9a9a #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9a9a9a #9a9a9a #9a9a9a #9a9a9a #9a9a9a #999999 #9a9a9a #999999 #999999 #9a9a9a #999999 #999999 #9a9a9a #9a9a9a #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9c9c9c #9b9b9b #9b9b9b #9a9a9a #9b9b9b #9d9d9d #9c9c9c #9c9c9c #9d9d9d #9d9d9d #9f9f9f #9f9f9f #9f9f9f #a0a0a0 #a1a1a1 #a1a1a1 #a1a1a1 #a3a3a3 #a3a3a3 #a3a3a3 #a5a5a5 #a5a5a5 #a6a6a6 #a5a5a5 #a7a7a7
# #a7a7a7 #a7a7a7 #a8a8a8 #a9a9a9 #a9a9a9 #aaaaaa #aaaaaa #aaaaaa #ababab #aaaaaa #ababab #ababab #ababab #aaaaaa #acacac #ababab #ababab #acacac #ababab #ababab #aaaaaa #aaaaaa #a9a9a9 #a9a9a9 #a9a9a9 #aaaaaa #aaaaaa #aaaaaa #aaaaaa #aaaaaa #ababab #ababab #aaaaaa #aaaaaa #aaaaaa #ababab #ababab #aaaaaa #ababab #ababab } {#505050 #525252 #545454 #575757 #575757 #575757 #585858 #575757 #565656 #545454 #535353 #4f4f4f #4c4c4c #4b4b4b #484848 #474747 #464646 #454545 #464646 #474747 #484848 #484848 #4c4c4c #515151 #595959 #606060 #646464 #676767 #6c6c6c #6f6f6f #727272 #737373 #757575 #797979 #7c7c7c #7e7e7e #808080 #858585 #878787 #8c8c8c #909090 #949494 #989898 #9b9b9b #9d9d9d #9f9f9f #a1a1a1 #a1a1a1 #a1a1a1 #a2a2a2 #a3a3a3 #a2a2a2 #a1a1a1
# #9e9e9e #9c9c9c #9a9a9a #999999 #979797 #959595 #959595 #919191 #8e8e8e #8a8a8a #878787 #878787 #858585 #808080 #7c7c7c #797979 #767676 #747474 #747474 #747474 #757575 #767676 #767676 #777777 #767676 #787878 #797979 #7a7a7a #7c7c7c #7f7f7f #808080 #818181 #828282 #838383 #858585 #848484 #848484 #838383 #828282 #808080 #7f7f7f #7e7e7e #7b7b7b #797979 #787878 #797979 #7b7b7b #7e7e7e #818181 #848484 #888888 #8b8b8b #8e8e8e #929292 #969696 #999999 #9c9c9c #9f9f9f #a2a2a2 #a3a3a3 #a6a6a6 #a7a7a7 #a8a8a8 #aaaaaa #aaaaaa #ababab #ababab #a9a9a9 #a9a9a9 #a8a8a8 #a6a6a6 #a6a6a6 #a4a4a4 #a3a3a3 #a2a2a2 #a2a2a2 #a1a1a1 #9f9f9f #9e9e9e #9d9d9d #9d9d9d #9d9d9d #9d9d9d
# #9e9e9e #9e9e9e #9e9e9e #9d9d9d #9d9d9d #9c9c9c #9b9b9b #9b9b9b #9b9b9b #9a9a9a #9b9b9b #9c9c9c #9b9b9b #9c9c9c #9c9c9c #9c9c9c #9b9b9b #9b9b9b #9a9a9a #9a9a9a #9b9b9b #9b9b9b #9a9a9a #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9c9c9c #9b9b9b #9c9c9c #9b9b9b #9b9b9b #9a9a9a #9a9a9a #9a9a9a #9a9a9a #9a9a9a #9a9a9a #999999 #999999 #9a9a9a #989898 #999999 #999999 #999999 #999999 #999999 #999999 #999999 #9a9a9a #9a9a9a #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9a9a9a #9a9a9a #9a9a9a #9c9c9c #9c9c9c #9c9c9c #9d9d9d #9d9d9d #9e9e9e #9e9e9e #a0a0a0 #9f9f9f #a0a0a0 #a0a0a0 #a1a1a1 #a2a2a2 #a3a3a3 #a4a4a4 #a4a4a4 #a4a4a4 #a5a5a5 #a5a5a5 #a5a5a5 #a5a5a5 #a7a7a7 #a7a7a7
# #a8a8a8 #a8a8a8 #a8a8a8 #a9a9a9 #a9a9a9 #a9a9a9 #a9a9a9 #aaaaaa #aaaaaa #ababab #aaaaaa #ababab #ababab #acacac #ababab #ababab #aaaaaa #a9a9a9 #a8a8a8 #a8a8a8 #a8a8a8 #a8a8a8 #a8a8a8 #a8a8a8 #a8a8a8 #a9a9a9 #aaaaaa #aaaaaa #aaaaaa #ababab #ababab #ababab #ababab #acacac #aaaaaa #aaaaaa #aaaaaa } {#505050 #525252 #545454 #565656 #575757 #585858 #585858 #565656 #565656 #545454 #525252 #4f4f4f #4d4d4d #4a4a4a #484848 #474747 #464646 #454545 #444444 #454545 #454545 #454545 #474747 #4b4b4b #515151 #575757 #5c5c5c #5f5f5f #636363 #656565 #676767 #676767 #6a6a6a #6d6d6d #717171 #757575 #777777 #7c7c7c #818181 #888888 #8b8b8b #8f8f8f #929292 #969696 #989898 #9a9a9a #9a9a9a #9a9a9a #9b9b9b #9b9b9b #9d9d9d #9c9c9c #9a9a9a #979797 #969696 #939393
# #929292 #919191 #8f8f8f #8d8d8d #8a8a8a #858585 #828282 #7e7e7e #7c7c7c #7b7b7b #777777 #727272 #6d6d6d #696969 #676767 #666666 #666666 #676767 #696969 #6b6b6b #6b6b6b #6b6b6b #6c6c6c #6f6f6f #727272 #737373 #757575 #777777 #787878 #787878 #7a7a7a #7c7c7c #7d7d7d #7d7d7d #7b7b7b #7a7a7a #787878 #767676 #747474 #727272 #707070 #6f6f6f #707070 #737373 #767676 #797979 #7d7d7d #808080 #858585 #888888 #8b8b8b #8f8f8f #939393 #989898 #999999 #9d9d9d #9f9f9f #a3a3a3 #a5a5a5 #a6a6a6 #a8a8a8 #a9a9a9 #a9a9a9 #a8a8a8 #a8a8a8 #a7a7a7 #a5a5a5 #a3a3a3 #a2a2a2 #9f9f9f #9e9e9e #9d9d9d #9d9d9d #9a9a9a #9a9a9a #9a9a9a #999999 #999999 #999999 #999999 #999999 #999999 #9a9a9a
# #999999 #9a9a9a #989898 #999999 #999999 #999999 #999999 #999999 #9a9a9a #9a9a9a #9b9b9b #9b9b9b #9a9a9a #9a9a9a #9a9a9a #999999 #9a9a9a #9b9b9b #9a9a9a #9a9a9a #9a9a9a #9a9a9a #9a9a9a #9b9b9b #9a9a9a #9a9a9a #9b9b9b #9a9a9a #9a9a9a #9a9a9a #9a9a9a #9a9a9a #999999 #9a9a9a #999999 #9a9a9a #999999 #999999 #999999 #999999 #999999 #999999 #999999 #9a9a9a #9a9a9a #999999 #989898 #999999 #9a9a9a #999999 #999999 #989898 #989898 #9a9a9a #9a9a9a #9a9a9a #9a9a9a #999999 #9b9b9b #9b9b9b #9b9b9b #9b9b9b #9c9c9c #9d9d9d #9e9e9e #9e9e9e #9f9f9f #9f9f9f #a0a0a0 #a0a0a0 #a1a1a1 #a2a2a2 #a3a3a3 #a3a3a3 #a3a3a3 #a5a5a5 #a5a5a5 #a6a6a6 #a6a6a6 #a7a7a7 #a7a7a7 #a8a8a8 #a8a8a8
# #a8a8a8 #a9a9a9 #a9a9a9 #a9a9a9 #aaaaaa #aaaaaa #aaaaaa #a9a9a9 #ababab #ababab #aaaaaa #ababab #a9a9a9 #a8a8a8 #a7a7a7 #a7a7a7 #a6a6a6 #a5a5a5 #a5a5a5 #a5a5a5 #a6a6a6 #a7a7a7 #a8a8a8 #a7a7a7 #a9a9a9 #aaaaaa #ababab #aaaaaa #aaaaaa #aaaaaa #aaaaaa #ababab #aaaaaa #ababab } {#525252 #545454 #565656 #575757 #585858 #585858 #585858 #575757 #575757 #545454 #525252 #4f4f4f #4d4d4d #4b4b4b #494949 #484848 #454545 #464646 #444444 #444444 #444444 #444444 #454545 #484848 #4a4a4a #4f4f4f #555555 #565656 #595959 #5c5c5c #5b5b5b #5d5d5d #5f5f5f #626262 #666666 #6a6a6a #707070 #767676 #7d7d7d #848484 #888888 #8a8a8a #8e8e8e #919191 #939393 #959595 #959595 #959595 #949494 #959595 #969696 #969696 #949494 #919191 #8f8f8f #8c8c8c #8b8b8b #898989 #878787
# #848484 #818181 #7b7b7b #777777 #737373 #707070 #6e6e6e #6c6c6c #676767 #606060 #5b5b5b #595959 #595959 #585858 #5b5b5b #5d5d5d #5f5f5f #5f5f5f #5e5e5e #5f5f5f #636363 #666666 #686868 #696969 #6c6c6c #6e6e6e #707070 #717171 #747474 #757575 #757575 #747474 #747474 #727272 #6f6f6f #6d6d6d #6b6b6b #676767 #656565 #666666 #686868 #6d6d6d #717171 #747474 #797979 #7e7e7e #828282 #868686 #8a8a8a #8e8e8e #929292 #959595 #999999 #9d9d9d #a0a0a0 #a3a3a3 #a5a5a5 #a7a7a7 #a8a8a8 #a8a8a8 #a7a7a7 #a6a6a6 #a4a4a4 #a2a2a2 #9f9f9f #9e9e9e #9c9c9c #9a9a9a #999999 #989898 #969696 #959595 #959595 #949494 #949494 #949494 #959595 #959595 #959595 #969696 #959595 #959595 #969696
# #959595 #969696 #969696 #969696 #969696 #969696 #989898 #999999 #999999 #999999 #989898 #999999 #989898 #9a9a9a #9a9a9a #999999 #999999 #999999 #999999 #999999 #9a9a9a #999999 #999999 #999999 #989898 #999999 #989898 #989898 #999999 #989898 #989898 #979797 #979797 #989898 #979797 #989898 #989898 #989898 #979797 #989898 #989898 #989898 #989898 #989898 #989898 #999999 #999999 #989898 #989898 #989898 #989898 #989898 #999999 #999999 #989898 #989898 #999999 #999999 #9a9a9a #9a9a9a #9b9b9b #9c9c9c #9c9c9c #9d9d9d #9e9e9e #9e9e9e #9e9e9e #9f9f9f #9f9f9f #a1a1a1 #a2a2a2 #a2a2a2 #a3a3a3 #a3a3a3 #a4a4a4 #a4a4a4 #a5a5a5 #a5a5a5 #a6a6a6 #a7a7a7 #a7a7a7 #a7a7a7 #a8a8a8 #a8a8a8 #a8a8a8 #a8a8a8 #aaaaaa #a8a8a8 #a9a9a9 #aaaaaa #aaaaaa #a9a9a9 #a8a8a8 #a7a7a7 #a5a5a5 #a4a4a4 #a3a3a3 #a2a2a2 #a2a2a2 #a3a3a3 #a4a4a4 #a5a5a5 #a6a6a6 #a8a8a8 #a8a8a8 #a9a9a9 #aaaaaa #aaaaaa #ababab #aaaaaa #aaaaaa #ababab #aaa