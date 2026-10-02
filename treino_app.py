from datetime import datetime, timedelta

class Treino:
    def __init__(self, id: int, dt: datetime, ds: float, t: timedelta):
        self.__id = id
        self.__data = dt
        self.__distancia = ds
        self.__tempo = t

    def get_id(self):
        return self.__id

    def set_id(self, id: int):
        self.__id = id

    def get_data(self):
        return self.__data

    def set_data(self, dt: datetime):
        self.__data = dt

    def get_distancia(self):
        return self.__distancia

    def set_distancia(self, ds: float):
        self.__distancia = ds

    def get_tempo(self):
        return self.__tempo

    def set_tempo(self, t: timedelta):
        self.__tempo = t

    def pace(self) -> timedelta:
        if self.__distancia <= 0:
            return timedelta(0)
        total_segundos = self.__tempo.total_seconds()
        segundos_por_km = total_segundos / self.__distancia
        return timedelta(seconds=segundos_por_km)

    def __str__(self):
        p = self.pace()
        total_p_sec = int(p.total_seconds())
        minutos = total_p_sec // 60
        segundos = total_p_sec % 60
        data_str = self.__data.strftime("%d/%m/%Y")
        return (f"ID: {self.__id} | Data: {data_str} | "
                f"Distância: {self.__distancia:.2f} km | Tempo: {self.__tempo} | "
                f"Pace: {minutos:02d}:{segundos:02d} min/km")


class TreinoUI:
    def __init__(self):
        self.__treinos = []

    def menu() -> int:
        print("\n--- MENU TREINOS ---")
        print("1. Inserir Treino")
        print("2. Listar Todos os Treinos")
        print("3. Listar Treino por ID")
        print("4. Atualizar Treino")
        print("5. Excluir Treino")
        print("6. Treino Mais Rápido (Menor Pace)")
        print("0. Sair")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    def main(self):
        op = -1
        while op != 0:
            op = TreinoUI.menu()
            if op == 1:
                self.inserir()
            elif op == 2:
                self.listar()
            elif op == 3:
                self.listar_id()
            elif op == 4:
                self.atualizar()
            elif op == 5:
                self.excluir()
            elif op == 6:
                self.mais_rapido()
            elif op == 0:
                print("A encerrar a aplicação...")
            else:
                print("Opção inválida!")

    def inserir(self):
        print("\n--- Inserir Treino ---")
        try:
            id_t = int(input("ID: "))
            for t in self.__treinos:
                if t.get_id() == id_t:
                    print("Erro: Já existe um treino com este ID!")
                    return
            dt_str = input("Data (dd/mm/aaaa): ")
            dt = datetime.strptime(dt_str, "%d/%m/%Y")
            ds = float(input("Distância (km): "))
            tempo_str = input("Tempo (hh:mm:ss): ")
            h, m, s = map(int, tempo_str.split(':'))
            tempo = timedelta(hours=h, minutes=m, seconds=s)

            treino = Treino(id_t, dt, ds, tempo)
            self.__treinos.append(treino)
            print("Treino inserido com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir treino: {e}")

    def listar(self):
        print("\n--- Listar Treinos ---")
        if not self.__treinos:
            print("Nenhum treino registado.")
            return
        for t in self.__treinos:
            print(t)

    def listar_id(self):
        print("\n--- Listar Treino por ID ---")
        try:
            id_t = int(input("Informe o ID: "))
            for t in self.__treinos:
                if t.get_id() == id_t:
                    print(t)
                    return
            print("Treino não encontrado.")
        except ValueError:
            print("ID inválido!")

    def atualizar(self):
        print("\n--- Atualizar Treino ---")
        try:
            id_t = int(input("Informe o ID do treino a atualizar: "))
            for t in self.__treinos:
                if t.get_id() == id_t:
                    dt_str = input("Nova Data (dd/mm/aaaa): ")
                    dt = datetime.strptime(dt_str, "%d/%m/%Y")
                    ds = float(input("Nova Distância (km): "))
                    tempo_str = input("Novo Tempo (hh:mm:ss): ")
                    h, m, s = map(int, tempo_str.split(':'))
                    tempo = timedelta(hours=h, minutes=m, seconds=s)

                    t.set_data(dt)
                    t.set_distancia(ds)
                    t.set_tempo(tempo)
                    print("Treino atualizado com sucesso!")
                    return
            print("Treino não encontrado.")
        except Exception as e:
            print(f"Erro ao atualizar treino: {e}")

    def excluir(self):
        print("\n--- Excluir Treino ---")
        try:
            id_t = int(input("Informe o ID do treino a excluir: "))
            for t in self.__treinos:
                if t.get_id() == id_t:
                    self.__treinos.remove(t)
                    print("Treino excluído com sucesso!")
                    return
            print("Treino não encontrado.")
        except ValueError:
            print("ID inválido!")

    def mais_rapido(self):
        print("\n--- Treino Mais Rápido ---")
        if not self.__treinos:
            print("Nenhum treino registado.")
            return
        mais_rapido = min(self.__treinos, key=lambda t: t.pace())
        print(mais_rapido)


if __name__ == "__main__":
    ui = TreinoUI()
    ui.main()