define e = Character('아이린', color="#c8ffc8")
define s = Character('서은', color="#222")

label right:
    $ gui.direction = 0.75
    $ gui.xdirection = 1.0
    $ renpy.log(gui.direction)
    $ gui.rebuild()
    return

image ch01_bg = "b.png"
label start:

    call ch01_main
    call ch02_main

    return

label ch01_main:
    scene ch01_bg
    "2008년, 봄. XX고등학교."
    s "…야."
    "어디선가 목소리가 들린다."
    s "야."
    "목소리가 꽤 또렷하게 들리지만 고개는 여전히 무겁다. 아직 일어나기 싫다."
    #call right
    s "일어나. 점심시간이야."
    "몽롱한 정신으로 고개를 들어 보니 어느 여자아이가 서 있다."
    s "점심시간이라니까? 수업 중에 잠이나 자고. 양아치네. 아무튼 점심 먹으러 안 가?"
    menu:
        "갈게 갈게":
            s "그럼 빨리 일어나. 너 때문에 밥 먹을 시간이 줄고 있잖아."
        "안먹을래":
            s "지금 가야 맛있는 것 많이 먹을 수 있단 말이야. 빨리 나와."
        "의이에에이ㅣ잉??!???!":
            s "갑자기 무슨 헛소리야. 빨리 나오기나 해. 나 배고파."
    #call ar ("ch01_ans")
    #if ch01_ans == "pos":
    #    s "그럼 빨리 일어나. 너 때문에 밥 먹을 시간이 줄고 있잖아." 
    #elif ch01_ans == "neg":
    #    s "지금 가야 맛있는 것 많이 먹을 수 있단 말이야. 빨리 나와."
    #else:
    #   s "갑자기 무슨 헛소리야. 빨리 나오기나 해. 나 배고파."
    "이럴 거면 왜 물어 본건지… 결국 잠이 덜 깬 몸을 일으켜 급식실로 향한다."
    return