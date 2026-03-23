import os
import json
import re
from datetime import datetime
import random

os.makedirs("_posts", exist_ok=True)

USED_TOPICS_FILE = ".used_topics.json"

topics = [
    # IA / ML
    ("IA em producao: decisoes tecnicas que importam", ["ia", "engenharia", "backend"]),
    ("RAG alem do hype: quando realmente usar", ["ia", "llm", "rag"]),
    ("Erros comuns ao escalar sistemas de IA", ["ia", "mlops"]),
    ("Fine-tuning vs prompting: qual escolher?", ["ia", "llm"]),
    ("Como avaliar a qualidade de respostas de LLMs", ["ia", "llm", "engenharia"]),
    ("Embeddings na pratica: busca semantica explicada", ["ia", "rag", "backend"]),
    ("MLOps: o que realmente importa em ambientes reais", ["ia", "mlops", "devops"]),
    ("Agentes de IA: autonomia com responsabilidade", ["ia", "llm", "arquitetura"]),

    # Cyber Security
    ("Falhas de seguranca comuns em APIs REST", ["security", "api", "backend"]),
    ("Por que autenticacao mal feita quebra sistemas", ["security", "auth"]),
    ("Boas praticas de cyber security que muitos ignoram", ["security", "infra"]),
    ("OWASP Top 10: entendendo as principais vulnerabilidades", ["security", "api"]),
    ("JWT na pratica: boas praticas e armadilhas", ["security", "auth", "backend"]),
    ("Como proteger variaveis de ambiente em producao", ["security", "devops", "infra"]),

    # Linguagens de Programacao
    ("Por que Python continua dominante no backend de IA", ["python", "backend", "ia"]),
    ("Quando NAO usar JavaScript no backend", ["javascript", "arquitetura"]),
    ("Comparando linguagens: performance vs produtividade", ["programacao"]),
    ("Go para desenvolvedores Python: principais diferencas", ["python", "programacao"]),
    ("TypeScript: vale a migracao?", ["javascript", "programacao"]),
    ("Rust em 2026: onde faz sentido usar", ["programacao", "performance"]),

    # Backend / Arquitetura
    ("Monolito ou microsservicos? A decisao real", ["arquitetura", "backend"]),
    ("Erros classicos ao escalar aplicacoes web", ["backend", "infra"]),
    ("Trade-offs tecnicos que todo backend enfrenta", ["engenharia", "arquitetura"]),
    ("Event-driven architecture: quando e por que usar", ["arquitetura", "backend"]),
    ("Cache na pratica: Redis e estrategias comuns", ["backend", "performance", "infra"]),
    ("Bancos de dados relacionais vs NoSQL em 2026", ["backend", "arquitetura"]),
    ("Filas de mensagem: RabbitMQ vs Kafka", ["arquitetura", "backend", "infra"]),

    # Softwares / Ferramentas
    ("Ferramentas que realmente aumentam produtividade dev", ["software", "produtividade"]),
    ("Automatizando tarefas repetitivas com scripts simples", ["automacao", "devops"]),
    ("Git alem do basico: habitos profissionais", ["git", "workflow"]),
    ("Docker na pratica: do desenvolvimento ao deploy", ["devops", "infra"]),
    ("VS Code extensions essenciais para 2026", ["software", "produtividade"]),

    # Hardware / Infra
    ("Como hardware impacta performance de aplicacoes", ["hardware", "performance"]),
    ("SSD vs HDD: impacto real no dia a dia do dev", ["hardware"]),
    ("Quando vale investir em mais RAM", ["hardware", "infra"]),
    ("Cloud vs on-premise: analise de custo real", ["infra", "arquitetura"]),

    # DevOps
    ("Automacao com GitHub Actions na pratica", ["devops", "automacao"]),
    ("Erros comuns em pipelines CI/CD", ["devops", "ci"]),
    ("Observabilidade: logs, metricas e traces", ["devops", "infra", "engenharia"]),
    ("Kubernetes para quem nunca usou: conceitos essenciais", ["devops", "infra"]),
    ("Infraestrutura como codigo com Terraform", ["devops", "infra", "automacao"]),
]

