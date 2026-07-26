# ☕ Calculadora Avançada de Cafeína (Terminal)

Uma calculadora de cafeína interativa desenvolvida em Python, projetada para rodar no terminal com uma experiência de usuário (UX) imersiva, utilizando pausas de tempo, cores personalizadas via códigos ANSI, estimativa de meia-vida no organismo, guia de emergência para excesso de estimulantes e **blindagem completa contra erros de digitação**.

---

## 🚀 Funcionalidades

* **Menu Interativo Colorido:** Opções estilizadas com cores exclusivas para cada tipo de bebida (Café, Monster e Red Bull).
* **Robustez e Blindagem (Try/Except):** O programa não fecha por falhas de digitação; ele valida entradas inválidas (letras, números negativos ou horários incorretos) e solicita a informação novamente de forma amigável.
* **Cálculo de Carga Total:** Converte diferentes tipos de bebidas em miligramas (mg) de cafeína consumidas no dia.
* **Sistema de Alertas Inteligentes:** 
  * 🟢 **Seguro:** Mensagem de tranquilidade para consumos moderados.
  * 🟡 **Atenção:** Avisos de proximidade do limite diário (400mg).
  * 🔴 **Alerta Vermelho:** Alerta crítico com efeitos visuais e tom humorístico caso o limite seja ultrapassado.
* **Guia de Emergência:** Recomendações práticas e primeiros socorros (hidratação, respiração e caminhada) caso o usuário ultrapasse o limite seguro.
* **Estimativa de Meia-Vida do Sono:** Calcula, com base no horário da última dose, em quanto tempo os níveis de cafeína no corpo cairão para níveis seguros (abaixo de 50mg) para não atrapalhar o sono.
* **Loop de Reinício:** Permite realizar novos cálculos quantas vezes quiser sem precisar fechar e reabrir o programa.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x** (Linguagem principal)
* **Biblioteca `time`** (Nativa do Python, utilizada para controlar o fluxo de tempo e simular pausas)
* **Códigos ANSI Escape Sequences** (Utilizados para estilizar textos, cores e efeitos de marca-texto diretamente no terminal)
* **Tratamento de Exceções (`try/except`)** (Garante a estabilidade e resiliência da aplicação)

---

## 📦 Como Executar o Projeto

1. Certifique-se de ter o **Python** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo do código-fonte (`calculadora_cafeina.py`).
3. Abra o seu terminal (CMD, PowerShell, Bash ou Terminal do VS Code).
4. Navegue até a pasta onde o arquivo está salvo.
5. Execute o comando:

```bash
python calculadora_cafeina.py