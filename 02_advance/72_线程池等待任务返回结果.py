from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
import time

def work(x):
    time.sleep(x)
    return x

with ThreadPoolExecutor(3) as pool:
    fs = [pool.submit(work, t) for t in [2,1,3]]
    done, pending = wait(fs, return_when=FIRST_COMPLETED)
    print("最先完成任务结果：", [d.result() for d in done])