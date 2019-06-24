init python:
    g = Gallery()

    g.button("sword")
    g.image("bg holodeck", "sword")
    g.unlock("sword")
    g.image("bg holodeck", "sword aim")
    g.unlock("sword aim")
    g.image("bg holodeck", "sword fire")
    g.unlock("sword fire")
    
    g.transition = dissolve
