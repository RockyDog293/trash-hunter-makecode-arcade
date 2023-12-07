controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Mouse.overlapsWith(Fish)) {
        info.changeScoreBy(-1)
        Fish.setPosition(randint(20, 140), randint(20, 100))
    } else {
        if (Mouse.overlapsWith(Trash)) {
            info.changeScoreBy(1)
            Trash.setPosition(randint(20, 140), randint(20, 100))
        }
    }
})
info.onCountdownEnd(function () {
    game.gameOver(false)
})
info.onScore(-2, function () {
    game.gameOver(false)
})
info.onScore(5, function () {
    game.gameOver(true)
})
let Mouse: Sprite = null
let Trash: Sprite = null
let Fish: Sprite = null
info.startCountdown(45)
info.setScore(0)
effects.bubbles.startScreenEffect()
scene.setBackgroundColor(9)
Fish = sprites.create(img`
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
    `, SpriteKind.Player)
Trash = sprites.create(img`
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
    `, SpriteKind.Player)
Mouse = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(Mouse)
Mouse.setStayInScreen(true)
Fish.setPosition(randint(20, 140), randint(20, 100))
Trash.setPosition(randint(20, 140), randint(20, 100))
game.onUpdateInterval(randint(1000, 3000), function () {
    Fish.setPosition(randint(20, 140), randint(20, 100))
})
game.onUpdateInterval(randint(1000, 3000), function () {
    Trash.setPosition(randint(20, 140), randint(20, 100))
})
