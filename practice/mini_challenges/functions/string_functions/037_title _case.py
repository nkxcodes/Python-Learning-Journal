# Return title case.

def to_title_case(text):
    splited_text = text.split()
    for index in range(0, len(splited_text)):
        first_ch = splited_text[index][0].upper()
        remaining_chs = splited_text[index][1:].lower()
        splited_text[index] = first_ch + remaining_chs
    text = ' '.join(splited_text)
    return text

result = to_title_case('programming is awesome')

print(result)