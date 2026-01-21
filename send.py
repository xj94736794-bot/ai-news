import requests
from datetime import datetime

# 👇👇👇 把下面引号里的内容换成您的 Server酱 SendKey
SCKEY = "SCT310629TSfn9HMNRv3R8yfcCUkxHTz7a" 

def main():
    print("正在获取新闻...")
    try:
        # 获取 GitHub 上最新的 AI 热点
        api = "https://api.github.com/search/repositories?q=topic:artificial-intelligence+OR+topic:gpt&sort=updated&order=desc"
        resp = requests.get(api).json()
        
        # 整理新闻内容
        content = f"📅 {datetime.now().strftime('%Y-%m-%d')} AI日报\n\n"
        content += "🔥 **全球最新AI热点 (GitHub实时):**\n\n"
        
        for i, item in enumerate(resp['items'][:10], 1): 
            desc = item['description']
            if desc: 
                # 简单翻译成中文提示 (模拟)
                desc = desc[:60] + "..." if len(desc) > 60 else desc
            else: 
                desc = "暂无描述"
            content += f"{i}. **{item['name']}**\n   {desc}\n\n"
            
    except Exception as e:
        content = f"获取失败: {str(e)}"

    # 发送到微信
    data = {"title": "今日AI快报", "desp": content}
    requests.post(f"https://sctapi.ftqq.com/{SCKEY}.send", data=data)
    print("发送完成！")

if __name__ == "__main__":
    main()
