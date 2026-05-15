META_EFICIENCIA = 80

CENARIOS = [
    {
        "servidores": 1,
        "throughput_real": 200,
    },
    {
        "servidores": 2,
        "throughput_real": 380,
    },
    {
        "servidores": 4,
        "throughput_real": 720,
    },
    {
        "servidores": 8,
        "throughput_real": 1280,
    },
]


def calcular_eficiencia(throughput_base, servidores, throughput_real):
    throughput_ideal = throughput_base * servidores
    eficiencia = (throughput_real / throughput_ideal) * 100
    return throughput_ideal, eficiencia


def executar_teste_escalabilidade():
    print("\n=== TESTE DE ESCALABILIDADE ===")
    print(f"Meta: eficiência horizontal > {META_EFICIENCIA}%\n")

    throughput_base = CENARIOS[0]["throughput_real"]

    aprovado_geral = True

    for cenario in CENARIOS:
        servidores = cenario["servidores"]
        throughput_real = cenario["throughput_real"]

        throughput_ideal, eficiencia = calcular_eficiencia(
            throughput_base,
            servidores,
            throughput_real
        )

        print(f"Servidores: {servidores}")
        print(f"Throughput real: {throughput_real} req/s")
        print(f"Throughput ideal: {throughput_ideal} req/s")
        print(f"Eficiência horizontal: {eficiencia:.2f}%")

        if eficiencia > META_EFICIENCIA:
            print("Resultado do cenário: APROVADO")
        else:
            print("Resultado do cenário: REPROVADO")
            aprovado_geral = False

        print("-" * 40)

    print("\n=== RESULTADO FINAL ===")

    if aprovado_geral:
        print("Resultado geral: APROVADO")
    else:
        print("Resultado geral: REPROVADO")


if __name__ == "__main__":
    executar_teste_escalabilidade()