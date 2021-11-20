from time import sleep
from tqdm import tqdm
from colorama import Fore
from models.product import Produto

ps4 = Produto('PlayStation 4', 2284.12)
xbox = Produto('Xbox Series X', 1823.92)

print(ps4)
print(xbox)

for i in tqdm(range(5)):
    sleep(0.5)
