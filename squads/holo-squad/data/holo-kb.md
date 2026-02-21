# Holo Squad Knowledge Base

## Dominio

MVP para detectar movimentos em video e controlar hologramas (graficos e objetos) compositados no mesmo video.

## Principios

- Priorizar pipeline simples e observavel.
- Separar deteccao, mapeamento e renderizacao.
- Garantir reproducibilidade e capacidade de demo.

## Heuristicas

- Se a deteccao falha em > 20% dos frames, reduzir complexidade.
- Preferir modelos leves para MVP.
- Evitar dependencias pesadas se nao agregarem melhoria clara.

## Riscos

- Jitter em tracking gera hologramas instaveis.
- Oclusao pode quebrar tracking.
- Performance baixa inviabiliza demo.

## Decisoes Recomendadas

- Usar smoothing temporal simples no MVP.
- Definir area de interesse manual para reduzir ruido.
- Medir latencia por frame em cada etapa.
