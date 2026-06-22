# 🐍 Automação em Python — Miniprojetos

> Uma coleção de pequenos projetos de automação em Python, feitos pra resolver dores reais do dia a dia.
> Cada projeto resolve um problema chato que eu não queria mais fazer na mão.

A filosofia aqui é simples: **por que fazer manualmente em 5 minutos o que dá pra automatizar em 3 horas?** 😄

---

## 📂 Projetos

| # | Projeto | Descrição | Stack | Artigo |
|---|---------|-----------|-------|--------|
| 01 | [Organizador de Arquivos](#01--organizador-de-arquivos) | Organiza uma pasta separando os arquivos por tipo | `os`, `tkinter` | [📖 Ler](https://medium.com/@nunomendesx40/i-was-drowning-in-my-downloads-folder-so-i-taught-python-to-clean-it-up-for-me-aca95fe249c1) |
| 02 | *Em breve...* | — | — | — |
| 03 | *Em breve...* | — | — | — |

---

## 01 — 📁 Organizador de Arquivos

Cansou da pasta de Downloads parecendo um campo de batalha? Este script resolve.

Ele abre uma **janela gráfica** pra você escolher uma pasta e então organiza tudo automaticamente, criando subpastas por tipo de arquivo e movendo cada coisa pro seu lugar.

### O que ele faz

```
PastaEscolhida/
├── Imagens/      → .jpg, .png, .gif, .webp, .svg...
├── Documentos/   → .pdf, .docx, .txt, .md, .pptx...
├── Planilhas/    → .xlsx, .xls, .csv
├── Compactados/  → .zip, .rar, .tar, .deb...
├── Videos/       → .mp4, .mov, .mkv...
├── Audio/        → .mp3, .wav, .flac
├── Scripts/      → .sh
└── Codigo/       → .js, .jsx
```

### Como usar

```bash
# Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPO.git
cd SEU_REPO

# Rode o organizador
python3 organizador.py
```

Uma janela vai abrir pedindo pra você selecionar a pasta. Escolha e pronto — em segundos ela estará organizada. ✨

### Tecnologias

- **Python 3**
- **`os`** — navegação no sistema de arquivos, criação de pastas e movimentação
- **`tkinter`** — janela gráfica pra seleção da pasta (já vem com o Python!)

> 📖 **Quer entender como foi feito?** Escrevi um artigo passo a passo (com os perrengues no caminho): **[Eu Estava Afogando na Pasta de Downloads, Então Ensinei o Python a Limpá-la Por Mim](https://medium.com/@nunomendesx40/i-was-drowning-in-my-downloads-folder-so-i-taught-python-to-clean-it-up-for-me-aca95fe249c1)**

---

## 🚀 Próximos projetos

Esta é uma série em construção. No roadmap:

- [ ] Renomeador de arquivos em lote
- [ ] Conversor de imagens em massa (Pillow)
- [ ] Watcher de pasta em tempo real (watchdog)
- [ ] *...e mais por aí*

---

## 🤝 Contribuições

Sugestões, ideias de projetos e melhorias são bem-vindas! Abra uma issue ou mande um PR.

## 📫 Contato

- LinkedIn: [Nuno Mendes](https://www.linkedin.com/in/nuno-mendes-07a259253/)
- Medium: [Nuno Mendes](https://medium.com/@nunomendesx40)

---

⭐ Se algum projeto te foi útil, deixa uma estrela no repo!