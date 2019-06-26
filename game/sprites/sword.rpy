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
    zoom 0.5
image don talking: 
    "base sword fire"
    zoom 0.5

