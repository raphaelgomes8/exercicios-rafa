"""Testes do exercício 01 — Listas e Filtros (importados pelo arquivo do aluno)."""


def teste_f1(dados, r):
    assert isinstance(r, int), "Retorne um número inteiro"
    assert 0 < r < 500, "Valor fora do esperado"
    print("✓ Fácil 1 passou!")


def teste_f2(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == len(set(r)), "A lista não pode ter repetições"
    assert len(r) >= 5, "Esperado pelo menos 5 bairros"
    print("✓ Fácil 2 passou!")


def teste_f3(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert all(d["tipo"] == "apartamento" for d in r), "Todos devem ser apartamento"
    assert len(r) > 0, "Lista não pode ser vazia"
    print("✓ Fácil 3 passou!")


def teste_f4(dados, r):
    assert isinstance(r, dict), "Retorne um dicionário"
    assert "preco" in r, "O dicionário deve ter a chave 'preco'"
    precos = [float(d["preco"]) for d in dados if d["preco"]]
    assert float(r["preco"]) == max(precos), "Não é o mais caro"
    print("✓ Fácil 4 passou!")


def teste_f5(dados, r):
    assert isinstance(r, int), "Retorne um inteiro"
    assert r > 0, "A soma deve ser maior que zero"
    print("✓ Fácil 5 passou!")


def teste_m1(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    for d in r:
        assert float(d["area_m2"]) > 80, "area_m2 deve ser > 80"
        assert float(d["preco"]) < 500_000, "preco deve ser < 500000"
    print("✓ Médio 1 passou!")


def teste_m2(dados, r):
    assert isinstance(r, dict), "Retorne um dicionário"
    assert set(r.keys()) == {"apartamento", "casa", "cobertura"}, "Chaves erradas"
    total = sum(len(v) for v in r.values())
    assert total == len(dados), "Nenhum imóvel pode ficar de fora"
    print("✓ Médio 2 passou!")


def teste_m3(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == len(dados), "Não pode perder imóveis"
    precos = [float(d["preco"]) for d in r]
    assert precos == sorted(precos), "Lista não está ordenada por preço"
    print("✓ Médio 3 passou!")


def teste_m4(dados, r):
    assert isinstance(r, dict), "Retorne um dicionário"
    assert sum(r.values()) == len(dados), "A soma deve ser igual ao total de imóveis"
    assert all(isinstance(v, int) for v in r.values()), "Valores devem ser inteiros"
    print("✓ Médio 4 passou!")


def teste_m5(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == 5, "Retorne exatamente 5 imóveis"
    print("✓ Médio 5 passou!")


def teste_d1(dados, r):
    assert isinstance(r, dict), "Retorne um dicionário"
    assert len(r) >= 5, "Esperado pelo menos 5 bairros"
    assert all(isinstance(v, float) for v in r.values()), "Valores devem ser float"
    assert r.get("Asa Norte", 0) > r.get("Ceilândia", 0), \
        "Asa Norte deve ter preço médio maior que Ceilândia"
    print("✓ Difícil 1 passou!")


def teste_d2(busca_binaria):
    lista = [100_000, 200_000, 300_000, 400_000, 500_000]
    assert busca_binaria(lista, 300_000) == 2, "Índice errado para 300k"
    assert busca_binaria(lista, 250_000) == 2, "Deve retornar o primeiro >= 250k"
    assert busca_binaria(lista, 100_000) == 0, "Deve retornar 0 para o menor"
    print("✓ Difícil 2 passou!")


def teste_d3(dados, r):
    assert r is not None, "Calcule o valor"
    assert 100_000 <= r <= 900_000, "Regra deve estar entre 100k e 900k"
    print(f"✓ Difícil 3 passou! Melhor regra: R$ {r:,.0f}")


def teste_d4(dados, r):
    assert isinstance(r, dict), "Retorne um dicionário"
    assert "ranking" in r, "Chave 'ranking' obrigatória"
    assert len(r["ranking"]) == 10, "Esperado 10 entradas (5 mais baratos + 5 mais caros)"
    print("✓ Difícil 4 passou!")


def teste_d5(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == 3, "Retorne exatamente 3 imóveis"
    for d in r:
        assert "area_m2" in d and "quartos" in d, "Dicionários incompletos"
    print("✓ Difícil 5 passou!")


def rodar_todos_os_testes(mod):
    """mod: módulo carregado do exercício (atributos dados, resultados, busca_binaria)."""
    dados = mod.dados
    teste_f1(dados, mod.resultado_f1)
    teste_f2(dados, mod.resultado_f2)
    teste_f3(dados, mod.resultado_f3)
    teste_f4(dados, mod.resultado_f4)
    teste_f5(dados, mod.resultado_f5)
    teste_m1(dados, mod.resultado_m1)
    teste_m2(dados, mod.resultado_m2)
    teste_m3(dados, mod.resultado_m3)
    teste_m4(dados, mod.resultado_m4)
    teste_m5(dados, mod.resultado_m5)
    teste_d1(dados, mod.resultado_d1)
    teste_d2(mod.busca_binaria)
    teste_d3(dados, mod.melhor_regra)
    teste_d4(dados, mod.resultado_d4)
    teste_d5(dados, mod.resultado_d5)
