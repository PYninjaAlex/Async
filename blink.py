import curses
import asyncio


async def blink(canvas, row, column, symbol='*'):
    while True:
        canvas.addstr(row, column, symbol, curses.A_DIM)
        await asyncio.sleep(2)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0.3)

        canvas.addstr(row, column, symbol, curses.A_BOLD)
        await asyncio.sleep(0.5)

        canvas.addstr(row, column, symbol)
        await asyncio.sleep(0.3)


async def draw(canvas):
    curses.curs_set(False)
    row, column = (5, 20)
    canvas.border()

    coroutine = blink(canvas, row=row, column=column)

    while True:
        try:
            coroutine.send(None)
            await asyncio.sleep(0)
        except StopIteration:
            break    


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(asyncio.run(draw))