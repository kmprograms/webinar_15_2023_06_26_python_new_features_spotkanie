from dataclasses import dataclass
import asyncio
import aiofiles

# ITERATOR ASYNCHRONICZNY

@dataclass
class AsyncIt:

    counter: int = 0

    def __aiter__(self):
        print('Async Iteration Started')
        return self

    async def __anext__(self):
        if self.counter > 20:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        self.counter += 1
        return self.counter


async def a_fun():
    ait = AsyncIt(10)
    async for v in ait:
        print(v)

# asyncio.run(a_fun())


# Mozesz w Python rzucic wiele wyjatkow naraz
# try:
#     raise ExceptionGroup("Exception Group for multiple errors", (
#         ValueError("Value Error"),
#         TypeError("Type Error"),
#         KeyError("Key Error"),
#         AttributeError('Attribute Error')
#     ))
# # Different ways of handling errors
# except* AttributeError as exc:
#     print(f'AE: {exc}')
# except* (ValueError, TypeError) as exc:
#     print(f'VE|TE: {exc}')
# except* KeyError as exc:
#     print(f'KE: {exc}')

async def read_file(filename: str) -> None:
    async with aiofiles.open(filename, mode='r') as f:
        async for line in f:
            print(line)
    print('File end')

async def fetch_data(data: int) -> dict[str, int]:
    if data == 0:
        raise Exception('No data found')
    print('Fetch end')
    return {'data': data}

async def main() -> None:

    # Ten sposob w obliczu bledu przerywa dzialanie wszystkich taskow
    # tasks = asyncio.gather(
    #     fetch_data(1),
    #     fetch_data(2),
    #     read_file('xxx.txt')
    # )
    # res = await tasks
    # print(res)

    # tasks = asyncio.gather(
    #     fetch_data(1),
    #     fetch_data(2),
    #     read_file('xxx.txt'),
    #     return_exceptions=True
    # )
    # res = await tasks
    # print(res)

    # TaskGroup
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(fetch_data(1))
            tg.create_task(fetch_data(2))
            tg.create_task(fetch_data(3))
            tg.create_task(read_file('data1.txt'))

        # W tym miejscu (poza asynchronicznym context managerem) mozesz do task1
        # odwolac sie bez niczego, nie musisz pisac await, bo tutaj masz juz pewnosc
        # ze wszystkie taski uruchomione w async context managerze sa skonczone
        # Jedyne co to wyluskujesz konkretne daje z otrzymanej struktury
        print(task1.result())
    except* FileNotFoundError as ferr:
        print(ferr.exceptions)
    except* Exception as ex:
        print(ex.exceptions)

asyncio.run(main())