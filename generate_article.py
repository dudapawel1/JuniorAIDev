import openai

openai.api_key = '********************************'


def get_text_from_article():
    with open("article.txt", "r", encoding="utf-8") as file:
        content = file.read()
    return content


def generate_html_from_text(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate HTML from the following article text:\n\n{text}\n\nInclude image tags as '<img src=\"image_placeholder.jpg\">' and use headers.",
        max_tokens=1500,
        temperature=0.5
    )
    return response.choices[0].text.strip()


def save_html(content):
    with open("article.html", "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    article_text = get_text_from_article()
    generated_html = generate_html_from_text(article_text)
    save_html(generated_html)
    print("HTML has been saved in article.html")
