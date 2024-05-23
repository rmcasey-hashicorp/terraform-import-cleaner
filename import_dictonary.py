def resource_dictionary(path="", resource="vpc") -> dict:
    import markdown
    from bs4 import BeautifulSoup

    index = 0
    patterns = {}

    with open(path+"/terraform-provider-aws/website/docs/r/"+resource+".html.markdown", "r",
              encoding="utf-8") as f:
        text = f.read()

    md_to_html = BeautifulSoup(markdown.markdown(text), 'html.parser')
    html_to_text = [text for text in md_to_html.ul.stripped_strings]

    for line in html_to_text:
        if 'Defaults to' in line:
            patterns[html_to_text[index - 1]] = line.split('Defaults to')[1].rstrip('.')
        elif 'Default' in line:
            patterns[html_to_text[index - 1]] = line.split('Default')[1].rstrip('.')
        index = index + 1

    return patterns


def main() -> None:
    test = resource_dictionary(path="/Users/ryancasey/projects")

    for key, value in test.items():
        print(key, value)


if __name__ == "__main__":
    main()
