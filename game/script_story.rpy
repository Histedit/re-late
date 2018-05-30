image test_movie = Movie(play="a.webm")

label menuv:
    image main_menuv = Movie(play="a.webm")
    scene black
    call play_movie(10)

    call ch01_main

    return

label play_movie (duration):
    show test_movie
    $ renpy.pause(duration, hard=True)
    hide test_movie

    return

label tutorial:
    
    return

label ch01_main:
    $ renpy.pause(1.0)
    scene black
    play music "jb.mp3"
    "2008년, 봄. XX고등학교."
    voice "se01.ogg"
    s "…야."
    "어디선가 목소리가 들린다."
    voice "se01.ogg"
    s "야."
    "목소리가 꽤 또렷하게 들리지만 고개는 여전히 무겁다. 아직 일어나기 싫다."
    voice "se02.ogg"
    s "일어나. 점심시간이야."
    scene cr1_day
    with dissolve_scene_full
    show se 3 at t11
    "몽롱한 정신으로 고개를 들어 보니 어느 여자아이가 서 있다."
    show se 1 at t11
    voice "se03.ogg"
    s "점심시간이라니까? 수업 중에 잠이나 자고. 아무튼 점심 먹으러 안 가?" #normal
    $ pre_ask = "점심시간이라니까? 수업 중에 잠이나 자고. 아무튼 점심 먹으러 안 가?"
    call qus("ch01_1plyr") from _call_qus

    if dic["ch01_1plyr"] == "positive":
        show se 3 at t11     
        voice "se04.ogg"
        s "그럼 빨리 일어나. 너 때문에 밥 먹을 시간이 줄고 있잖아." #smile
        $ pre_ask = "그럼 빨리 일어나. 너 때문에 밥 먹을 시간이 줄고 있잖아."
    elif dic["ch01_1plyr"] == "negative":
        show se 5 at t11
        voice "se05.ogg"
        s "지금 가야 맛난 거 많이 먹을 수 있단 말이야. 빨리 나와." #smile
    elif dic["ch01_1plyr"] == "nonsense":
        show se 5 at t11
        voice "se06.ogg"
        s "갑자기 무슨 헛소리야? 빨리 나오기나 해. 나 배고프다니까." #smile

    call qus("ch01_2plyr") from _call_qus_1

    if dic["ch01_2plyr"] == "normal":
        hide se
        "이럴거면 왜 물어본건지... 결국 잠이 덜 깬 몸을 일으켜 급식실로 향한다."
    elif dic["ch01_2plyr"] == "joy":
        show se 1 at t11
        voice "se07.ogg"
        s "......너 이상해." #normal
        hide se
        "결국 잠이 덜 깬 몸을 일으켜 급식실로 향한다."
    elif dic["ch01_2plyr"] == "sad":
        show se 3 at t11
        voice "se08.ogg"
        s "안돼. 빨리 나와, 빨리!!!" #smile
        hide se
        "결국 잠이 덜 깬 몸을 일으켜 급식실로 향한다."
    elif dic["ch01_2plyr"] == "anger":
        show se 5 at t11
        voice "se09.ogg"
        s "새삼스럽게 왜 화내. 익숙해질 때도 됐잖아. 어서 가자." #anger
        hide se
        "결국 잠이 덜 깬 몸을 일으켜 급식실로 향한다."
    return



