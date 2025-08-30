# handle_instagram_regex.py
import re
from urllib.parse import urlparse, urlunparse, parse_qsl, urlencode

import aiohttp  # 之後若需要檢查連結可用，目前不強制使用
import discord


# 可重用：把 instagram 網域換成 kkinstagram，並清掉追蹤參數
def _rewrite_instagram_url(url: str) -> str:
    """
    Examples:
    https://www.instagram.com/reel/DNxkpU6Xqu1/?utm_source=ig_web_copy_link&igsh=abc
      -> https://www.kkinstagram.com/reel/DNxkpU6Xqu1/
    """
    parsed = urlparse(url)

    # 僅處理 instagram 連結
    host = parsed.netloc.lower()
    if "instagram.com" not in host:
        return url

    # 統一換成 www.kkinstagram.com
    new_host = "www.kkinstagram.com"

    # 過濾雜訊參數
    junk_keys = {
        "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
        "igsh", "igshid", "ig_mid", "ig_rid", "fbclid"
    }
    kept_q = [(k, v) for k, v in parse_qsl(parsed.query, keep_blank_values=True) if k not in junk_keys]
    new_query = urlencode(kept_q, doseq=True)

    rebuilt = parsed._replace(netloc=new_host, query=new_query)
    return urlunparse(rebuilt)


async def handle_instagram_regex(match: re.Match, message: discord.Message):
    """
    對單一 regex match 進行改寫並回覆預覽。
    預期由外部的訊息處理器對 message.content 跑 regex，對每個 match 呼叫本函式。
    """
    try:
        # 盡量穩健地從 match 取得原始 URL
        original_url = None
        if match is not None:
            # 優先取第一個群組；若沒有群組就用整個 match
            if match.lastindex and match.lastindex >= 1:
                original_url = match.group(1)
            else:
                original_url = match.group(0)

        if not original_url:
            return  # 沒東西就不做

        rewritten = _rewrite_instagram_url(original_url)

        # 如果真的改寫成功，回覆新連結讓 Discord 自己產生 embed 預覽
        if rewritten and rewritten != original_url:
            await message.reply(
                rewritten,
                mention_author=False,
                suppress_embeds=False,
                allowed_mentions=discord.AllowedMentions.none(),
            )
        else:
            # 不是 Instagram 連結或無需改寫就略過
            return

    except Exception as e:
        # 失敗時避免噴堆疊；你也可以改成 logger.error
        try:
            await message.reply(
                f"無法處理此 Instagram 連結：{e}",
                mention_author=False,
                allowed_mentions=discord.AllowedMentions.none(),
            )
        except Exception:
            pass
