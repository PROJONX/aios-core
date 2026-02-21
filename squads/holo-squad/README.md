# Holo Squad

Squad para criar um MVP que identifica movimentos em um video e manipula hologramas de graficos ou objetos no proprio video.

## Missao

Entregar um MVP funcional que:
- Detecta movimentos relevantes em um video.
- Converte movimentos em sinais de controle.
- Renderiza hologramas (graficos ou objetos) sincronizados com o movimento.
- Permite ajuste rapido de parametros para demos e testes.

## Escopo do MVP

- Entrada: video gravado ou stream curto.
- Saida: video com hologramas compositados.
- Latencia: tolerancia a near-real-time (nao precisa ser tempo real estrito).
- Foco: prototipo convincente com qualidade visual suficiente para demos.

## Tiers do Squad

- Orchestrator: `holo-orchestrator`
- Tier 0: `product-vision`
- Tier 1: `motion-vision-engineer`, `hologram-compositor`, `realtime-engineer`
- Tier 2: `dataset-annotator`, `qa-benchmarker`

## Agentes

Veja `squads/holo-squad/agents/` para definicoes completas.

## Tarefas Principais

Veja `squads/holo-squad/tasks/`:
- `mvp-brief.md`
- `motion-pipeline.md`
- `hologram-composition.md`
- `integration-demo.md`
- `evaluation-benchmark.md`

## Templates

- `mvp-brief.yaml`
- `experiment-report.md`

## Proximos Passos

1. Rodar `mvp-brief.md` para fechar requisitos do MVP.
2. Implementar pipeline de movimentos (`motion-pipeline.md`).
3. Conectar render holografico e integrar (`hologram-composition.md`, `integration-demo.md`).
4. Medir qualidade e estabilidade (`evaluation-benchmark.md`).