label ch02_main:
    scene hall_day
    with dissolve_scene_full
    show se 1 at t11
    "이 아이의 이름은 서은. 당찬 성격인 아이라서 매번 나를 이런 식으로 질질 끌고 간다."
    "가끔 피곤하기는 하지만 밉지는 않은, 3년째 붙어 다니는 나의 친구다."
    show se 1 at t11
    voice "se10.ogg"
    s "그나저나 날씨, 완전 따뜻해지지 않았어?" #normal

    call qus("ch02_1plyr") from _call_qus_2

    if dic["ch02_1plyr"] == "positive":
        show se 3 at t11
        voice "se11.ogg"
        s "그렇다니까. 벌써 부산 쪽은 벚꽃 다 펴서 이미 진다더라." #smile
    elif dic["ch02_1plyr"] == "negative":
        show se 4 at t11
        voice "se12.ogg"
        s "이게? 원래 추위 많이 탔었나. 아무튼 약한 척은." #surprise
    elif dic["ch02_1plyr"] == "nonsense":
        show se 5 at t11
        voice "se13.ogg"
        s "뭐라는 거야. 날씨가 따뜻해지지 않았냐고 물었잖아." #anger

    show se 2 at t11
    voice "se15.ogg"
    s "꽃구경 간 지가 언젠지 모르겠어. 올해는 수능도 봐서 가기가 더 눈치 보인다니까." #sad
    show se 3 at t11
    voice "se16.ogg"
    s "그런데 약간 올해라서 더 가고 싶은 것 같아. 일탈 같은 느낌이잖아." #smile

    call qus("ch02_2plyr") from _call_qus_3

    if dic["ch02_2plyr"] == "positive":
        show se 1 at t11
        voice "se17.ogg"
        s "앗, 그러면 나랑 같이 꽃구경 갈래? 나 혼자서 가면 죄책감 들 것 같단 말이야." #normal
    elif dic["ch02_2plyr"] == "negative":
        show se 1 at t11
        voice "se18.ogg"
        s "모범생인 척 좀 하지 마. 그런 김에 나랑 벚꽃 보러 가자. 나 혼자 가면 심심해." #normal
    elif dic["ch02_2plyr"] == "ask":
        show se 4 at t11
        voice "se19.ogg"
        s "엥 너랑? 어..." #surprise

    call qus("ch02_3plyr_a") from _call_qus_4

    if dic["ch02_3plyr_a"] == "positive":
        show se 1 at t11
        voice "se20.ogg"
        s "으음, 근데 나 오늘밖에 시간이 없는데 괜찮아? 오늘 학교 끝나고 바로!" #normal
        
        call qus("ch02_3plyr_b") from _call_qus_5

        if dic["ch02_3plyr_b"] == "positive":
            show se 3 at t11
            voice "se21.ogg"
            s "그럼 수업 다 끝나고 보자!" #smile
            hide se
            "꽃구경 가는 것이 그렇게 기쁠 일인가. 방방 뛰면서 올라가는 서은이의 모습에 괜시리 웃음이 난다."
            "나도 슬슬 일어나서 다시 교실로 돌아가도록 하자."

            return
        elif dic["ch02_3plyr_b"] == "negative":
            show se 2 at t11
            
            voice "se22.ogg"
            s "으으.. 나중은 벚꽃 다 질 텐데..." #sad
            show se 3 at t11
            voice "se23.ogg"
            s "그럼 내년에 가지 뭐. 수능도 다 끝나고 대학생일테니까, 시간도 많...지 않으려나." #smile
    
            voice "se24.ogg"
            s "아무튼! 나는 먼저 교실 들어가볼게." #smile
            hide se
            "이상하다. 평소와 같은 모습인데 미묘하게 서은이의 표정이 슬퍼보였다."
            "하지만 곧 수업 시간이다. 생각을 그만두고 교실로 돌아가야 한다."
            "괜찮을 거야. 항상 바보처럼 밝은 애니까. 그런 애니까."


    elif dic["ch02_3plyr_a"] == "negative":
        show se 2 at t11
        voice "se22.ogg"
        s "으으.. 나중은 벚꽃 다 질 텐데..." #sad
        show se 3 at t11
        voice "se23.ogg"
        s "그럼 내년에 가지 뭐. 수능도 다 끝나고 대학생일테니까, 시간도 많...지 않으려나." #smile
        voice "se24.ogg"
        s "아무튼! 나는 먼저 교실 들어가볼게." #smile
        hide se
        "이상하다. 평소 같은 모습인데 미묘하게 서은이의 표정이 슬퍼보였다."
        "하지만 곧 수업 시간이다. 생각을 그만두고 교실로 돌아가야 한다."
        "괜찮을 거야. 항상 바보처럼 밝은 애니까. 그런 애니까."
    



    
