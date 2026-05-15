class Calculadora:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.resultado = 0

    def _validar_numeros(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Argumentos devem ser numeros")

    def somar(self, a, b):
        self._validar_numeros(a, b)
        resultado = a + b
        self.repositorio.salvar(f"{a} + {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def subtrair(self, a, b):
        self._validar_numeros(a, b)
        resultado = a - b
        self.repositorio.salvar(f"{a} - {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def multiplicar(self, a, b):
        self._validar_numeros(a, b)
        resultado = a * b
        self.repositorio.salvar(f"{a} * {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def dividir(self, a, b):
        self._validar_numeros(a, b)

        if b == 0:
            raise ValueError("Divisao por zero nao permitida")

        resultado = a / b
        self.repositorio.salvar(f"{a} / {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def potencia(self, base, expoente):
        self._validar_numeros(base, expoente)
        resultado = base ** expoente

        # BUG CORRIGIDO:
        # Antes estava usando "*" no histórico.
        # Correto: registrar "**" para representar potenciação.
        self.repositorio.salvar(f"{base} ** {expoente} = {resultado}")

        self.resultado = resultado
        return resultado

    def obter_ultimo_resultado(self):
        return self.resultado