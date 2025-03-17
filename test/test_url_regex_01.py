import re

# 定義 Twitter 連結的正則表達式
twitter_regex = re.compile(r"https://x\.com/[A-Za-z0-9_]{1,15}/status/([0-9]+)")

# 測試字串
test_url = "https://x.com/hino_kagutsuki/status/1901211852282962130"

# 匹配 Twitter 連結並執行對應的處理函式
match = twitter_regex.search(test_url)

if match:
    tweet_id = match.group(1)
    print(f"匹配成功，推文 ID: {tweet_id}")
else:
    print("匹配失敗")