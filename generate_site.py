import os
import markdown
import re

def parse_markdown(content):
    """Парсить ім'я, навички та посилання із Markdown-контенту."""
    lines = content.split("\n")
    name = lines[0].replace("# ", "") if lines[0].startswith("# ") else "Без імені"
    skills = ""
    links = ""
    
    for line in lines[1:]:
        if line.startswith("**Навички:**"):
            skills = line.replace("**Навички:**", "").strip()
        elif line.startswith("**Посилання:**"):
            links = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', line.replace("**Посилання:**", "").strip())
    
    return f"""
    <div class='member'>
        <h2>{name}</h2>
        <p><strong>Навички:</strong> {skills}</p>
        <p><strong>Посилання:</strong> {links}</p>
    </div>
    """

def read_markdown_files(directory):
    """Зчитує всі .md файли та повертає їх у вигляді відформатованого HTML."""
    team_members = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()
                member_html = parse_markdown(content)
                team_members.append(member_html)
    return team_members

def generate_index_html(team_members):
    """Генерує index.html зі списком команди."""
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Our Team</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .member { border-bottom: 1px solid #ccc; padding: 20px; }
            h2 { color: #2c3e50; }
        </style>
    </head>
    <body>
        <h1>Meet Our Team</h1>
        {content}
    </body>
    </html>
    """
    members_html = "\n".join(team_members)
    return template.replace("{content}", members_html)

def save_index_html(content, output_file="index.html"):
    """Зберігає HTML-контент у файл."""
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    directory = "team"
    if not os.path.exists(directory):
        print(f"Директорія '{directory}' не знайдена.")
        return
    
    team_members = read_markdown_files(directory)
    html_content = generate_index_html(team_members)
    save_index_html(html_content)
    print("Файл index.html успішно створено!")

if __name__ == "__main__":
    main()