label ch03_main:
    scene hall_day
    with dissolve_scene_full
    show hj 1 at t11
    voice "hj/hj01.ogg"
    h "나랑 얘기 좀 해." #normal
    "누군가가 갑자기 나를 불러 세운다. 옆 반의 효주였다. 나랑 친하지도 않은 애가, 갑자기?"
    voice "hj/hj02.ogg"
    h "할 얘기가 있어. 들어줄 수 있어?" #normal

    call qus("ch03_1plyr") from _call_qus_6

    if dic["ch03_1plyr"] == "positive":
        show hj 2 at t11
        voice "hj/hj03.ogg"
        h "서은이에 대한 건데..." #sad
    elif dic["ch03_1plyr"] == "negative":
        show hj 2 at t11
        voice "hj/hj04.ogg"
        h "서은이에 관한 이야기야. 들어줬으면 좋겠어." #sad


    "참, 볼수록 서은이와 정반대되는 성격이다. 무뚝뚝하고, 조용한 말투. 얘기를 들을까?"

    call qus("ch03_2plyr") from _call_qus_7

    if dic["ch03_2plyr"] == "positive":
        show hj 1 at t11
        voice "hj/hj05.ogg"
        h "서은이에게 이야기하지 않을 거지?" #normal

        call qus("ch03_3plyr") from _call_qus_8

        if dic["ch03_3plyr"] == "answer":
            show hj 1 at t11
            voice "hj/hj06.ogg"
            h "그래, 그건 네가 선택할 일이니까." #normal
            show hj 2 at t11
            voice "hj/hj07.ogg"
            h "아무튼, 서은이가 너에 대해서 좋지 않은 소문을 퍼뜨리고 다녀." #sad
    
        call qus("ch03_4plyr") from _call_qus_9

        if dic["ch03_4plyr"] == "normal":
            show hj 2 at t11
            voice "hj/hj08.ogg"
            h "그게..." #sad
        elif dic["ch03_4plyr"] == "sad":
            show hj 2 at t11
            voice "hj/hj09.ogg"
            h "울지는 마. 뭐라고 했었냐면," #sad
        elif dic["ch03_4plyr"] == "anger":
            show hj 4 at t11
            voice "hj/hj10.ogg"
            h "목소리 좀 낮춰줘. 애들이 다 듣겠다. 아무튼," #anger
    

        show hj 1 at t11
        "네가 이 사람 저 사람 찔러보고 다닌다고도 했고, 사람을 계획적으로 이용한다고 했어." #normal
        "나도 지나가다가 들은 거라 정확하진 않은데, 네가 알아야 할 것 같아 말하는 거야." #normal

        call qus("ch03_5plyr") from _call_qus_10

        if dic["ch03_5plyr"] == "why":
            show hj 1 at t11
            voice "hj/hj11.ogg"
            h "그냥, 서은이가 어떤 아이인지 알길 바랐어. 너네 3년 내내 붙어다녔잖아." #normal
        elif dic["ch03_5plyr"] == "lie":
            show hj 1 at t11
            voice "hj/hj12.ogg"
            h "믿든 말든 그건 네 자유긴 해. 하지만 적어도 3학년 내에서는 소문이 쫙 돌았어. 잘 판단하길 바랄게." #normal
        elif dic["ch03_5plyr"] == "sad":
            show hj 2 at t11
            voice "hj/hj13.ogg"
            h "어... 충격 받은 건 알겠지만 정신 똑바로 차리길 바라. 지금도 소문은 돌고 있어." #sad
        elif dic["ch03_5plyr"] == "anger":
            show hj 4 at t11
            
            voice "hj/hj14.ogg"
            h "제발, 나한테 화내지 말아줘. 나도 그저 들었을 뿐이라구." #surprise
            
            
    elif dic["ch03_2plyr"] == "negative":
        show hj 1 at t11
        
        voice "hj/hj15.ogg"
        h "완고하네. 알겠어. 다만, 어떤 소문이 돌아도 듣지마." #normal


    show hj 3 at t11 
    voice "hj/hj16.ogg"
    h "아무튼, 좀 더 자세히 듣고 싶다면 학교 끝나고 나를 찾아오기를 바라." #smile
    hide hj
    "대답도 듣지 않은 채 효주는 자기 교실로 급하게 들어가버렸다. 나도 일단 교실로 돌아가야겠다."
    
    return


