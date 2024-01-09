from multiprocessing import Process, current_process
from time import sleep
import os

def sub_task(content, nums):
    # 通过current_process函数获取当前进程对象
    # 通过进程对象的pid和name属性获取进程的id号和名字
    print(f'PID:{current_process().pid}')
    print(f'Name:{current_process().name}')

    current, total = 0, nums.pop(0)
    print(f'Loop count:{total}')
    sleep(0.5)
    while current < total:
        current += 1
        print(f'{current}: {content}')
        sleep(0.01)

def main():
    nums = [20, 30, 40]
    Process(target=sub_task, args=('Ping', nums)).start()
    Process(target=sub_task, args=('Pong', nums)).start()
    sub_task('Good', nums)

if __name__ == '__main__':
    main()
