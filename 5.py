import asyncio
from proxy_handler import main

async def main_script():
    user_id = input("Masukkan user ID: ")  # Meminta user_id dari pengguna
    await main('proxy_5.txt', user_id)

if __name__ == "__main__":
    asyncio.run(main_script())