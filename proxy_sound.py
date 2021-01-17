"""
2021/01/11
"""
"""
卒論用
代行実験用プログラム_エージェント=ロボットver
"""
"""
メモ
proxy_base.pyがおおもと
"""

# coding: utf-8
import PySimpleGUI as sg
import robot
import reviews
import select_poses_lines
import posedef
import time
import sys

import jtalk
from playsound import playsound
import subprocess
import os.path
from pydub import AudioSegment

INIT_LOCATION = (0,0)

def sound_say(text, speed=1.0, emotion="normal"):
    output_file = "sound_output.wav"
    jtalk.make_wav(text, speed, emotion, output_file)
    playsound(output_file)
    sound = AudioSegment.from_file(output_file, 'wav')
    return sound.duration_seconds


def explain_sound(text = "こんにちは",emo="happy"):
    t = sound_say(text, emotion = emo)
    print(t)
    # time.sleep(t)

def main():
    
    # w0_導入
    print("window0")
    L0=[
        [sg.Text("実験が始まります。\n下のボタンを押してください。")],
        [sg.Button("start",key="b0")]
    ]
    # W0 = sg.Window("導入",L0)
    W0 = sg.Window("導入",L0,location=INIT_LOCATION)
    # event0, values0 = W0.read()
    
    while True:
        event0, values0 = W0.read()
        print('event0:',event0,', values0:',values0)
        if event0 == None:
            print("×がクリックされました。")
            sys.exit()
        elif event0 == "b0":
            print("「start」がクリックされました。")
            for i in range(len(select_poses_lines.W0)):
                explain_sound(select_poses_lines.W0[i]["lines"],"happy")
            break
    W0.close()

    # w1_商品1
    print("window1")
    L1=[
        [
            sg.Text(reviews.review1,font=(None,15)),\
            sg.Image(filename="./images/resize/cleaner_ex.png",background_color='#ffffff')\
        ],
        [sg.Button("商品の説明を聞く",key="b1")]
    ]
    # W1 = sg.Window("商品1",L1)
    W1 = sg.Window("商品1",L1,location=INIT_LOCATION)

    while True:
        event1, values1 = W1.read()
        print('event1:',event1,', values1:',values1)
        if event1 == None:
            print("×がクリックされました。")
            sys.exit()
        elif event1 == "b1":
            print("「商品の説明を聞く」がクリックされました。")
            for i in range(len(select_poses_lines.W0)):
                explain_sound(select_poses_lines.W1[i]["lines"],"happy")
            break
    W1.close()

    # w2_商品2
    print("window2")
    L2=[
        [
            sg.Text(reviews.review2,font=(None,15)),\
            sg.Image(filename="./images/resize/cleaner_2.png",background_color='#ffffff')\
        ],
        [sg.Button("商品の説明を聞く",key="b2")]
    ]
    # W2 = sg.Window("商品2",L2)
    W2 = sg.Window("商品2",L2,location=INIT_LOCATION)

    while True:
        event2, values2 = W2.read()
        print('event2:',event2,', values2:',values2)
        if event2 == None:
            print("×がクリックされました。")
            sys.exit()
        elif event2 == "b2":
            print("「商品の説明を聞く」がクリックされました。")
            for i in range(len(select_poses_lines.W0)):
                explain_sound(select_poses_lines.W2[i]["lines"],"happy")
            break
    W2.close()

    # w3_商品3
    print("window3")
    L3=[
        [
            sg.Text(reviews.review3,font=(None,15)),\
            sg.Image(filename="./images/resize/cleaner_3.png",background_color='#ffffff')\
        ],
        [sg.Button("商品の説明を聞く",key="b3")]
    ]
    # W3 = sg.Window("商品3",L3)
    W3 = sg.Window("商品3",L3,location=INIT_LOCATION)

    while True:
        event3, values3 = W3.read()
        print('event3:',event3,', values3:',values3)
        if event3 == None:
            print("×がクリックされました。")
            sys.exit()
        elif event3 == "b3":
            print("「商品の説明を聞く」がクリックされました。")
            for i in range(len(select_poses_lines.W0)):
                explain_sound(select_poses_lines.W3[i]["lines"],"happy")
            break
    W3.close()

    # w4_終わり
    print("window4")
    L4=[
        [sg.Text("これで実験は終わりです。\nありがとうございました。")],
        [sg.Text("アンケートへの回答をお願いします。")],
        [sg.Button("finish",key="b4")]
    ]
    # W4 = sg.Window("終わり",L4)
    W4 = sg.Window("終わり",L4,location=INIT_LOCATION)

    while True:
        event4, values4 = W4.read()
        print('event4:',event4,', values4:',values4)
        if event4 == None:
            print("×がクリックされました。")
            sys.exit()
        elif event4 == "b4":
            print("finishが押されました。")
            for i in range(len(select_poses_lines.W0)):
                explain_sound(select_poses_lines.W4[i]["lines"],"happy")
            break
    W4.close()

if __name__ == "__main__":
     main()   

