import re
with open("from.txt", 'r+', encoding='utf-8') as from_input:
    from_input.write("Hello Mr.张，welcome you to 南京。")
    with open("from.txt", encoding='utf-8') as from_input_next:
        from_output = from_input_next.read()
        pattern = re.compile(r"[A-z]+")
        print(from_input)
        from_output = pattern.findall(from_output)
        print(from_output)
        from_output = '\n'.join(from_output)
        with open("to.txt", 'w', encoding='utf-8') as to_input:
            to_input.write(from_output)