label ch04_1_main:
    scene cr2_day
    with dissolve_scene_full
    "수업 내용이 전혀 귀에 들어오지 않았다."
    "사실일까? 서은이가 정말로 그랬을까? 아냐, 그럴 리가 없어."
    "사실이라면, 왜 그랬을까? 3년 동안 대체 나는 서은이와 무슨 사이였던 걸까?"
    "친구? 애초에 친구였던 걸까?"
    "아니다. 섣부른 판단은 금물이다. 당사자와 이야기를 나눠 봐야 한다."
    "하지만 진실이 두렵다. 나는 어떻게 해야 할까."
    return



label ch04_2_main:
    scene cr2_day
    with dissolve_scene_full
    "항상 느끼는 거지만"
    "수업 시간은 너무..."
    "졸려."
    "그나저나 효주가 하려던 이야기는 뭐였을까?"
    "시답잖은 이야기였겠지. 잠이나 자자."
    return



label ch05_main:
    scene cr1_day
    with dissolve_scene_full
    show se 2 at t11
    voice "se25.ogg"
    s "...야." 
    "서은이다. 표정이 많이 어두워 보인다."
    show se 1 at t11
    
    voice "se26.ogg"
    s "나한테 물어볼 거 없어?" #normal

    call qus("ch05_1plyr") from _call_qus_11

    if dic["ch05_1plyr"] == "positive_normal":
        show se 2 at t11
        voice "se27.ogg"
        s "그 소문에 관한 거지?" #sad
    elif dic["ch05_1plyr"] == "negative_normal":
        show se 2 at t11
        voice "se28.ogg"
        s "들었을 거 아냐. 내가 너에 관한 이상한 소문들을 퍼뜨리고 다닌다는 말." #sad
    elif dic["ch05_1plyr"] == "anger_sad":
        show se 2 at t11
        voice "se29.ogg"
        s "너, 그 소문들 믿는구나? 그래서 화가 난 거지?" #sad
    
    call qus("ch05_2plyr") from _call_qus_12

    if dic["ch05_2plyr"] == "positive":
        show se 5 at t11
        voice "se30.ogg"
        s "내가 정말 그랬을 거라고 생각하는 거야? 그런 바보 같은 소문을 믿는 너도 멍청이다." #anger
    elif dic["ch05_2plyr"] == "negative":
        show se 5 at t11
        voice "se31.ogg"
        s "거짓말. 결국 너도 날 못 믿네. 못 믿으니까 그런 반응인 것 아냐?" #anger
        voice "se32.ogg"
        s "3년 동안이나 같이 지내왔으면서 어떻게 나에 대해 그렇게 한 치도 모를 수 있어?" #anger
    
    call qus("ch05_3plyr") from _call_qus_13

    if dic["ch05_3plyr"] == "anger":
        show se 5 at t11
        voice "se33.ogg"
        s "이것 봐. 무턱대고 화부터 내잖아. 내 친구면 내 얘기를 먼저 들어줘야 하는 거 아냐?" #anger
        show se 2 at t11
        voice "se34.ogg"
        s "진짜 실망이야." #sad

        call qus("ch05_3plyr_a") from _call_qus_14
    
        if dic["ch05_3plyr_a"] == "anger":
            show se 5 at t11
            voice "se35.ogg"
            s "있지, 소문 낸 애들, 그리고 그걸 믿는 다른 애들보다" #anger
            voice "se36.ogg"
            s "네가 세상에서 제일 나빠." #anger
            show se 2 at t11
            voice "se37.ogg"
            s "약속은 없던 걸로 하자. 갈게." #sad
        elif dic["ch05_3plyr_a"] == "apologize":
            show se 2 at t11
            voice "se38.ogg"
            s "이미 늦었어. 나는 그래도 너만은 날 믿어주길 바랐어." #sad
            
            call qus("ch05_3plyr_a_a") from _call_qus_15

            if dic["ch05_3plyr_a_a"] == "apologize":
                show se 2 at t11
                voice "se39.ogg"
                s "...휴..." #sad
                show se 1 at t11
                voice "se40.ogg"
                s "아무튼, 난 안 그랬어. 정말이야. 그렇게도 날 모르냐." #normal
                show se 3 at t11
                voice "se41.ogg"
                s "다음부터는 내 얘기부터 먼저 들어줘. 양쪽 얘기를 다 듣고 나서 판단해도 괜찮잖아." #smile
                
                voice "se42.ogg"
                s "...나도 무턱대고 화내서 미안해. 일단 갈게, 수업 시작한다. 좀 있다 보자." #smile
            elif dic["ch05_3plyr_a_a"] == "anger":
                show se 5 at t11
                voice "se43.ogg"
                s "됐다. 그만하자." #anger
                hide se
                voice "se44.ogg"
                s "오늘 약속은 없던 걸로 해. 먼저 간다." #anger


    elif dic["ch05_3plyr"] == "believe":
        show se 1 at t11
        voice "se45.ogg"
        s "정말로? 내가 그러지 않았다는 것을 믿어? 확신할 수 있어?" #normal

        call qus("ch05_3plyr_b") from _call_qus_16

        if dic["ch05_3plyr_b"] == "believe":
            show se 2 at t11
            voice "se46.ogg"
            s "...그렇구나." #sad
            voice "se47.ogg"
            s "그래, 네가 아무것도 묻지 않고서 날 의심할 리가 없는데..." #sad
            show se 1 at t11
            voice "se48.ogg"
            s "미안. 나도 너무 화가 나서 괜히 너한테 화풀이한 것 같아." #normal
            show se 3 at t11
            voice "se49.ogg"
            s "하하.. 괜히 어색해지네. 진짜 미안해." #smile
            voice "se50.ogg"
            s "조금 있다 벚꽃 보러갈 때 다시 얘기하자. 나도 조금 진정할 시간이 필요할 것 같아." #smile

            call qus("ch05_3plyr_b_a") from _call_qus_17

            if dic["ch05_3plyr_b_a"] == "worry":
                show se 3 at t11
                voice "se51.ogg"
                s "걱정해줘서 고마워. 그런데 네가 믿어준다니까 다 괜찮아졌어! 정말로." #smile
                voice "se52.ogg"
                s "조금 있다가 봐!" #smile
                hide se
            elif dic["ch05_3plyr_b_a"] == "positive":
                show se 3 at t11
                voice "se53.ogg"
                s "응, 조금 있다가 보자! 오늘 벚꽃 보러가기로 했으니까." #smile
                hide se

        elif dic["ch05_3plyr_b"] == "notbelieve":
            show se 5 at t11
            voice "se54.ogg"
            s "장난치는 거야?" #anger
            voice "se55.ogg"
            s "나는 진지하게 들어주길 바랐어." #anger
            show se 2 at t11
            voice "se56.ogg"
            s "정말 다른 아이들은 몰라도 너만은 내 이야기를 진심으로 들어줄 줄 알았는데." #sad
            show se 5 at t11
            voice "se57.ogg"
            s "갈게. 오늘은.. 그냥 일찍 집에 갈게." #anger
            hide se

    elif dic["ch05_3plyr"] == "explain":
        show se 4 at t11
        voice "se58.ogg"
        s "설명할 것도 없이, 난 애초에 안 그랬어. 내가.." #surpirse
        show se 2 at t11
        voice "se59.ogg"
        s "내가 널 얼마나 소중히 여기는데! 알잖아!" #sad
    
        call qus("ch05_3plyr_c") from _call_qus_18

        if dic["ch05_3plyr_c"] == "agree":
            show se 5 at t11
            voice "se60.ogg"
            s "뭘 알아 또!" #anger
            show se 2 at t11
            voice "se61.ogg"
            s "휴..." #sad
            show se 1 at t11
            voice "se62.ogg"
            s "...미안해." #normal
            voice "se63.ogg"
            s "괜히 화가 나서 너한테 뭐라고 한 것 같다." #normal
            show se 3 at t11
            voice "se64.ogg"
            s "아무튼 수업 시작하니까 조금 있다가 봐. 약속 안 잊었지?" #smile
            voice "se65.ogg"
            s "그 때 더 얘기하자. 조금 있다가 봐." #smile
            hide se

        elif dic["ch05_3plyr_c"] == "disagree":
            show se 5 at t11
            voice "se66.ogg"
            s "장난치지 마, 진짜." #anger
            show se 2 at t11
            voice "se67.ogg"
            s "부끄러움을 무릅쓰고 말하는 거야." #sad
            show se 1 at t11
            voice "se68.ogg"
            s "난 절대로 너에 대해서 그렇게 말한 적 없어. 믿어줄래?" #normal

            call qus("ch05_3plyr_c_a") from _call_qus_19

            if dic["ch05_3plyr_c_a"] == "believe":
                show se 3 at t11
                voice "se69.ogg"
                s "그래, 고마워." #smile
                voice "se70.ogg"
                s "진심이야." #smile
                voice "se71.ogg"
                s "수업 시작하니까 이만 가 볼게. 화내지 않고, 몰아세우지 않고 들어줘서 고맙다." #smile
                hide se
            elif dic["ch05_3plyr_c_a"] == "notbelieve":
                show se 2 at t11
                voice "se72.ogg"
                s "......진짜 너무한다, 너." #sad
                voice "se73.ogg"
                s "됐어, 갈게." #sad
                voice "se74.ogg"
                s "벚꽃은 나중에 보러 가자." #sad
                hide se


    elif dic["ch05_3plyr"] == "apologize":
        show se 5 at t11
        voice "se75.ogg"
        s "뭐가 미안한데. 정말로 날 안 믿은 거야?" #anger
        
        call qus("ch05_3plyr_d") from _call_qus_20

        if dic["ch05_3plyr_d"] == "believe":
            show se 5 at t11
            voice "se76.ogg"
            s "장난치는 거야?" #anger
            voice "se77.ogg"
            s "나는 진지하게 들어주길 바랐어." #anger
            show se 2 at t11
            voice "se78.ogg"
            s "정말 다른 아이들은 몰라도 너만은 내 이야기를 진심으로 들어줄 줄 알았는데." #sad
            show se 5 at t11
            voice "se79.ogg"
            s "갈게. 오늘은.. 그냥 일찍 집에 갈게." #anger
            hide se
        elif dic["ch05_3plyr_d"] == "notbelieve":
            show se 5 at t11
            voice "se80.ogg"
            s "있지, 소문 낸 애들, 그리고 그걸 믿는 다른 애들보다" #anger
            voice "se81.ogg"
            s "네가 세상에서 제일 나빠." #anger
            show se 2 at t11
            voice "se82.ogg"
            s "약속은 없던 걸로 하자. 갈게." #sad

    return
    
