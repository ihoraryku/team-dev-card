#!/usr/bin/env python3
"""
Генератор веб-сайту команди з Markdown-профілів
"""

import glob
import os
from markdown2 import markdown
from datetime import datetime

# Конфігурація
TEMPLATE = """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Наша Команда</title>
    <link rel="stylesheet" href="styles/main.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <header>
        <h1><i class="fas fa-users"></i> Наша Команда</h1>
        <p>Останнє оновлення: {update_time}</p>
    </header>
    
    <main class="team-container">
        {profiles}
    </main>
    
    <footer>
        <p>© {year} Всі права захищені</p>
    </footer>
</body>
</html>
"""

def generate_profile_cards():
    """Генерує HTML-картки з профілів команди"""
    profiles_html = ""
    
    for file_path in sorted(glob.glob("team/*.md")):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                md_content = f.read()
                
            # Конвертація Markdown → HTML
            html_content = markdown(
                md_content,
                extras=["fenced-code-blocks", "tables"]
            )
            
            # Додаємо картку профілю
            profiles_html += f"""
            <div class="profile-card">
                {html_content}
            </div>
            """
            
        except Exception as e:
            print(f"Помилка при обробці {file_path}: {str(e)}")
    
    return profiles_html

def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_year = datetime.now().year
    
    # Генеруємо контент
    profiles = generate_profile_cards()
    
    # Заповнюємо шаблон
    final_html = TEMPLATE.format(
        profiles=profiles,
        update_time=current_time,
        year=current_year
    )
    
    # Зберігаємо результат
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    
    print(f"Сайт успішно згенеровано о {current_time}")

if __name__ == "__main__":
    main()
