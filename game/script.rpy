
default bg_left = False
define config.voice_filename_format = "{filename}"
transform tcommon(x=640, z=1):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.05
        zoom z*0.95 alpha 0.00
        xcenter x yoffset -20
        easein .25 yoffset 0 zoom z*1.00 alpha 1.00
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter x zoom z*1.00
        parallel:
            easein .15 yoffset 0 ypos 1.05

transform n_cg2_wiggle:
    subpixel True
    xoffset 0
    easein 0.15 xoffset 20
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -15
    easeout 0.15 xoffset 0
    easein 0.15 xoffset 10
    easeout 0.15 xoffset 0
    easein 0.15 xoffset -5
    ease 0.15 xoffset 0


transform t21: 
    tcommon(400)
transform t22:
    tcommon(880)
transform t11:
    tcommon(960)

define dissolve_scene_full = MultipleTransition([
    False, Dissolve(1.0),
    Solid("#000"), Pause(1.0),
    Solid("#000"), Dissolve(1.0),
    True])

init python:
    _preferences.afm_enable = True
    _preferences.afm_time = 15
    config.keymap['toggle_afm'].append('alt_K_F3')

label left:
    $ gui.direction = 0.25
    $ gui.xdirection = 0.0
    $ gui.rebuild()
    return

label right:
    $ gui.direction = 0.75
    $ gui.xdirection = 1.0
    $ gui.rebuild()
    return

init python:
    import subprocess
    import random
    dic = {}
    a_dic = {}
    a_dic["ch01_1plyr"]=["positive","negative","nonsense"]
    a_dic["ch01_2plyr"]=["normal","joy","sad","anger"]
    a_dic["ch02_1plyr"]=["positive","negative","nonsense"]
    a_dic["ch02_2plyr"]=["positive","negative","ask"]
    a_dic["ch02_3plyr_a"]=["positive","negative"]
    a_dic["ch02_3plyr_b"]=["positive","negative"]
    a_dic["ch03_1plyr"]=["positive","negative"]
    a_dic["ch03_2plyr"]=["positive","negative"]
    a_dic["ch03_3plyr"]=["answer"]
    a_dic["ch03_4plyr"]=["normal","sad","anger"]
    a_dic["ch03_5plyr"]=["why","lie","sad","anger"]#
    a_dic["ch05_1plyr"]=["positive_normal","negative_normal","anger_sad"]#
    a_dic["ch05_2plyr"]=["positive","negative"]
    a_dic["ch05_3plyr"]=["anger","believe","explain"]#
    a_dic["ch05_3plyr_a"]=["apologize","anger"]
    a_dic["ch05_3plyr_a_a"]=["apologize","anger"]
    a_dic["ch05_3plyr_b"]=["believe","notbelieve"]
    a_dic["ch05_3plyr_b_a"]=["worry","positive"]#
    a_dic["ch05_3plyr_c"]=["agree","disagree"]
    a_dic["ch05_3plyr_c_a"]=["believe","notbelieve"]
    a_dic["ch05_3plyr_d"]=["believe","notbelieve"]
    a_dic["ch06_1plyr"]=["seoeun","hyoju"]
    a_dic["ch07_1plyr"]=["positive","negative","ask"]
    a_dic["ch07_2plyr"]=["answer"]
    a_dic["ch07_2_1plyr"]=["positive","negative","nonsense"]
    a_dic["ch07_2_2plyr"]=["normal","joy","sad","anger"]
    ps_list = ["ch01_1plyr","ch02_1plyr","ch02_2plyr","ch02_3plyr_a","ch02_3plyr_b","ch03_1plyr","ch03_2plyr","ch05_2plyr","ch05_3plyr_b","ch05_3plyr_c","ch05_3plyr_c_a","ch05_3plyr_d","ch07_1plyr","ch07_2_1plyr"]
    pass_list = ["ch03_3plyr","ch07_2plyr"]
    emo_list =["ch01_2plyr","ch03_4plyr","ch07_2_2plyr"]
    apl_list =["ch05_3plyr_a","ch05_3plyr_a_a"]
    process_list = []
    _process = ["xmlpipe.exe"]
    process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
    if not list(set(process_list).intersection(_process)):
        subprocess.call("C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\do_justrun.cmd",shell=True)


