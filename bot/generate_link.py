def generate_link(original_url: str, bot_username: str) -> str:
    encoded = original_url.replace('/', '-').replace('.', '_')
    return f"https://t.me/{bot_username}?start={encoded}"

if __name__ == '__main__':
    print(generate_link("https://paricy.com/free-anime", "Animanvers_bot"))
  
