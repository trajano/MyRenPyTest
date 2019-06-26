image base tree = Movie(
        play = "tree.webm",
        start_image = "tree-aim_S.png",
        image = "tree-aim.png",
        side_mask=True
    )

image base tree fire = Movie(
        play = "tree-fire.webm",
        start_image = "tree-fire_S.png",
        image = "tree-fire.png",
        side_mask=True,
        loop = True
    )


image bo: 
    "base tree aim"
    zoom 0.5
image bo talking: 
    "base tree fire"
    zoom 0.5
