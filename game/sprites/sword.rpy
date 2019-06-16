image sword = Movie(
        play = "sword-ready.webm",
        start_image = "sword-ready_S.png",
        image = "sword-ready.png",
        side_mask=True
    )

image sword aim = Movie(
        play = "sword-aim.webm",
        start_image = "sword-aim_S.png",
        image = "sword-aim.png",
        side_mask=True
    )

image sword fire = Movie(
        play = "sword-fire.webm",
        start_image = "sword-fire_S.png",
        image = "sword-fire.png",
        side_mask=True,
        loop = False
    )

image sword thumbnail:
    "sword-ready.png"
    zoom 0.3
