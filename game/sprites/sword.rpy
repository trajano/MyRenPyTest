image sword = Movie(
        play = "sword-ready.webm",
        start_image = "sword-ready_S.png",
        image = "sword-ready.png",
        side_mask=True
    )

image base sword aim = Movie(
        play = "sword-aim.webm",
        start_image = "sword-aim_S.png",
        image = "sword-aim.png",
        side_mask=True
    )

image base sword fire = Movie(
        play = "sword-fire.webm",
        start_image = "sword-fire_S.png",
        image = "sword-fire.png",
        side_mask=True,
        loop = True
    )

image don: 
    "base sword aim"
    crop (480,0,960, 1080)
image don talking: 
    "base sword fire"
    crop (480,0,960, 1080)
image bo: 
    "base sword aim"
    crop (480,0,960, 1080)
    yzoom -1.0
image bo talking: 
    "base sword fire"
    crop (480,0,960, 1080)
    yzoom -1.0
image sword thumbnail:
    "sword-ready.png"
    zoom 0.3
