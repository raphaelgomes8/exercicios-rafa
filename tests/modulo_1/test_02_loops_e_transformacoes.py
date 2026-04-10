"""Testes do exercício 02 — Loops e Transformações."""

from collections import defaultdict


def teste_f1(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) > 0, "Lista não pode ser vazia"
    esperado = len([d for d in dados if d["preco"]])
    assert len(r) == esperado, "Quantidade deve bater com imóveis com preço válido"
    for s in r:
        assert isinstance(s, str), "Cada item deve ser string"
        assert s.startswith("R$ "), 'Formato deve começar com "R$ "'
        resto = s[3:].strip()
        assert resto.replace(".", "").isdigit(), "Parte numérica inválida"
    print("✓ Fácil 1 passou!")


def teste_f2(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == len(dados), "Deve ter um item por imóvel"
    for i, d in enumerate(dados):
        assert r[i] == d["bairro"].upper(), "Use .upper() no nome do bairro"
    print("✓ Fácil 2 passou!")


def teste_f3(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert all(isinstance(x, int) for x in r), "Todos devem ser int"
    assert len(r) == len([d for d in dados if d["quartos"]]), "Tamanho incorreto"
    assert all(1 <= x <= 4 for x in r), "Quartos deve estar entre 1 e 4"
    print("✓ Fácil 3 passou!")


def teste_f4(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == len(dados), "Um dicionário por imóvel"
    for orig, novo in zip(dados, r):
        if orig["preco"]:
            assert "preco_mil" in novo, "Falta preco_mil quando há preco"
            assert abs(novo["preco_mil"] - float(orig["preco"]) / 1000) < 1e-6
    print("✓ Fácil 4 passou!")


def teste_f5(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == len(dados)
    for d, s in zip(dados, r):
        assert s == f'{d["id"]}:{d["bairro"]}'
    print("✓ Fácil 5 passou!")


def teste_m1(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    precos = [float(d["preco"]) for d in dados if d["preco"]]
    assert len(r) == len(precos), "Um valor normalizado por preço válido na ordem"
    if precos:
        assert min(r) >= 0 and max(r) <= 1, "Valores devem estar em [0, 1]"
        if min(precos) != max(precos):
            assert min(r) == 0.0 or abs(min(r) - 0.0) < 1e-9
            assert max(r) == 1.0 or abs(max(r) - 1.0) < 1e-9
    print("✓ Médio 1 passou!")


def teste_m2(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    n = len(dados)
    esperado_len = n // 100
    assert len(r) == esperado_len, "Um total a cada 100 imóveis"
    acum = 0.0
    idx = 0
    for i, d in enumerate(dados, start=1):
        acum += float(d["preco"]) if d["preco"] else 0.0
        if i % 100 == 0:
            assert abs(r[idx] - acum) < 0.01, f"Total no marco {i} incorreto"
            idx += 1
    print("✓ Médio 2 passou!")


def teste_m3(dados, r):
    assert isinstance(r, dict), "Retorne um dicionário"
    assert set(r.keys()) == {1, 2, 3, 4}, "Chaves devem ser 1, 2, 3 e 4"
    for q in (1, 2, 3, 4):
        esperado = sum(
            1 for d in dados
            if d["quartos"] and int(d["quartos"]) == q
        )
        assert r[q] == esperado, f"Contagem errada para {q} quartos"
    print("✓ Médio 3 passou!")


def teste_m4(dados, r):
    assert isinstance(r, dict), "Retorne um dicionário"
    assert len(r) == len(dados), "Um imóvel por id"
    for d in dados:
        k = int(d["id"])
        assert k in r, f"Falta id {k}"
        assert r[k]["id"] == d["id"]
    print("✓ Médio 4 passou!")


def teste_m5(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == len(dados)
    for d, mini in zip(dados, r):
        assert set(mini.keys()) == {"id", "bairro", "preco"}
        assert mini["id"] == d["id"] and mini["bairro"] == d["bairro"] \
            and mini["preco"] == d["preco"]
    print("✓ Médio 5 passou!")


def teste_d1(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) <= 10, "No máximo 10 imóveis"
    candidatos = []
    for d in dados:
        if d["tipo"] != "apartamento":
            continue
        try:
            float(d["area_m2"])
        except ValueError:
            continue
        candidatos.append(d)
    candidatos.sort(key=lambda x: float(x["area_m2"]), reverse=True)
    esperado_ids = [d["id"] for d in candidatos[:10]]
    assert [d["id"] for d in r] == esperado_ids, "Deve ser o top 10 por área (apartamentos, área numérica)"
    areas = [float(d["area_m2"]) for d in r]
    assert areas == sorted(areas, reverse=True), "Ordem por área decrescente"
    print("✓ Difícil 1 passou!")


def teste_d2(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    ordenados = sorted(dados, key=lambda d: int(d["id"]))
    esperados = []
    for a, b in zip(ordenados, ordenados[1:]):
        if not a["preco"] or not b["preco"]:
            continue
        pa, pb = float(a["preco"]), float(b["preco"])
        if pa == 0:
            continue
        esperados.append((pb - pa) / pa * 100)
    assert len(r) == len(esperados), "Quantidade de variações incorreta"
    for x, y in zip(r, esperados):
        assert abs(x - y) < 0.01
    print("✓ Difícil 2 passou!")


def teste_d3(mod):
    def so_ap(d):
        return [x for x in d if x["tipo"] == "apartamento"]

    def pega_ids(lst):
        return [int(x["id"]) for x in lst]

    entrada = mod.dados[:5]
    out = mod.transformar(entrada, [so_ap, pega_ids])
    assert isinstance(out, list)
    assert all(isinstance(i, int) for i in out)
    print("✓ Difícil 3 passou!")


def teste_d4(dados, r):
    assert isinstance(r, list), "Retorne uma lista"
    assert len(r) == len(dados)
    por_bairro = defaultdict(list)
    for d, z in zip(dados, r):
        if not d["preco"]:
            assert z is None, "Sem preço → None"
        else:
            assert isinstance(z, float), "Com preço → float"
            por_bairro[d["bairro"]].append(z)
    for b, zs in por_bairro.items():
        if len(zs) >= 2:
            media = sum(zs) / len(zs)
            assert abs(media) < 1e-5, f"Média do z-score no bairro {b!r} deveria ser ~0"
    print("✓ Difícil 4 passou!")


def teste_d5(mod):
    agg = mod.agrupar_e_agregar(mod.dados, "tipo", "preco", sum)
    assert isinstance(agg, dict)
    assert set(agg.keys()) <= {"apartamento", "casa", "cobertura"}
    for k, v in agg.items():
        assert isinstance(v, (int, float))
    print("✓ Difícil 5 passou!")


def rodar_todos_os_testes(mod):
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
    teste_d2(dados, mod.resultado_d2)
    teste_d3(mod)
    teste_d4(dados, mod.resultado_d4)
    teste_d5(mod)