label ch06_main:
    scene cr1_night
    with dissolve_scene_full
    "나한테는 두 가지 선택만이 남았다."
    "서은이와의 약속을 지킬 건지, 효주를 만나 내 호기심을 해소할 것인지."
    
    call qus("ch06_1plyr") from _call_qus_21

    if dic["ch06_1plyr"] == "seoeun":
        "그래, 서은이를 만나러 가자."
    if dic["ch06_1plyr"] == "hyoju":
        "중요한 이야기일지도 몰라. 벚꽃은 나중에 보더라도 효주의 이야기를 먼저 듣자."
    scene black
    return



label ch07_main:
    call right
    scene present_day
    with dissolve_scene_full
    "2018년 봄, 레스토랑 앞."
    "오늘은 고등학교 동창회다. 어느덧 서른을 앞둔 나이에 고등학교 친구들을 다시 볼 생각을 하니 조금 들뜬 마음이다."
    "사실, 제일 궁금한 건 서은이였다. 3년을 붙어 다닌, 피곤하지만 밉지 않은 내 친구."
    "벌써부터 북적거리는 레스토랑 안은 친숙하면서도 낯선 사람들로 가득 차 있다."
    "성인이 된다는 것에 막연한 불안함이 있던 열아홉은 한 명도 없었다."
    "그때보다 부쩍 자라버린 어른들만 있을 뿐이었다. 기분이 묘했다."
    "친구들과 반갑게 인사를 하며 안부를 묻는 중에도 내 눈은 계속 서은이를 찾고 있었다."
    "하지만 보이지 않는다. 이런 자리에 빠질 애가 아닌데..."
    show hj 1 at t11
    voice "se83.ogg"
    h "오랜만이네. 잘 지냈어?" #normal

    call qus("ch07_1plyr") from _call_qus_22

    if dic["ch07_1plyr"] == "positive":
        show hj 3 at t11
        voice "se84.ogg"
        h "그렇구나. 좋아 보이네." #smile
    elif dic["ch07_1plyr"] == "negative":
        show hj 3 at t11
        voice "se85.ogg"
        h "뭐... 그래, 힘내." #smile
    elif dic["ch07_1plyr"] == "ask":
        show hj 3 at t11
        voice "se86.ogg"
        h "응, 잘 지냈지. 얼마 전에 겨우 취직했거든. 이제 좀 살 맛 나더라." #smile
    

    "효주라면 서은이의 행방을 알고 있을지도 모른다. 물어보자."
    "서은이 어디 있는지 알아?"
    voice "se87.ogg"
    h "...농담하는 거지?"

    call qus("ch07_2plyr") from _call_qus_23

    if dic["ch07_2plyr"] == "answer":
        show hj 5 at t11
        voice "se88.ogg"
        h "장난치지 마. 나 이런 장난 싫어해." #anger
    
    "효주의 표정이 많이 불안해 보인다. 그냥 단순한 질문인데 주위의 술렁임이 느껴진다. 대체 왜?"

    if dic["ch02_3plyr_b"] == "positive" and (dic["ch03_2plyr"] == "negative" or dic["ch03_5plyr"] == "lie") and dic["ch05_3plyr_a_a"] == "apologize" and dic["ch05_2plyr_b"] == "believe" and dic["ch05_3plyr_b_a"] == "worry" and dic["ch05_3plyr_c"] == "agree" and dic["ch05_3plyr_c_a"] == "believe" and dic["ch06_1plyr"] == "seoeun":
        $ _end = "good"
    else:
        $ _end = "bad"
    
    if _end == "good":
        call ch07_1_main from _call_ch07_1_main
    else:
        call ch07_2_main from _call_ch07_2_main
    return


