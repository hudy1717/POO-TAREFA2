from datetime import datetime, timedelta

class Musica:
    def __init__(self, id: int, titulo: str, artista: str, album: str, duracao: timedelta):
        self.__id = id
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__duracao = duracao

    def get_id(self): return self.__id
    def set_id(self, id: int): self.__id = id
    def get_titulo(self): return self.__titulo
    def set_titulo(self, t: str): self.__titulo = t
    def get_artista(self): return self.__artista
    def set_artista(self, a: str): self.__artista = a
    def get_album(self): return self.__album
    def set_album(self, alb: str): self.__album = alb
    def get_duracao(self): return self.__duracao
    def set_duracao(self, d: timedelta): self.__duracao = d

    def __str__(self):
        return f"[{self.__id}] {self.__titulo} - {self.__artista} (Álbum: {self.__album}) | Duração: {self.__duracao}"


class PlayList:
    def __init__(self, id: int, nome: str, descricao: str):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao

    def get_id(self): return self.__id
    def set_id(self, id: int): self.__id = id
    def get_nome(self): return self.__nome
    def set_nome(self, n: str): self.__nome = n
    def get_descricao(self): return self.__descricao
    def set_descricao(self, d: str): self.__descricao = d

    def tempo_total(self, lista_itens, lista_musicas) -> timedelta:
        total = timedelta()
        for item in lista_itens:
            if item.get_id_playlist() == self.__id:
                for m in lista_musicas:
                    if m.get_id() == item.get_id_musica():
                        total += m.get_duracao()
        return total

    def __str__(self):
        return f"ID: {self.__id} | Nome: {self.__nome} | Descrição: {self.__descricao}"


class PlayListItem:
    def __init__(self, id: int, id_playlist: int, id_musica: int, data_inclusao: datetime, sequencia: int):
        self.__id = id
        self.__id_playlist = id_playlist
        self.__id_musica = id_musica
        self.__data_inclusao = data_inclusao
        self.__sequencia = sequencia

    def get_id(self): return self.__id
    def set_id(self, id: int): self.__id = id
    def get_id_playlist(self): return self.__id_playlist
    def set_id_playlist(self, ip: int): self.__id_playlist = ip
    def get_id_musica(self): return self.__id_musica
    def set_id_musica(self, im: int): self.__id_musica = im
    def get_data_inclusao(self): return self.__data_inclusao
    def set_data_inclusao(self, d: datetime): self.__data_inclusao = d
    def get_sequencia(self): return self.__sequencia
    def set_sequencia(self, s: int): self.__sequencia = s

    def __str__(self):
        dt_str = self.__data_inclusao.strftime("%d/%m/%Y %H:%M")
        return f"Item ID: {self.__id} | Playlist ID: {self.__id_playlist} | Música ID: {self.__id_musica} | Seq: {self.__sequencia} | Incluído em: {dt_str}"


class UI:
    def __init__(self):
        self.__playlists = []
        self.__musicas = []
        self.__itens = []

    def menu() -> int:
        print("\n=== SISTEMA DE PLAYLISTS ===")
        print("1. Cadastrar Músicas")
        print("2. Cadastrar Playlists")
        print("3. Gerir Itens da Playlist (Adicionar/Remover Músicas)")
        print("0. Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def main(self):
        op = -1
        while op != 0:
            op = UI.menu()
            if op == 1:
                self.gerir_musicas()
            elif op == 2:
                self.gerir_playlists()
            elif op == 3:
                self.gerir_itens()
            elif op == 0:
                print("A encerrar...")

    def gerir_musicas(self):
        print("\n--- GESTÃO DE MÚSICAS ---")
        print("1. Inserir | 2. Listar | 3. Excluir")
        op = input("Opção: ")
        if op == "1":
            id_m = int(input("ID: "))
            tit = input("Título: ")
            art = input("Artista: ")
            alb = input("Álbum: ")
            dur_str = input("Duração (mm:ss): ")
            m, s = map(int, dur_str.split(':'))
            dur = timedelta(minutes=m, seconds=s)
            self.__musicas.append(Musica(id_m, tit, art, alb, dur))
            print("Música inserida!")
        elif op == "2":
            for m in self.__musicas:
                print(m)
        elif op == "3":
            id_m = int(input("ID da música a excluir: "))
            self.__musicas = [m for m in self.__musicas if m.get_id() != id_m]
            print("Música excluída!")

    def gerir_playlists(self):
        print("\n--- GESTÃO DE PLAYLISTS ---")
        print("1. Inserir | 2. Listar (com Tempo Total) | 3. Excluir")
        op = input("Opção: ")
        if op == "1":
            id_p = int(input("ID: "))
            nome = input("Nome: ")
            desc = input("Descrição: ")
            self.__playlists.append(PlayList(id_p, nome, desc))
            print("Playlist inserida!")
        elif op == "2":
            for p in self.__playlists:
                tt = p.tempo_total(self.__itens, self.__musicas)
                print(f"{p} | Tempo Total: {tt}")
        elif op == "3":
            id_p = int(input("ID da playlist a excluir: "))
            self.__playlists = [p for p in self.__playlists if p.get_id() != id_p]
            print("Playlist excluída!")

    def gerir_itens(self):
        print("\n--- ITENS DA PLAYLIST ---")
        print("1. Adicionar Música a Playlist | 2. Listar Músicas de uma Playlist")
        op = input("Opção: ")
        if op == "1":
            id_i = int(input("ID do Item: "))
            id_p = int(input("ID da Playlist: "))
            id_m = int(input("ID da Música: "))
            seq = int(input("Sequência/Posição: "))
            dt = datetime.now()
            self.__itens.append(PlayListItem(id_i, id_p, id_m, dt, seq))
            print("Música adicionada à playlist!")
        elif op == "2":
            id_p = int(input("ID da Playlist: "))
            print(f"\nMúsicas da Playlist {id_p}:")
            for item in self.__itens:
                if item.get_id_playlist() == id_p:
                    musica = next((m for m in self.__musicas if m.get_id() == item.get_id_musica()), None)
                    print(f"Posição {item.get_sequencia()}: {musica}")


if __name__ == "__main__":
    ui = UI()
    ui.main()