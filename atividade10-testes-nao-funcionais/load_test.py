import time
import requests
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINT = "/posts/1"

TOTAL_REQUISICOES = 500
CONCORRENCIA = 50

META_THROUGHPUT = 2000  # req/s


def fazer_requisicao():
    response = requests.get(f"{BASE_URL}{ENDPOINT}")
    return response.status_code


def executar_teste_carga():
    inicio = time.perf_counter()

    with ThreadPoolExecutor(max_workers=CONCORRENCIA) as executor:
        resultados = list(executor.map(lambda _: fazer_requisicao(), range(TOTAL_REQUISICOES)))

    fim = time.perf_counter()

    tempo_total = fim - inicio
    throughput = TOTAL_REQUISICOES / tempo_total

    sucesso = sum(1 for r in resultados if r == 200)
    taxa_sucesso = (sucesso / TOTAL_REQUISICOES) * 100

    print("\n=== TESTE DE CARGA ===")
    print(f"Total de requisições: {TOTAL_REQUISICOES}")
    print(f"Concorrência: {CONCORRENCIA}")
    print(f"Tempo total: {tempo_total:.2f}s")
    print(f"Throughput: {throughput:.2f} req/s")
    print(f"Taxa de sucesso: {taxa_sucesso:.2f}%")
    print(f"Meta: > {META_THROUGHPUT} req/s")

    if throughput > META_THROUGHPUT:
        print("Resultado: APROVADO")
    else:
        print("Resultado: REPROVADO")

    assert taxa_sucesso > 95  # valida estabilidade mínima


if __name__ == "__main__":
    executar_teste_carga()