nome_livro = str (input("Qual é o nome do livro que você quer registrar? "))
autor = str (input("Foi escrito por quem? "))
ano_publi = int (input("Foi publicado em que ano? "))
pags = int (input("Tem quantas páginas? "))

print ("O livro {}, escrito por {}, foi publicado em {} e tem {} páginas." .format(nome_livro, autor, ano_publi, pags))