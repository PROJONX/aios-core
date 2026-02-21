# MVP Brief

## Summary

- Problem: Mover objetos holograficos em videos gravados e lives usando movimentos de maos/objeto.
- Target User: Times de video/VFX e P&D que precisam de demo funcional rapido.
- Demo Goal: Demo que mostra controle de hologramas (2D e 3D) sincronizados com movimentos.

## Scope

In scope:
- Videos gravados e lives curtos
- Tracking de maos e objetos simples
- Hologramas 2D (graficos) e 3D (objeto)
- Composicao no proprio video

Out of scope:
- Reconstrucao 3D completa do ambiente
- Oclusao perfeita e sombras fisicamente corretas
- Suporte multi-camera e multi-person

## Inputs

- Video Type: Gravado e live
- Hardware Constraints: Intel Core i5 + GPU dedicada

## Pipeline

1. Input
2. Tracking
3. Mapping
4. Render
5. Output

## Success Metrics

- Stability: >= 95% sem crash em 10 execucoes
- Accuracy: >= 80% de tracking estavel em cenas simples
- Latency: <= 150 ms (target). Melhor possivel dentro do hardware
- Visual Quality: >= 4/5 em avaliacao interna

## Risks

- Tracking instavel em oclusoes e movimentos rapidos
- Latencia alta em live com GPU basica
- Composicao inconsistente entre resolucoes
