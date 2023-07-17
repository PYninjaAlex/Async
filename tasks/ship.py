import curses
import asyncio
import random
import time

TIC_TIMEOUT = 0.1


def read_frame_1():
    with open("rocket_frames/rochet_frame_1.txt", mode="r", encoding="utf-8") as frame_1:
        res = frame_1.read()
    return res


def read_frame_2():
    with open("rocket_frames/rocket_frame_2.txt", mode="r", encoding="utf-8") as frame_2:
        res = frame_2.read()
    return res


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


async def animate_space_ship(canvas, frame, row=6, column=122, ping=10):
    for _ in range(ping):
        await asyncio.sleep(0)
    while True:
        canvas.addstr(row, column, frame)
        for _ in range(ping):
            await asyncio.sleep(0)


def draw(canvas):
    curses.curs_set(False)
    canvas.border()
    symbols = "+*.:"
    ping = 50
    y, x = canvas.getmaxyx()
    stars_coroutines = [
        blink(canvas, row=random.randint(0, y), column=random.randint(0, x), symbol=random.choice(symbols),
              ping=random.randint(10, ping))
        for _ in range(100)]

    ship_frame_1 = read_frame_1()
    ship_frame_2 = read_frame_2()
    ship_coroutines = [animate_space_ship(canvas, ship_frame_1), animate_space_ship(canvas, ship_frame_2)]
    iterator = 0

    while True:
        for coroutine in stars_coroutines:
            try:
                coroutine.send(None)
            except StopIteration:
                stars_coroutines.remove(coroutine)
                break
            except RuntimeError:
                pass
            except curses.error:
                pass
        try:
            if not iterator or not iterator % 2:
                coroutine = ship_coroutines[0]
            else:
                coroutine = ship_coroutines[1]
            coroutine.send(None)
        except StopIteration:
            stars_coroutines.remove(coroutine)
            break
        except RuntimeError:
            pass
        except curses.error:
            pass
        iterator += 1
        canvas.refresh()
        time.sleep(TIC_TIMEOUT)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)
