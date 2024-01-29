# 导入模块
import subprocess
import threading
from queue import Queue
from queue import Empty

# 定义一个空列表，用于存储活跃主机
alives = []

# 定义一个函数，用于调用ping命令
def call_ping(ip):
    # 如果ping成功，打印活跃信息，并将IP地址添加到alives列表
    if subprocess.call(["ping", "-c", "1", ip]) == 0:
        print(" {0} is alive.".format(ip))
        alives.append(ip)
    # 如果ping失败，打印不活跃信息
    else:
        print(" {0} is not.".format(ip))

# 定义一个函数，用于从队列中获取IP地址，并调用ping函数
def is_reacheable(q):
    try:
        # 循环获取IP地址，直到队列为空
        while True:
            ip = q.get_nowait()
            call_ping(ip)
    # 如果队列为空，抛出异常
    except Empty:
        pass

# 定义一个主函数，用于创建线程和队列
def main():
    # 定义一个空列表，用于存储线程
    threads = []
    # 定义一个队列，用于存储IP地址
    q = Queue()
    # 循环生成一组IP地址，并放入队列中
    for i in range(100, 200):
        ip = "192.168.154." + str(i)
        q.put(ip)
    # 循环创建10个线程，并启动它们
    for i in range(10):
        # 创建一个线程，指定目标函数和参数
        t = threading.Thread(target=is_reacheable, args=(q,))
        # 启动线程
        t.start()
        # 将线程添加到列表中
        threads.append(t)
    # 循环等待所有线程结束
    for t in threads:
        t.join()
    # 打印活跃主机的数量和列表
    print("There are {0} alive hosts.".format(len(alives)))
    print(alives)

# 调用主函数
if __name__ == "__main__":
    main()
