print('~='*30)
print('ANALISADOR DE DIABETES'.center(40))
print('~='*30)

#entrada do usuario
glicose = float(input('Digite o seu nível de glicose (mg/dL):'))

#classifiçao do usuario
if glicose < 100:
    print('\033[34mGlicose normal.\033[m')
    status = 'normal'
elif glicose <= 125:
    print('\033[33mAtenção! Pré-diabético.\033[m')
    status = 'pre'
else:
    print('\033[31mProcure um médico! Diabético.\033[m')
    status = 'diabetes'

#lista de alimentos

alimentos = [("Refrigerante", 65),
             ("Maçã", 30),
             ("Chocolate", 60),
             ("Leite", 35),
             ("Biscoito recheado", 55),
             ("Bolo", 45),
             ("Arroz", 30),
             ("Feijão", 25),
             ("Sorvete", 60),
             ("Pudim", 55),
             ("Banana", 20),
             ("Alface", 5),
             ("Tomate", 10),
             ("Ovo", 5),
             ("Frango", 15),
             ("Cenoura", 12),
             ("Beterraba", 30),
             ("Inhame", 15),
             ("Pizza", 40)]

print("\nANÁLISE DE ALIMENTOS: ")

#iteração para analisar os alimentos da lista conforme o teor de glicose do usuário

for nome, açucar in alimentos:
    if status == "diabetes":
        if açucar > 20:
            print(f'{nome} - ({açucar}%) -> NÃO RECOMENDADO ❌')
        else:
            print(f'{nome} - ({açucar}%) -> Pode consumir ✔️')
    elif status == "pre":
        if açucar > 35:
            print(f'{nome} - ({açucar}%) -> EVITAR ❌')
        else:
            print(f'{nome} - ({açucar}%) -> Uso moderado ⚠️')
    else:
        print(f'{nome} - ({açucar}%) -> Pode consumir ✔️')
print("Programa encerrado. Não deixe de cuidar da sua saúde! 😃")

    
