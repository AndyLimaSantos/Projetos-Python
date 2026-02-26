import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# =========================
# Configuração
# =========================

random.seed(42)
np.random.seed(42)

NUM_CLIENTES = 5000
NUM_EMPRESTIMOS = 5000
NUM_PAGAMENTOS = 5000

cidades = [
    "São Paulo", "Rio de Janeiro", "Belo Horizonte",
    "Curitiba", "Salvador", "Fortaleza", "Brasília"
]

status_opcoes = ["ativo", "quitado", "inadimplente"]

# =========================
# 1️⃣ Gerar Clientes
# =========================

clientes = []

for i in range(1, NUM_CLIENTES + 1):
    data_nasc = datetime(1950, 1, 1) + timedelta(days=random.randint(0, 20000))
    data_cadastro = datetime(2018, 1, 1) + timedelta(days=random.randint(0, 2500))

    clientes.append({
        "id_cliente": i,
        "nome": f"Cliente_{i}",
        "data_nascimento": data_nasc.date(),
        "cidade": random.choice(cidades),
        "data_cadastro": data_cadastro.date()
    })

clientes_df = pd.DataFrame(clientes)

# =========================
# 2️⃣ Gerar Empréstimos
# =========================

emprestimos = []

for i in range(1, NUM_EMPRESTIMOS + 1):
    cliente_id = random.randint(1, NUM_CLIENTES)
    valor = random.randint(1000, 50000)
    taxa = round(random.uniform(0.01, 0.05), 3)
    data_contratacao = datetime(2020, 1, 1) + timedelta(days=random.randint(0, 1500))
    status = random.choice(status_opcoes)

    emprestimos.append({
        "id_emprestimo": i,
        "id_cliente": cliente_id,
        "valor": valor,
        "taxa_juros": taxa,
        "data_contratacao": data_contratacao.date(),
        "status": status
    })

emprestimos_df = pd.DataFrame(emprestimos)

# =========================
# 3️⃣ Gerar Pagamentos
# =========================

pagamentos = []

for i in range(1, NUM_PAGAMENTOS + 1):
    emprestimo_id = random.randint(1, NUM_EMPRESTIMOS)
    valor_pago = random.randint(200, 10000)
    data_pagamento = datetime(2020, 6, 1) + timedelta(days=random.randint(0, 1200))

    pagamentos.append({
        "id_pagamento": i,
        "id_emprestimo": emprestimo_id,
        "valor_pago": valor_pago,
        "data_pagamento": data_pagamento.date()
    })

pagamentos_df = pd.DataFrame(pagamentos)

# =========================
# Exportação em CSV
# =========================

clientes_df.to_csv("Clientes.csv",index =False)
emprestimos_df.to_csv("Emprestimos.csv",index =False)
pagamentos_df.to_csv("Pagamentos.csv",index =False)