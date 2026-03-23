import os
from datetime import datetime
import random

os.makedirs("_posts", exist_ok=True)

topics = [
    # IA / ML
    ("IA em produção: decisões técnicas que importam", ["ia", "engenharia", "backend"]),
    ("RAG além do hype: quando realmente usar", ["ia", "llm", "rag"]),
    ("Erros comuns ao escalar sistemas de IA", ["ia", "mlops"]),
    ("Fine-tuning vs prompting: qual escolher?", ["ia", "llm"]),
    ("Como avaliar a qualidade de respostas de LLMs", ["ia", "llm", "engenharia"]),
    ("Embeddings na prática: busca semântica explicada", ["ia", "rag", "backend"]),
    ("MLOps: o que realmente importa em ambientes reais", ["ia", "mlops", "devops"]),
    ("Agentes de IA: autonomia com responsabilidade", ["ia", "llm", "arquitetura"]),

    # Cyber Security
    ("Falhas de segurança comuns em APIs REST", ["security", "api", "backend"]),
    ("Por que autenticação mal feita quebra sistemas", ["security", "auth"]),
    ("Boas práticas de cyber security que muitos ignoram", ["security", "infra"]),
    ("OWASP Top 10: entendendo as principais vulnerabilidades", ["security", "api"]),
    ("JWT na prática: boas práticas e armadilhas", ["security", "auth", "backend"]),
    ("Como proteger variáveis de ambiente em produção", ["security", "devops", "infra"]),

    # Linguagens de Programação
    ("Por que Python continua dominante no backend de IA", ["python", "backend", "ia"]),
    ("Quando NÃO usar JavaScript no backend", ["javascript", "arquitetura"]),
    ("Comparando linguagens: performance vs produtividade", ["programacao"]),
    ("Go para desenvolvedores Python: principais diferenças", ["python", "programacao"]),
    ("TypeScript: vale a migração?", ["javascript", "programacao"]),
    ("Rust em 2025: onde faz sentido usar", ["programacao", "performance"]),

    # Backend / Arquitetura
    ("Monólito ou microsserviços? A decisão real", ["arquitetura", "backend"]),
    ("Erros clássicos ao escalar aplicações web", ["backend", "infra"]),
    ("Trade-offs técnicos que todo backend enfrenta", ["engenharia", "arquitetura"]),
    ("Event-driven architecture: quando e por que usar", ["arquitetura", "backend"]),
    ("Cache na prática: Redis e estratégias comuns", ["backend", "performance", "infra"]),
    ("Bancos de dados relacionais vs NoSQL em 2025", ["backend", "arquitetura"]),
    ("Filas de mensagem: RabbitMQ vs Kafka", ["arquitetura", "backend", "infra"]),

    # Softwares / Ferramentas
    ("Ferramentas que realmente aumentam produtividade dev", ["software", "produtividade"]),
    ("Automatizando tarefas repetitivas com scripts simples", ["automacao", "devops"]),
    ("Git além do básico: hábitos profissionais", ["git", "workflow"]),
    ("Docker na prática: do desenvolvimento ao deploy", ["devops", "infra"]),
    ("VS Code extensions essenciais para 2025", ["software", "produtividade"]),

    # Hardware / Infra
    ("Como hardware impacta performance de aplicações", ["hardware", "performance"]),
    ("SSD vs HDD: impacto real no dia a dia do dev", ["hardware"]),
    ("Quando vale investir em mais RAM", ["hardware", "infra"]),
    ("Cloud vs on-premise: análise de custo real", ["infra", "arquitetura"]),

    # DevOps
    ("Automação com GitHub Actions na prática", ["devops", "automacao"]),
    ("Erros comuns em pipelines CI/CD", ["devops", "ci"]),
    ("Observabilidade: logs, métricas e traces", ["devops", "infra", "engenharia"]),
    ("Kubernetes para quem nunca usou: conceitos essenciais", ["devops", "infra"]),
    ("Infraestrutura como código com Terraform", ["devops", "infra", "automacao"]),
]

content_templates = [
    """\
Este é um post gerado automaticamente sobre **{title}**.

## Contexto

O tema de hoje é relevante para qualquer desenvolvedor que trabalha com tecnologia moderna. À medida que os sistemas crescem em complexidade, entender os trade-offs envolvidos se torna essencial.

## Pontos principais

- Cada decisão técnica carrega consequências diretas na manutenibilidade do sistema
- A escolha certa depende sempre do contexto: tamanho do time, escala esperada e requisitos de negócio
- Documentar decisões é tão importante quanto tomá-las

## Considerações finais

Este projeto demonstra automação de geração de conteúdo com Python e publicação contínua via GitHub Actions e Jekyll.
""",
    """\
Post automático sobre **{title}**.

## Por que isso importa?

No cenário atual de desenvolvimento de software, esse tema aparece com frequência em discussões técnicas — e por boas razões.

## O que você deve saber

1. O contexto sempre supera a teoria: soluções genéricas raramente se aplicam sem adaptação
2. Simplicidade bem aplicada supera complexidade desnecessária
3. Iterar com feedback real é mais valioso do que planejar em excesso

## Conclusão

O objetivo deste blog é explorar temas técnicos de forma prática e direta, com publicação automatizada duas vezes ao dia.
""",
    """\
Hoje o tema é **{title}**.

## Introdução

Profissionais de tecnologia lidam diariamente com escolhas que impactam desde a experiência do usuário até a saúde operacional dos sistemas. Entender os princípios por trás dessas decisões faz diferença.

## Aspectos técnicos relevantes

- **Escalabilidade**: como a solução se comporta sob carga crescente?
- **Manutenibilidade**: o time consegue evoluir o código com segurança?
- **Custo operacional**: o que é necessário para manter isso em produção?

## Próximos passos

Explore os outros posts deste blog para aprofundar seu conhecimento em temas relacionados.
""",
]

today = datetime.now()
date_str = today.strftime("%Y-%m-%d")

choice = random.choice(topics)
post_title = choice[0]
post_tags = choice[1]

tags_formatted = "[" + ", ".join(f'"{tag}"' for tag in post_tags) + "]"
filename = f"_posts/{date_str}-post-{random.randint(1000, 9999)}.md"

body = random.choice(content_templates).format(title=post_title)

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
