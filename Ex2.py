num_list = []

while True:

    num = int(input(f"Digite um número: "))
    if num not in num_list:
        num_list.append(num)
    else:
        print(f"Esse número ja foi inserido, digite outro.")
    continuar = input(f"Deseja continuar?Digite S ou N ").lower()
    if continuar != 's':
        num_list.sort()
        print("Os números inseridos foram: ", num_list)
        break
