# Motion Pipeline

## Objetivo

Construir o pipeline de deteccao e tracking que gera sinais de controle estaveis.

## Inputs

- Dataset minimo ou videos de teste
- Criterios de movimentos relevantes

## Steps

1. Definir abordagem de tracking (optical flow, pose, hand, pontos).
2. Implementar deteccao base e extrair sinais.
3. Normalizar sinais (escala, offsets).
4. Aplicar smoothing temporal.
5. Medir taxa de falhas e ajustar parametros.

## Outputs

- Codigo do pipeline de tracking
- Especificacao de sinais gerados
- Parametros recomendados

## Acceptance

- Sinais consistentes em 80%+ dos frames
- Smoothing reduz jitter perceptivel
- Documentacao de parametros pronta
