# py2port_pygame_template

A standalone Pygame starter game and GitHub repository template. Move a square
with the keyboard or a gamepad, then build your own game from this working loop.
The game runs on a normal computer without py2ports, Docker, or a handheld.

This template is public and [MIT-licensed](LICENSE), including its inherited
game code, with the owner's authorization for public redistribution. Preserve
the license and origin attribution in games made from it.

## Create your own game

1. Open [py2port_pygame_template](https://github.com/OscarJHernandez/py2port_pygame_template).
2. Select **Use this template → Create a new repository**.
3. Choose your game's repository name and visibility (public or private).
4. Clone your new repository and run:

```sh
git clone https://github.com/YOU/YOUR-GAME.git
cd YOUR-GAME
make setup
make run
```

You need Python 3.11+ and Make. If your default Python is older, use
`make setup PYTHON=python3.12`. GitHub creates independent history for your
template-generated repository; you do not need to fork or clone the original
game repository's history.

To try this template itself, clone this repository and use the same Make commands.

## Controls and tests

- Move: arrow keys or a gamepad D-pad.
- Exit: Escape, window close, or gamepad buttons 6, 9, or 10.

```sh
make test
```

The desktop smoke test runs the real entrypoint for one frame with dummy SDL
video/audio and posts a quit event. It does not contact a handheld.

Without Make, create a virtual environment, install `requirements.txt`, then run
`python src/run.py` and `python -m unittest discover -s tests`.

## Customize

```text
src/main.py             # game loop, drawing, input, screen size and frame rate
src/run.py              # thin desktop entrypoint
assets/                 # add your own images, sounds and fonts
tests/test_desktop.py   # headless entrypoint smoke test
requirements.txt        # desktop dependencies
Makefile                # setup, play and test
```

Start by editing `src/main.py`; keep `src/run.py` as a thin entrypoint. Resolve
assets relative to your source files as described in `assets/README.md`. Add
tests as your game develops. Do not commit credentials, virtual environments,
generated packages, or private build outputs.

## Deploy your game with py2ports

From your separate py2ports checkout:

```sh
.venv/bin/py2ports add https://github.com/YOU/YOUR-GAME.git \
    --name my_game --entrypoint src/run.py
make validate GAME=my_game
make check-device
make deploy GAME=my_game
```

Review the generated manifest and set `include = ["src", "assets", "README.md", "LICENSE"]`.
Keep `publish = false` unless you intend public releases and all game content
and dependencies permit redistribution. Commit the manifest, `.gitmodules`, and pinned gitlink
in py2ports. Use `DEVICE_HOST=<device-IP>` if the hostname `knulli` is unavailable.
Deployment checks the device before building and preserves other installed games.

Knulli runtime, launcher, and SSH configuration belong in py2ports, not this
standalone template. Desktop requirements retain `pygame==2.6.1`; the existing
py2ports device profile supplies Pygame-CE 2.5.6 and Python 3.12.8.
For saves, deployed games can use `PY2PORTS_DATA_DIR` supplied by the launcher.

## Origin and license

The unchanged `src/main.py` and `src/run.py` originate from Oscar Javier
Hernandez's private `OscarJHernandez/python_game` repository at commit
`8a63594750dea6553a5e44dabe6e7a737371b747`, copied with the owner's
authorization. This repository starts with a new root commit; the original
repository and the earlier `py2ports-example-game` repository are unchanged.
No assets were tracked in the original revision.

The owner has authorized releasing this template, including the inherited game
code, under the MIT license in this repository. This authorization supersedes
the earlier private-distribution restriction for this template. The original
repositories remain private and unchanged. Future third-party assets retain
their own licenses. Preserve this origin attribution and the MIT notice when
creating a game from the template. This is unofficial and not affiliated with Knulli.
