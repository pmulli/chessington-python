Chessington
===========

Starter project for a chess-based TDD exercise.

Running the application
-----------------------

To run the application, first ensure that you have installed Poetry_ on your system. Install
dependencies using the command `poetry install`.

To run the application, use the command `poetry run start`. This will pop up a window containing
a chess board. Clicking on one of the white pieces will highlight the square that piece is on,
and also show you the squares it can move to. Except...

None of the rules of chess have been implemented yet! That's your job :)

Notes for WSL users
-------------------

Sadly, WSL does not support GUIs, so this application will not work from a WSL terminal. Sorry :(

.. _Poetry: https://github.com/sdispater/poetry