import curses
import asyncio
import random
import time

TIC_TIMEOUT = 0.1


async def blink(canvas, row, column, symbol, ping):
    for _ in range(ping):
        await asyncio.sleep(0)
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        for _ in range(20):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        for _ in range(5):
            await asyncio.sleep(0)

        canvas.addstr(row, column, symbol)
        for _ in range(3):
            await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    symbols = "+*.:"
    ping = 50
    y, x = canvas.getmaxyx()
    coroutines = [blink(canvas, row=random.randint(0, y), column=random.randint(0, x), symbol=random.choice(symbols), ping=random.randint(10, ping))
                  for _ in range(100)]

    while True:
        for coroutine in coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                coroutines.remove(coroutine)
                break
            except RuntimeError:
                pass
            except curses.error:
                pass
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
