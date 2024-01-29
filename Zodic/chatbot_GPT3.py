# 导入requests库
import requests

# 定义gpt-3.5-turbo API的密钥，替换为你自己的
API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# 定义gpt-3.5-turbo API的请求头，包含密钥和内容类型
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# 定义gpt-3.5-turbo API的请求参数，包括模型、输入、输出长度等
params = {
    "model": "gpt-3.5-turbo-16k", # 使用最大的模型
    "query": "", # 输入为空，等待用户输入
    "max_tokens": 100, # 输出最多100个单词
    "temperature": 0.9, # 使用较高的温度，增加多样性
    "stop": "\n" # 使用换行符作为输出的终止符
}

# 定义一个函数，用于发送请求给gpt-3.5-turbo API，并处理返回的结果
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

# 定义一个函数，用于获取用户的输入，并调用上面的函数，以及打印模型的输出
def chat():
    # 打印欢迎信息
    print("欢迎使用gpt-3.5-turbo聊天机器人，你可以和它聊天，或者让它做一些有趣的事情，比如写诗、编程、讲笑话等。")
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
        # 调用上面的函数，获取模型的输出
        response = query_gpt(query)
        # 打印模型的输出，去掉首尾的空格
        print("机器人: " + response.strip())

# 调用上面的函数，开始聊天
chat()
