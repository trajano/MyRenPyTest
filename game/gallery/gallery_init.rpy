init python:
    g = Gallery()

    g.button("sword")
    g.image("bg holodeck", "sword")
    g.image("bg holodeck", "sword aim")
    g.image("bg holodeck", "sword fire")
    g.unlock("bg holodeck", "sword")
    g.unlock("bg holodeck", "sword aim")
    g.unlock("bg holodeck", "sword fire")
    
    g.transition = dissolve
