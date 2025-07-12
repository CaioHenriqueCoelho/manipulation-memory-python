# 🕹️ Trainer para Assault Cube (Python + Cheat Engine)

Este projeto é um **Trainer simples em Python** que utiliza a biblioteca `pymem` para manipular a memória do jogo **Assault Cube**, permitindo **reposicionar automaticamente a vida e as balas** do jogador, com interface gráfica usando `tkinter`.

---

## ✅ Funcionalidades

- [x] Interface gráfica com botões para ligar/desligar cada função
- [x] Reposição automática de balas quando estiverem abaixo de um limite
- [x] Reposição automática de vida quando estiver abaixo de um limite
- [x] Monitoramento contínuo usando multithread

---

## 📦 Requisitos

- Python 3.8+
- Bibliotecas:
  - `pymem`
  - `tkinter` (já vem com Python)

Instalação do pymem:

```bash
pip install pymem

```

🛠️ Como usar
Abra o Assault Cube (ac_client.exe)

Execute o script Python:

bash
Copiar
Editar
python trainer.py

Use os botões da interface para ativar/desativar a reposição de balas e vida

🔍 Como foram encontrados os endereços?
Os endereços de memória para vida e balas foram obtidos com o Cheat Engine, utilizando varreduras de valores com tipo 4 Bytes:

0x006C3130 → Endereço das balas

0x006C30DC → Endereço da vida

⚠️ Aviso Legal

⚠️ Este projeto tem fins exclusivamente educacionais e é destinado ao estudo de manipulação de memória com Python e Cheat Engine em ambiente controlado (offline).

Não deve ser usado para trapacear em jogos online, competir de forma desleal ou violar os termos de uso de softwares.

A modificação de softwares de terceiros sem permissão pode violar leis de direitos autorais ou ser interpretada como crime dependendo da jurisdição.

O autor não se responsabiliza por usos indevidos do código.

📚 Aprendizado
Este projeto ensina:

Como usar pymem para interagir com a memória de processos.

Como encontrar e monitorar valores com Cheat Engine.

Como criar uma interface com tkinter.

Princípios básicos de engenharia reversa para jogos educacionais.

👨‍💻 Autor
Desenvolvido por Caio Henrique Coelho — para fins de estudo e aprendizado.
