# просто вызовите функцию) располагаются по порядку, как идут задания
import re
import matplotlib.pyplot as plt


def write_ftps():
    text = ''
    pattern = r'\bftp\.[^\s,;]+'

    with open('references') as inf, open('ftps', 'w') as ouf:
        text = inf.read()
        content = '\n'.join(re.findall(pattern, text))
        ouf.write(content)


def digits_match():
    text = ''
    pattern = r'\d+'

    with open('2430AD') as inf:
        text = inf.read()

    content = '\n'.join(re.findall(pattern, text))
    return content


def words_a_match():
    text = ''
    pattern = r'\b\w*[Aa]+\w*\b'

    with open('2430AD') as inf:
        text = inf.read()

    content = '\n'.join(re.findall(pattern, text))
    return content


def exclamation_point():
    text = ''
    pattern = r'[A-Z0-9][\w ,;:]+!'

    with open('2430AD') as inf:
        text = inf.read()

    content = '\n'.join(re.findall(pattern, text))
    return content


def word_length_distribution():
    text = ''
    # если есть апостроф, то считаем как одно слово
    pattern = r'\b[A-z\']+\b'

    with open('2430AD') as inf:
        text = inf.read()

    content = list(sorted(map(len, set(map(str.lower, re.findall(pattern, text))))))

    plt.hist(content, density=True)
    plt.title('Unique words length distribution')
    plt.xlabel('Word length')
    plt.ylabel('Word ratio')
    plt.style.use('classic')
    plt.show()
