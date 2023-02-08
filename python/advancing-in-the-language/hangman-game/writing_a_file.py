#Vale lembrar que o w sobrescreve o arquivo, se o mesmo existir. Se só quisermos adicionar conteúdo ao arquivo, utilizamos o a.

word_file = open("words.txt", "w")
word_file.write("banana")

word_file2 = open("words.txt", "a")
word_file.write("\nmorango\n")
word_file.write("melancia\n")

word_file.close()

# file reading:
text_file = open("words.txt", "r")
print(text_file.read()) # ler o arquivo inteiro
text_file.close()

text_file = open("words.txt", "r")
# ler linha por linha
for line in text_file:
    print(line.strip()) # remove uma linha a mais criada entre cada palavra
text_file.close()

text_file2 = open("words.txt", "r")
line = text_file2.readline()