tag_content = {
    "ia": """\
## Por que isso importa agora

IA deixou de ser diferencial e virou requisito em muitos sistemas. Mas colocar um modelo em producao e diferente de fazer um notebook funcionar no Colab.

## O que vale prestar atencao

- Latencia e custo por requisicao sao os primeiros gargalos em producao
- Avaliar qualidade de respostas precisa de metricas claras, nao so "parece bom"
- Versionamento de modelos e dados e tao critico quanto versionamento de codigo

## Conclusao

O tema **{title}** aparece com frequencia em times que sairam do piloto e precisam escalar. Dominar os fundamentos evita retrabalho caro mais adiante.
""",
    "security": """\
## Por que seguranca ainda falha

A maioria das brechas nao vem de ataques sofisticados. Vem de configuracoes erradas, segredos expostos e validacoes que ninguem revisou.

## Pontos que fazem diferenca na pratica

- Nunca confie na validacao so no front-end
- Segredos em variaveis de ambiente, nunca no codigo
- Logs de auditoria salvam horas de investigacao em incidentes

## Conclusao

**{title}** e um tema que todo desenvolvedor deveria conhecer, independentemente de especialidade. Falhas de seguranca nao escolhem stack.
""",
    "backend": """\
## O dia a dia de quem mantem sistemas

Sistemas backend carregam o peso das regras de negocio, da consistencia dos dados e da performance que o usuario nunca ve, mas sente quando falta.

## O que separa codigo que escala de codigo que quebra

- Entender o caminho critico da requisicao antes de otimizar
- Tratar erros com intencao, nao so com try/catch generico
- Monitorar o que importa: latencia, taxa de erro e uso de recursos

## Conclusao

**{title}** e um desses temas que parece simples ate voce precisar lidar com ele em producao com carga real.
""",
    "devops": """\
## A distancia entre desenvolvimento e operacao

DevOps nao e ferramenta, e cultura. Mas certas ferramentas tornam a cultura possivel.

## O que times maduros fazem diferente

- Pipeline de CI/CD que falha rapido e com mensagem clara
- Ambientes de desenvolvimento proximos do ambiente de producao
- Rollback e tao importante quanto deploy

## Conclusao

**{title}** faz parte da base que qualquer time serio de engenharia precisa ter no radar.
""",
    "arquitetura": """\
## Decisoes que ficam

Arquitetura e dificil de mudar depois. Cada escolha feita hoje carrega custo ou beneficio por anos.

## O que guia boas decisoes arquiteturais

- Complexidade so se justifica quando a simplicidade ja foi tentada
- Acoplamento baixo e coesao alta nunca saem de moda
- Documentar o porque de uma decisao vale mais do que documentar o que ela faz

## Conclusao

O tema **{title}** e um bom ponto de partida para pensar nas trocas que todo sistema inevitavelmente enfrenta.
""",
    "default": """\
## Contexto

O tema de hoje e relevante para desenvolvedores que trabalham com tecnologia no dia a dia. A medida que os sistemas crescem, entender os trade-offs se torna essencial.

## Pontos principais

- Cada decisao tecnica tem consequencias na manutenibilidade do sistema
- A escolha certa depende sempre do contexto: tamanho do time, escala e requisitos
- Documentar decisoes e tao importante quanto toma-las

## Conclusao

**{title}** e um tema que aparece cedo ou tarde na carreira de qualquer desenvolvedor. Vale entender os fundamentos antes que o problema apareca em producao.
""",
}


def load_used_topics():
    if os.path.exists(USED_TOPICS_FILE):
        with open(USED_TOPICS_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    return set()


def save_used_topics(used):
    with open(USED_TOPICS_FILE, "w", encoding="utf-8") as f:
        json.dump(list(used), f, ensure_ascii=False)


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text).strip("-")
    return text[:60]


def pick_topic(used_titles):
    available = [t for t in topics if t[0] not in used_titles]
    if not available:
        used_titles.clear()
        available = topics
    return random.choice(available)


def get_content(title, tags):
    for tag in tags:
        if tag in tag_content:
            return tag_content[tag].format(title=title)
    return tag_content["default"].format(title=title)


today = datetime.now()
date_str = today.strftime("%Y-%m-%d")

used = load_used_topics()
post_title, post_tags = pick_topic(used)
used.add(post_title)
save_used_topics(used)

tags_formatted = "[" + ", ".join(f'"{tag}"' for tag in post_tags) + "]"
slug = slugify(post_title)
filename = f"_posts/{date_str}-{slug}.md"

body = get_content(post_title, post_tags)

post_content = f"""---
layout: post
title: "{post_title}"
date: {date_str}
categories: [Tecnologia, IA]
tags: {tags_formatted}
---

{body}
"""

with open(filename, "w", encoding="utf-8") as f:
    f.write(post_content)

print(f"Post criado: {filename}")
print(f"Titulo: {post_title}")
