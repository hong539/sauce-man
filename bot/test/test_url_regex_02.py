from bot.url_regex import regexs_dict

urls = [
    "https://www.instagram.com/p/DN2-iOmZk5Q/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==",
    "https://www.instagram.com/p/DNyEUl55h_l/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==",
    "https://www.instagram.com/reel/DNf9df2T9Sa/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==",
    "https://www.instagram.com/reel/DMfegfUz9Qo/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==",
]

for url in urls:
    for regex, handler in regexs_dict.items():
        match = regex.match(url)
        if match:
            print(f"{url} -> matched by {handler.__name__}, shortcode={match.group(1)}")