label qus(q):
    python:
        num = 0
        import os
        import io
        _chk_init = False
        subprocess.call("del C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.txt C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\check.init",shell=True)
        subprocess.Popen(['C:\\Users\\boa65\\Anaconda3\\python.exe', 'C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\_test.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
        comm = "C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\result.txt"
        chk_init = "C:\\Users\\boa65\\Downloads\\2dTest_Student\\re-late\\game\\check.init"
        while(1):
            if _chk_init or os.path.isfile(chk_init):
                _chk_init = True
                if os.path.isfile(comm):
                    break
            num += 1
            if not _chk_init:
                say(None,".....")
            else:
                say(None,"."*(num%3+1))
        
        f = io.open(comm, mode="r", encoding="utf-8")
        a,b,c = f.read().splitlines()
        f.close()
        if q in ps_list:
            if c == 'pos':
                dic[q] = "positive"
                say(None,a)
            else:
                dic[q] = "negative"
                say(None,a)
        if q in emo_list:
            if b == "boredom":
                dic[q] = "normal"
            elif b == "sadness":
                dic[q] = "sad"
            elif b == "anger" or b == "disgust":
                dic[q] = "anger"
            else:
                if "joy" in a_dic[q]:
                    dic[q] = "joy"
                else:
                    dic[q] = "normal"
            say(None,a)
        if q in pass_list:
            dic[q] = "answer"
            say(None,a)
        if q == "ch06_1plyr":
            if "서은" in a:
                dic[q] = "seoeun"
                say(None,a)
            elif "효주" in a:
                dic[q] = "hyoju"
                say(None,a)
            else: 
                say(None,'서은이와 효주 중 한 명은 선택해야겠어')
                qus(q)
        if q == "ch03_5plyr":
            if "왜" in a:
                dic[q] = "why"
            elif "거짓말" in a:
                dic[q] = "lie"
            elif b == "surprise" or b == "anger" or b == "disgust":
                dic[q] = "anger"
            else:
                dic[q] = "sad"
            say(None,a)
        if q == "main":
            dic[q] = "true"
        print dic[q]
    return

define s = Character(u'서은', image='', what_prefix='"', what_suffix='"', say_who_window_background="gui/yellow_nt.png", voice_tag="seoeun")
define h = Character(u'효주', image='', what_prefix='"', what_suffix='"', say_who_window_background="gui/pink_nt.png", voice_tag="hyoju")
define d = Character(u'???', image='', what_prefix='"', what_suffix='"', say_who_window_background="gui/mint_nt.png")

image se 1 = im.Composite((1920, 1211), (0, 0), "images/se_normal.png")
image se 2 = im.Composite((1920, 1211), (0, 0), "images/se_sad.png")
image se 3 = im.Composite((1920, 1211), (0, 0), "images/se_smile.png")
image se 4 = im.Composite((1920, 1211), (0, 0), "images/se_surprise.png")
image se 5 = im.Composite((1920, 1211), (0, 0), "images/se_anger.png")

image hj 1 = im.Composite((1920, 1211), (0, 0), "images/hj_normal.png")
image hj 2 = im.Composite((1920, 1211), (0, 0), "images/hj_sad.png")
image hj 3 = im.Composite((1920, 1211), (0, 0), "images/hj_smile.png")
image hj 4 = im.Composite((1920, 1211), (0, 0), "images/hj_surprise.png")
image hj 5 = im.Composite((1920, 1211), (0, 0), "images/hj_anger.png")

image cr1_day = "cr1_day.jpg"
image cr1_night = "cr1_night.jpg"
image cr2_day = "cr2_day.jpg"
image cr2_night = "cr2_night.jpg"
image hall_day = "hall_day.jpg"
image hall_night = "hall_night.jpg"
image present_day = "back.png"

image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat
    
$ style.say_dialogue = style.normal

label splashscreen:
    $ renpy.movie_start_displayable("intro_final.webm")
    scene black
    with dissolve_scene_full
    call menuv
    return

label start:

    call ch01_main from _call_ch01_main
    call ch02_main from _call_ch02_main
    call ch03_main from _call_ch03_main
    if dic["ch03_2plyr"] == "negative" or not dic["03_5plyr"] == "lie":
        call ch04_2_main from _call_ch04_2_main
    else:
        call ch04_1_main from _call_ch04_1_main
    call ch05_main from _call_ch05_main
    call ch06_main from _call_ch06_main
    call ch07_main from _call_ch07_main

    return

label nd2_start:

    call ch10_main from _call_ch10_main
    call ch01_main from _call_ch01_main_1
    call ch02_main from _call_ch02_main_1
    call ch03_main from _call_ch03_main_1
    call ch05_main from _call_ch05_main_1
    call ch06_main from _call_ch06_main_1
    call ch07_main from _call_ch07_main_1
    return
