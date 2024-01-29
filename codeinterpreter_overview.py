# 导入模块
import requests
import json
import subprocess

# 定义GPT-3.5或GPT-4的API密钥，替换为你自己的
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 定义GPT-3.5或GPT-4的API请求头，包含密钥和内容类型
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 定义GPT-3.5或GPT-4的API请求参数，包括模型、输入、输出长度等
params = {
    "model": "gpt-3.5-turbo-16k", # 使用最大的模型
    "query": "", # 输入为空，等待用户输入
    "max_tokens": 100, # 输出最多100个单词
    "temperature": 0.9, # 使用较高的温度，增加多样性
    "stop": "\n" # 使用换行符作为输出的终止符
}

# 定义一个函数，用于发送请求给GPT-3.5或GPT-4的API，并处理返回的结果
def query_gpt(query):
    # 将用户输入作为请求参数的一部分
    params["query"] = query
    # 发送POST请求，获取响应
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=params)
    # 检查响应状态，如果正常，则返回结果中的文本部分
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    # 如果出错，则返回错误信息
    else:
        return response.text

# 定义一个函数，用于在Linux沙盒环境中运行python代码，并返回输出或错误
def run_code(code):
    # 使用subprocess模块创建一个子进程，执行python命令，并将代码作为标准输入
    process = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # 将代码编码为字节，并发送给子进程
    process.stdin.write(code.encode())
    # 关闭子进程的标准输入
    process.stdin.close()
    # 从子进程的标准输出和标准错误中读取字节，并解码为文本
    output = process.stdout.read().decode()
    error = process.stderr.read().decode()
    # 如果有错误，返回错误信息
    if error:
        return error
    # 如果没有错误，返回输出信息
    else:
        return output

# 定义一个函数，用于获取用户的输入，并调用上面的函数，以及打印模型的输出
def chat():
    # 打印欢迎信息
    print("欢迎使用code interpreter，你可以用自然语言描述你想要的python代码，我会为你生成并执行代码，返回结果。")
    print("如果你想退出，可以输入quit或exit。")
    # 循环获取用户的输入
    while True:
        # 获取用户的输入，去掉首尾的空格
        query = input("你: ").strip()
        # 如果输入为空，跳过本次循环
        if not query:
            continue
        # 如果输入为quit或exit，退出循环
        if query.lower() in ["quit", "exit"]:
            break
        # 调用上面的函数，获取模型生成的python代码
        code = query_gpt(query)
        # 打印模型生成的python代码
        print("模型生成的python代码: \n" + code)
        # 调用上面的函数，运行python代码，并获取输出或错误
        result = run_code(code)
        # 打印运行结果或错误信息
        print("运行结果或错误信息: \n" + result)

# 调用上面的函数，开始聊天
chat()
