import time

rodando = True

while rodando:
    print('\nOlá! Sou uma calculadora especializada em cafeina! ⚡⚡')
    time.sleep(1.5)
    nome = input('Primeiro, me diz seu nome!  ')
    time.sleep(1.5)
    print(f'Muito prazer, {nome}!')
    time.sleep(1.5)

    print('O que você gostaria de calcula hoje?')
    time.sleep(1.5)
    print('\033[33m[1] Apenas Café ☕\033[0m')
    time.sleep(1)
    
    print('\033[92m[2] Apenas Monster ⚡\033[0m')
    time.sleep(1)
    
    print('\033[34m[3] Apenas Redbull ⚡\033[0m')
    time.sleep(1)
    
    print('\033[36m[4] Calcular tudo! (Café, Monster e Redbull)\033[0m')
    time.sleep(1)

    limite_seguro = 400
    total_cafeina = 0

    while True:
        opcao = input('Digite a opção desejada: ').strip()
        if opcao in ['1', '2', '3', '4']:
            break
        print('\033[91m⚠️ Opção inválida! Digite apenas um número de 1 a 4.\033[0m')
    
    time.sleep(1)

    if opcao == '1':
        while True:
            try:
                cafe = int(input(f'{nome}, quantas xícaras de café você já tomou hoje? ☕ '))
                if cafe < 0:
                    print('\033[91m⚠️ Digite um número positivo!\033[0m')
                    continue
                break
            except ValueError:
                print('\033[91m⚠️ Ops! Digite apenas números inteiros válidos.\033[0m')
        total_cafeina = cafe * 80

    elif opcao == '2':
        while True:
            try:
                monster = int(input(f'{nome}, quantas latas de Monster você tomou hoje? '))
                if monster < 0:
                    print('\033[91m⚠️ Digite um número positivo!\033[0m')
                    continue
                break
            except ValueError:
                print('\033[91m⚠️ Ops! Digite apenas números inteiros válidos.\033[0m')
        total_cafeina = monster * 150

    elif opcao == '3':
        while True:
            try:
                redbull = int(input(f'{nome}, quantas latas de Redbull você já tomou hoje? '))
                if redbull < 0:
                    print('\033[91m⚠️ Digite um número positivo!\033[0m')
                    continue
                break
            except ValueError:
                print('\033[91m⚠️ Ops! Digite apenas números inteiros válidos.\033[0m')
        total_cafeina = redbull * 80

    elif opcao == '4':
        while True:
            try:
                cafe = int(input('Quantas xícaras de café já tomou hoje? '))
                monster = int(input('E quantas latas de monster? '))
                redbull = int(input('E latas de redbull? '))
                if cafe < 0 or monster < 0 or redbull < 0:
                    print('\033[91m⚠️ Digite apenas números positivos em todas as opções!\033[0m')
                    continue
                break
            except ValueError:
                print('\033[91m⚠️ Ops! Digite apenas números inteiros válidos.\033[0m')
        total_cafeina = (cafe * 80) + (monster * 150) + (redbull * 80)

    if total_cafeina > 0:
        while True:
            try:
                hora_ultima_dose = int(input(f'\n{nome}, a que horas (em formato de 0 a 23h) você consumiu sua última bebida?: '))
                if 0 <= hora_ultima_dose <= 23:
                    break
                print('\033[91m⚠️ Horário inválido! Digite um valor entre 0 e 23.\033[0m')
            except ValueError:
                print('\033[91m⚠️ Ops! Digite apenas números inteiros para a hora.\033[0m')

        horas_para_limpar = 0
        cafeina_restante = total_cafeina

        print('\nCalculando a carga de cafeína no seu sistema...')
        time.sleep(2)
        print(f'\n\033[43m\033[30m⚡ {nome}, você consumiu um total de {total_cafeina}mg de cafeína. ⚡\033[0m')
        time.sleep(1)

        if total_cafeina >= limite_seguro:
            print(f'\n\033[91m🚨 ALERTA VERMELHO, {nome}! Você passou dos {limite_seguro}mg!\033[0m')
            time.sleep(1)
            print('\033[91m☕ Seu coração está batendo mais rápido que processador overclockado.\033[0m')
            time.sleep(1)
            print('\033[91m⚠️ Beba uma água e vá dar uma caminhada, você extrapolou o limite hoje!\033[0m')
            
            time.sleep(2)
            print(f'\n\033[93m--- GUIA DE EMERGÊNCIA PARA O(A) {nome.upper()} --- \033[0m')
            time.sleep(1)
            print('💧 1. Beba bastante água agora mesmo para ajudar a filtrar o organismo.')
            time.sleep(1)
            print('🧘 2. Respire fundo e tente relaxar (evite ambientes estressantes).')
            time.sleep(1)
            print('🚶 3. Faça uma caminhada leve se conseguir, para gastar o excesso de energia.')
            time.sleep(1)
            print('🛑 4. Zero cafeína pelo resto do dia, combinado?')
            
        elif total_cafeina >= 300:
            print(f'\n\033[93m⚠️ Atenção, {nome}! Você está bem perto do seu limite diário. Pegue leve!\033[0m')
        else:
            print(f'\n\033[92m✅ Tranquilo, {nome}! Seu consumo está dentro de um nível seguro.\033[0m')
            
        while cafeina_restante > 50:
            cafeina_restante = cafeina_restante / 2
            horas_para_limpar += 6

        hora_estimada = (hora_ultima_dose + horas_para_limpar) % 24

        print(f'\n⏳ Estimativa de sono: Com base no seu consumo, a cafeína deve cair para níveis seguros (abaixo de 50mg) por volta das {hora_estimada}:00h.')
    print('\n' + '='*40)
    continuar = input('Deseja fazer outro cálculo? (s/n): ').strip().lower()
    if continuar != 's':
        print(f'\nObrigado por usar a calculadora de cafeína, {nome}! Até mais! ⚡')
        rodando = False