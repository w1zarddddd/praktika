import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

# Инициализируем лемматизатор
lemmatizer = WordNetLemmatizer()

def lemmatize_word(word):
    # Применяем лемматизацию к слову
    return lemmatizer.lemmatize(word.lower())

def check_ifile(ifile):
    if not ifile:
        print("Bad ifile!")
        exit(1)

def from_istream_set_words(istr, words_set):
    for line in istr:
        words = word_tokenize(line)
        for word in words:
            # Лемматизация только при добавлении в множество
            normalized_word = lemmatize_word(word)
            words_set.add(normalized_word)

def line_has_words(b_line, words_set):
    words = word_tokenize(b_line)
    for word in words:
        # Лемматизация только при проверке
        normalized_word = lemmatize_word(word)
        if normalized_word in words_set:
            return True
    return False

def generate_lines_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

def write_lines_to_file(filename, lines):
    with open(filename, 'a', encoding='utf-8') as file:
        for line in lines:
            file.write(line)

def main():
    FILE_BELIBERDA_NAME = "тест56.txt"
    FILE_WORDS_NAME = "dictionary.txt"
    FILE_JAL_PRIZN_NAME = "Жал-призн.txt"
    FILE_JAL_KAND_NAME = "Жал-канд.txt"

    try:
        words_set = set()

        with open(FILE_WORDS_NAME, 'r', encoding='utf-8') as w_ifile:
            from_istream_set_words(w_ifile, words_set)

        jal_prizn_lines = []
        jal_kand_lines = []

        for b_line in generate_lines_from_file(FILE_BELIBERDA_NAME):
            if line_has_words(b_line, words_set):
                jal_prizn_lines.append(b_line)
            else:
                jal_kand_lines.append(b_line)

        write_lines_to_file(FILE_JAL_PRIZN_NAME, jal_prizn_lines)
        write_lines_to_file(FILE_JAL_KAND_NAME, jal_kand_lines)
    except IOError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()