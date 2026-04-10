# gerar_dados.py
import random
import csv
from pathlib import Path

BAIRROS = {
    "Asa Norte":    {"preco_base": 900_000, "desvio": 300_000},
    "Asa Sul":      {"preco_base": 950_000, "desvio": 320_000},
    "Lago Norte":   {"preco_base": 750_000, "desvio": 250_000},
    "Sudoeste":     {"preco_base": 700_000, "desvio": 200_000},
    "Águas Claras": {"preco_base": 450_000, "desvio": 150_000},
    "Taguatinga":   {"preco_base": 350_000, "desvio": 120_000},
    "Ceilândia":    {"preco_base": 250_000, "desvio":  80_000},
    "Samambaia":    {"preco_base": 200_000, "desvio":  60_000},
    "Planaltina":   {"preco_base": 180_000, "desvio":  50_000},
}

TIPOS = ["apartamento", "casa", "cobertura"]
CAMPOS = ["id", "bairro", "tipo", "quartos", "banheiros",
          "area_m2", "garagens", "andar", "novo", "preco"]


def _gerar_imovel(id_, rng):
    bairro = rng.choice(list(BAIRROS.keys()))
    tipo   = rng.choices(TIPOS, weights=[70, 25, 5])[0]
    quartos   = rng.randint(1, 4)
    banheiros = min(quartos, rng.randint(1, 3))
    area      = round(rng.uniform(35, 200), 1)
    garagens  = rng.randint(0, min(3, quartos))
    andar     = 0 if tipo == "casa" else rng.randint(1, 20)
    novo      = rng.random() < 0.3

    info  = BAIRROS[bairro]
    ruido = rng.gauss(0, info["desvio"])
    preco = (info["preco_base"]
             + area * 3_000
             + quartos * 30_000
             + (50_000 if novo else 0)
             + ruido)
    preco = max(80_000, round(preco, -3))

    return {"id": id_, "bairro": bairro, "tipo": tipo,
            "quartos": quartos, "banheiros": banheiros,
            "area_m2": area, "garagens": garagens,
            "andar": andar, "novo": novo, "preco": preco}


def gerar_dados(n=500, seed=42):
    """Gera dataset de imóveis do DF e salva em dados/imoveis_df.csv."""
    rng = random.Random(seed)
    imoveis = [_gerar_imovel(i + 1, rng) for i in range(n)]

    campos_nulaveis = ["banheiros", "garagens", "andar", "novo"]
    for imovel in imoveis:
        if rng.random() < 0.05:
            imovel[rng.choice(campos_nulaveis)] = ""
        if rng.random() < 0.03:
            imovel["area_m2"] = f"{imovel['area_m2']} m²"
        if rng.random() < 0.01:
            imovel["preco"] = rng.choice([9_999_999, 1])

    Path("dados").mkdir(exist_ok=True)
    with open("dados/imoveis_df.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CAMPOS)
        writer.writeheader()
        writer.writerows(imoveis)

    print(f"✓ {n} imóveis gerados em 'dados/imoveis_df.csv'")


if __name__ == "__main__":
    gerar_dados()
