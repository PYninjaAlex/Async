import curses
import asyncio
import random
import time


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    row, column = (5, 20)
    coroutines = [blink(canvas, row=row + i, column=column - i) for i in range(5)]

    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
                break
        canvas.refresh()
        time.sleep(0.5)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
