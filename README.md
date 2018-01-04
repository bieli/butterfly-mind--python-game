# Butterfly Mind - experimental logic game for girls & geeks ;-)

[![Build Status](https://travis-ci.org/bieli/butterfly-mind--python-game.png)](https://travis-ci.org/bieli/butterfly-mind--python-game)

## Inspiration and game scenario

General idea it's training important area in our head - short memory.

Program draw 3 letters in easy mode or butterflies in hard mode
on screen and we must to remember letters or shapes of butterflies.
Next after we click 1 or 2 or 3 key (referenced to object line)
we can see next set of butterflies, but only one is from last set.

We have 120 seconds to the end of game.
We can see seconds/scoring information on game screen.

Difficult in this game it's select letter or butterfly shape
in new set from last set.

## Screen shots

![Welcome screen shot](https://raw.githubusercontent.com/bieli/butterfly-mind--python-game/master/resources/img/screen_shots/welcome_screenshot.png)

![Game screen shot - mode EASY](https://raw.githubusercontent.com/bieli/butterfly-mind--python-game/master/resources/img/screen_shots/game_screenshot.1.png)

![Game screen shot - mode HARD](https://raw.githubusercontent.com/bieli/butterfly-mind--python-game/master/resources/img/screen_shots/game_screenshot.3.png)


## How to run
```
$ python3.5 run_game.py
```

## Technology
- programming language: Python >= 3.5
- game development library: PyGame >= 1.9.3

## Supported platforms
- Linux
- Unix
- *BSD
- MacOSX
- Windows
- Android

## Development

#### How to running unit tests (warning! took a few minutes)

```
$ cd <project-dir>
$ python3.5 -m unittest tests.ToolsTest.TestTools
```

## TODO LIST
- [x] welcome scene
- [x] welcome controls (ESCAPE, ENTER)
- [x] game scene
- [ ] game controls (ESCAPE, SAPACE)
- [x] game logic library
- [x] unit tests for game logic library
- [ ] summary / scores / winners scene
- [ ] music
- [ ] refactoring
- [ ] multiplatform automatic builds in releases
- [ ] performance in rivalization & points & levels
