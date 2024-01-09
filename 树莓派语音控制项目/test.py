import time

if __name__ == '__main__':
    i = 0
    state = True
    while(True):
        i += 1
        state = not state
        print('开关状态:', state)
        time.sleep(3)
        if i > 21:
            break