label ch07_1_main:
    scene present_day
    show hj 1 at t11
    voice "se89.ogg"
    h "정말 기억 안 나? 서은이는..." #normal
    show hj 2 at t11
    voice "se90.ogg"
    h "서은이는 죽었잖아. 10년 전 오늘, 학교에서." #sad
    "정신이 멍해진다. 서은이가 죽었다고?"
    show hj 1 at t11
    voice "se91.ogg"
    h "교통사고. 정말 기억 안 나? 너 오늘 좀 이상하다." #normal
    "서은이가 죽었다고? 대체 왜?"
    "멍해진 정신이 좀 더 흐릿해진다. 눈 앞이 아득하다. 몸이 기울어진다."
    show hj 4 at t11
    voice "se92.ogg"
    h "...야! 정신차려!!" #surprise
    "기억이 어긋난 것처럼 아파온다. 억지로 들어낸 것처럼 지운 자국이 선명하다."
    scene black
    "서은이가 그랬을 리 없다. 서은이가 죽었을 리 없다. 혼란스럽다. 그 때였다."
    d "당신이 과거에 했을 작은 선택으로 모든 것을 바꿀 수 있다면?"
    "칠흑 같은 어둠 속에서 의문의 목소리가 들려온다."
    d "그 선택으로 당신의 소중한 사람을 살릴 수 있다면?"
    "서은이를 살릴 수 있다고? 하지만, 이미 10년 전에 죽은 아이를 어떻게?"
    d "잘 생각해봐. 그 날의 너를."
    "수수께끼 같은 말과 함께, 나는 다시 끝없는 어둠 속으로 추락했다."
    "아래로... 아래로... 아래로..."

    return



