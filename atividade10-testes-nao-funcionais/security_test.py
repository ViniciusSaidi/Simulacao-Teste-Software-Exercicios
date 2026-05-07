import time
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINT = "/posts/1"

LIMITE_REQ_POR_MINUTO = 100
TOTAL_REQUISICOES = 120


def executar_teste_seguranca_rate_limit():
    respostas = []

    inicio = time.perf_counter()

    for _ in range(TOTAL_REQUISICOES):
        response = requests.get(f"{BASE_URL}{ENDPOINT}")
        respostas.append(response.status_code)

    fim = time.perf_counter()

    tempo_total = fim - inicio
    total_429 = respostas.count(429)
    total_sucesso = respostas.count(200)

    print("\n=== TESTE DE SEGURANÇA: RATE LIMITING ===")
    print(f"Endpoint testado: {BASE_URL}{ENDPOINT}")
    print(f"Total de requisições enviadas: {TOTAL_REQUISICOES}")
    print(f"Tempo total: {tempo_total:.2f}s")
    print(f"Respostas 200 OK: {total_sucesso}")
    print(f"Respostas 429 Too Many Requests: {total_429}")
    print(f"Meta esperada: bloquear acima de {LIMITE_REQ_POR_MINUTO} req/min/IP")

    if total_429 > 0:
        print("Resultado: APROVADO")
        print("A API apresentou comportamento de rate limiting.")
    else:
        print("Resultado: REPROVADO")
        print("A API não retornou 429 mesmo acima do limite esperado.")

    return total_429 > 0


if __name__ == "__main__":
    executar_teste_seguranca_rate_limit()