import asyncio

import websockets


# Асинхронная функция клиента
async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение, которое отправит клиент
        print(f"Отправка: {message}")
        await websocket.send(message)  # Отправляем сообщение

        # Получаем 5 ответов от сервера
        for _ in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")


# Запуск клиента
asyncio.run(client())
