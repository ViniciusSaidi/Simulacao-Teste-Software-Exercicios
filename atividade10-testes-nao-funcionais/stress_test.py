import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://jsonplaceholder.typicode.com"
ENDPOINT = "/posts/1"

NIVEIS_CONCORRENCIA = [10, 50, 100, 200, 500]
REQUISICOES_POR_NIVEL = 500

META_USUARIOS = 15000
LIMITE_ERRO_PERCENTUAL = 5


def fazer_requisicao():
    try:
        response = requests.get(f"{BASE_URL}{ENDPOINT}", timeout=5)
        return response.status_code
    except requests.RequestException:
        return 0


def testar_nivel(concorrencia):
    inicio = time.perf_counter()

    resultados = []

    with ThreadPoolExecutor(max_workers=concorrencia) as executor:
        futures = [
            executor.submit(fazer_requisicao)
            for _ in range(REQUISICOES_POR_NIVEL)
        ]

        for future in as_completed(futures):
            resultados.append(future.result())

    fim = time.perf_counter()

    tempo_total = fim - inicio
    sucessos = sum(1 for status in resultados if status == 200)
    erros = REQUISICOES_POR_NIVEL - sucessos
    taxa_erro = (erros / REQUISICOES_POR_NIVEL) * 100
    throughput = REQUISICOES_POR_NIVEL / tempo_total

    return {
        "concorrencia": concorrencia,
        "tempo_total": tempo_total,
        "throughput": throughput,
        "sucessos": sucessos,
        "erros": erros,
        "taxa_erro": taxa_erro,
    }


def executar_teste_estresse():
    print("\n=== TESTE DE ESTRESSE ===")
    print(f"Endpoint testado: {BASE_URL}{ENDPOINT}")
    print(f"Meta teórica: suportar mais de {META_USUARIOS} usuários")
    print(f"Limite de erro aceitável: até {LIMITE_ERRO_PERCENTUAL}%\n")

    ponto_de_quebra = None

    for concorrencia in NIVEIS_CONCORRENCIA:
        resultado = testar_nivel(concorrencia)

        print(f"Concorrência simulada: {resultado['concorrencia']}")
        print(f"Tempo total: {resultado['tempo_total']:.2f}s")
        print(f"Throughput: {resultado['throughput']:.2f} req/s")
        print(f"Sucessos: {resultado['sucessos']}")
        print(f"Erros: {resultado['erros']}")
        print(f"Taxa de erro: {resultado['taxa_erro']:.2f}%")
        print("-" * 40)

        if resultado["taxa_erro"] > LIMITE_ERRO_PERCENTUAL:
            ponto_de_quebra = concorrencia
            break

    print("\n=== RESULTADO FINAL ===")

    if ponto_de_quebra is None:
        print("Nenhum ponto de quebra encontrado nos níveis simulados.")
        print(f"Maior concorrência testada: {NIVEIS_CONCORRENCIA[-1]}")
        print("Resultado: INCONCLUSIVO para a meta de 15.000 usuários")
    else:
        print(f"Ponto de quebra encontrado em aproximadamente {ponto_de_quebra} usuários simultâneos.")

        if ponto_de_quebra > META_USUARIOS:
            print("Resultado: APROVADO")
        else:
            print("Resultado: REPROVADO")

    return ponto_de_quebra


if __name__ == "__main__":
    executar_teste_estresse()