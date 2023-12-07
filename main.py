def on_a_pressed():
    if Mouse.overlaps_with(Fish):
        info.change_score_by(-1)
        Fish.set_position(randint(20, 140), randint(20, 100))
    else:
        if Mouse.overlaps_with(Trash):
            info.change_score_by(1)
            Trash.set_position(randint(20, 140), randint(20, 100))
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_countdown_end():
    game.game_over(False)
info.on_countdown_end(on_countdown_end)

def on_on_score():
    game.game_over(False)
info.on_score(-2, on_on_score)

def on_on_score2():
    game.game_over(True)
info.on_score(5, on_on_score2)

Mouse: Sprite = None
Trash: Sprite = None
Fish: Sprite = None
info.start_countdown(45)
info.set_score(0)
effects.bubbles.start_screen_effect()
scene.set_background_color(9)
Fish = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . c c c c . . . . 
            . . . . . . c c d d d d c . . . 
            . . . . . c c c c c c d c . . . 
            . . . . c c 4 4 4 4 d c c . . . 
            . . . c 4 d 4 4 4 4 4 1 c . c c 
            . . c 4 4 4 1 4 4 4 4 d 1 c 4 c 
            . c 4 4 4 4 1 4 4 4 4 4 1 c 4 c 
            f 4 4 4 4 4 1 4 4 4 4 4 1 4 4 f 
            f 4 4 4 f 4 1 c c 4 4 4 1 f 4 f 
            f 4 4 4 4 4 1 4 4 f 4 4 d f 4 f 
            . f 4 4 4 4 1 c 4 f 4 d f f f f 
            . . f f 4 d 4 4 f f 4 c f c . . 
            . . . . f f 4 4 4 4 c d b c . . 
            . . . . . . f f f f d d d c . . 
            . . . . . . . . . . c c c . . .
    """),
    SpriteKind.player)
Trash = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . f f f . . . . . . . 
            . . . . . . f f f . . . . . . . 
            . . f f f f f f f f f f f f . . 
            . . f f f f f f f f f f f f . . 
            . . f f f f f f f f f f f f . . 
            . . f f f f f f f f f f f f . . 
            . . f f f f f f f f f f f f . . 
            . . . f f f f f f f f f f . . . 
            . . . . f f f f f f f f . . . . 
            . . . . f f f f f f f . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
Mouse = sprites.create(img("""
        .........2.........
            .........2.........
            .........2.........
            .........2.........
            .........2.........
            .........2.........
            .........2.........
            ...................
            22222222.2.22222222
            ...................
            .........2.........
            .........2.........
            .........2.........
            .........2.........
            .........2.........
            .........2.........
            .........2.........
    """),
    SpriteKind.player)
controller.move_sprite(Mouse)
Mouse.set_stay_in_screen(True)
Fish.set_position(randint(20, 140), randint(20, 100))
Trash.set_position(randint(20, 140), randint(20, 100))

def on_update_interval():
    Fish.set_position(randint(20, 140), randint(20, 100))
game.on_update_interval(randint(1000, 3000), on_update_interval)

def on_update_interval2():
    Trash.set_position(randint(20, 140), randint(20, 100))
game.on_update_interval(randint(1000, 3000), on_update_interval2)