label ch07_2_main:
    scene present_day
    show se 3 at t11
    voice "se93.ogg"
    s "나를 왜 걔한테 물어봐." #smile
    "이 목소리는..."
    voice "se94.ogg"
    s "왜 그렇게 쳐다 봐? 죽은 사람 돌아온 것처럼. 오랜만이네?" #smile
    "오랜만에 만난 서은이는 10년 전처럼 장난끼 넘쳤고, 기운찼다."
    show se 1 at t11
    voice "se95.ogg"
    s "밥이나 먹자. 배고파." #normal

    call qus("ch07_2_1plyr") from _call_qus_24

    if dic["ch07_2_1plyr"] == "positive":
        show se 3 at t11
        voice "se96.ogg"
        s "그럼 빨리 일어나. 너 때문에 밥 먹을 시간이 줄고 있잖아." #smile
    elif dic["ch07_2_1plyr"] == "negative":
        show se 3 at t11
        voice "se97.ogg"
        s "빨리 나와라. 음식 다 떨어지기 전에." #smile
    elif dic["ch07_2_1plyr"] == "nonsense":
        show se 1 at t11
        voice "se98.ogg"
        s "갑자기 무슨 헛소리야? 빨리 나오기나 해. 나 배고프다니까." #normal

    call qus("ch07_2_2plyr") from _call_qus_25

    if dic["ch07_2_2plyr"] == "normal":
        show se 3 at t11
        voice "se99.ogg"
        s "가자가자!!" #smile
    elif dic["ch07_2_2plyr"] == "joy":
        show se 2 at t11
        voice "se100.ogg"
        s "......너 이상해." #sad
    elif dic["ch07_2_2plyr"] == "sad":
        show se 5 at t11
        voice "se101.ogg"
        s "안돼. 빨리 나와, 빨리!!!" #anger
    elif dic["ch07_2_2plyr"] == "anger":
        show se 3 at t11
        voice "se102.ogg"
        s "새삼스럽게 왜 화내. 익숙해질 때도 됐잖아. 아, 오랜만이라 적응이 안 되나?" #smile


    "전에도 비슷한 대화를 한 것 같은데, 기분이 묘하다."
    show se 3 at t11
    voice "se103.ogg"
    s "무슨 생각을 그렇게 해. 얼른 일어나라니까! 가자!" #smile
    "10년이나 지났음에도 우리는 변함없이 티격태격했고 철이 없었다."
    "이상하다. 제멋대로인 서은이의 모습에 짜증이 나면서도 왠지 모를 안도감이 찾아온다."
    "그리웠었다. 다시는 못 볼 사이였던 것처럼."
    "하지만 서은이는 지금 여기 있다."
    "여전히, 그 날처럼."
    
    return

label ch10_main:
    scene cr1_day
    "이상하다."
    "엄청 생생한 꿈을 꾼 것 같은데..."
    "무언가 소중한 것을 잃어버린 듯한 느낌이 들었다."
    call nd2_start from _call_nd2_start
    return


label start_game:
    python:
        import os
        import io
        while(1):
            num = 0
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
            f = io.open(comm, mode="r", encoding="utf-8")
            a,b,c = f.read().splitlines()
            f.close()
            if ("시작" in a) and (c != "neg"):
                break