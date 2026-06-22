import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
lista_arquivos = os.listdir(caminho)

locais = {
    "Imagens":     [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documentos":  [".pdf", ".docx", ".doc", ".txt", ".md", ".pptx"],
    "Planilhas":   [".xlsx", ".xls", ".csv"],
    "Compactados": [".zip", ".rar", ".tar", ".gz", ".7z", ".jar", ".deb"],
    "Videos":      [".mp4", ".mov", ".avi", ".mkv"],
    "Audio":       [".mp3", ".wav", ".flac"],
    "Scripts":     [".sh"],
    "Codigo":      [".js", ".jsx"],
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    extensao = extensao.lower()
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")