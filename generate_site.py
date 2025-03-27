import glob
from markdown2 import markdown

# 1) Зчитуємо всі .md файли з папки team/
profiles_html = ""
for file_path in glob.glob("team/*.md"):
    with open(file_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()
        # 2) Конвертуємо Markdown у HTML
        profiles_html += markdown(markdown_content)

# 3) Генеруємо повноцінний HTML-документ
final_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Team Dev Card</title>
    <link rel="stylesheet" href="styles/main.css">
</head>
<body>
    <h1>Our Awesome Team</h1>
    <div class="profiles">
        {profiles_html}
    </div>
</body>
</html>
"""

# Записуємо результат у index.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(final_html)

print("Site generated successfully!")