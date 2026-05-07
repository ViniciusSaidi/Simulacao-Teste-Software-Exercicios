import time
import statistics
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINT = "/posts/1"
TOTAL_REQUISICOES = 50
META_P95_MS = 500


def calcular_percentil(valores, percentil):
    valores_ordenados = sorted(valores)
    indice = int((percentil / 100) * len(valores_ordenados)) - 1
    indice = max(indice, 0)
    return valores_ordenados[indice]


def executar_teste_desempenho():
    tempos_resposta = []

    for _ in range(TOTAL_REQUISICOES):
        inicio = time.perf_counter()

        resposta = requests.get(f"{BASE_URL}{ENDPOINT}")

        fim = time.perf_counter()

        tempo_ms = (fim - inicio) * 1000
        tempos_resposta.append(tempo_ms)

        assert resposta.status_code == 200

    media = statistics.mean(tempos_resposta)
    p95 = calcular_percentil(tempos_resposta, 95)

    print("\n=== TESTE DE DESEMPENHO ===")
    print(f"Endpoint testado: {BASE_URL}{ENDPOINT}")
    print(f"Total de requisições: {TOTAL_REQUISICOES}")
    print(f"Tempo médio: {media:.2f} ms")
    print(f"P95: {p95:.2f} ms")
    print(f"Meta: P95 < {META_P95_MS} ms")

    if p95 < META_P95_MS:
        print("Resultado: APROVADO")
    else:
        print("Resultado: REPROVADO")

    assert p95 < META_P95_MS


if __name__ == "__main__":
    executar_teste_desempenho()