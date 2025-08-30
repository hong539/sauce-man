import re
from .handle_pixiv_regex import handle_pixiv_regex
from .handle_twitter_regex import handle_twitter_regex
from .handle_instagram_regex import handle_instagram_regex

# 正則表達式對應表
regexs_dict = {
    re.compile(r"https://www.pixiv.net/artworks/(\d+)"): handle_pixiv_regex,
    re.compile(r"https://twitter.com/[A-Za-z0-9_]{1,15}/status/(\d+)"): handle_twitter_regex,
    re.compile(r"https://x\.com/[A-Za-z0-9_]{1,15}/status/([0-9]+)"): handle_twitter_regex,
    re.compile(r"(https://www\.instagram\.com/(?:p|reel|tv)/[A-Za-z0-9_-]+/?)"): handle_instagram_regex
}