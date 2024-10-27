import tkinter as tk
from tkinter import messagebox, ttk
import yt_dlp
import pathlib

def progress_hook(d):
    """Função de callback para mostrar o progresso do download."""
    if d['status'] == 'downloading':
        # Atualiza a barra de progresso com o percentual
        percent = d['downloaded_bytes'] / d['total_bytes'] * 100
        progress_var.set(percent)  # Atualiza a variável da barra de progresso
        progress_bar.update()  # Atualiza a barra de progresso

def download_video():
    """Função para baixar o vídeo da URL fornecida."""
    url = url_entry.get()  # Obtém a URL do campo de entrada
    if not url:
        messagebox.showerror("Erro", "Por favor, insira um link.")
        return

    try:
        download_path = pathlib.Path.home() / "Desktop"  # Define o caminho para a área de trabalho
        ydl_opts = {
            'format': 'best',  # Melhor qualidade disponível
            'outtmpl': str(download_path / '%(title)s.%(ext)s'),  # Nome do arquivo na área de trabalho
            'progress_hooks': [progress_hook],  # Adiciona a função de progresso
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Faz o download do vídeo
        messagebox.showinfo("Sucesso", "Vídeo baixado com sucesso!")  # Mensagem de sucesso
        progress_var.set(0)  # Reseta a barra de progresso
    except Exception as e:
        messagebox.showerror("Erro", str(e))  # Mensagem de erro se ocorrer

# Configuração da janela
app = tk.Tk()
app.title("Marcos Rocco e ChatGPT")  # Título da janela

tk.Label(app, text="Cole o link do vídeo:").pack(pady=10)  # Label para instrução

url_entry = tk.Entry(app, width=50)  # Campo de entrada para o link
url_entry.pack(pady=5)  # Adiciona o campo à janela

# Variável para a barra de progresso
progress_var = tk.DoubleVar()

# Barra de progresso
progress_bar = ttk.Progressbar(app, variable=progress_var, maximum=100)
progress_bar.pack(pady=10, fill=tk.X)

# Botão para baixar o vídeo
tk.Button(app, text="Baixar Vídeo", command=download_video).pack(pady=5)

app.mainloop()  # Inicia o loop principal da interface gráfica
