# Checklist Tecnico do Pipeline (MVP)

## 1) Ingestao de Video
- [ ] Suporta video gravado (arquivo)
- [ ] Suporta live (camera / stream simples)
- [ ] Resolucao configuravel (720p/1080p)
- [ ] FPS configuravel
- [ ] Log de erros de entrada

## 2) Tracking de Maos
- [ ] MediaPipe Hands integrado
- [ ] Sinais normalizados (0..1)
- [ ] Smoothing temporal aplicado
- [ ] Tolerancia a oclusoes leves
- [ ] Export de landmarks para debug

## 3) Tracking de Objeto
- [ ] Inicializacao manual (ROI)
- [ ] Tracking estavel (CSRT ou ORB)
- [ ] Queda detectada e recovery simples
- [ ] Sinais normalizados

## 4) Mapeamento de Sinais
- [ ] Mapeamento posicao -> holograma
- [ ] Mapeamento escala/rotacao
- [ ] Parametros ajustaveis por preset
- [ ] Logs com valores por frame

## 5) Render Holografico
- [ ] Glow + scanlines
- [ ] Blend com video base
- [ ] Preset grafico 2D
- [ ] Preset objeto 3D fake (wireframe/contorno)
- [ ] Camada separada para debug

## 6) Composicao Final
- [ ] Composicao estavel sem flicker
- [ ] Sincronizacao com tracking
- [ ] Export para arquivo
- [ ] Preview em tempo real

## 7) Performance
- [ ] Latencia media por frame <= 150 ms (target)
- [ ] FPS minimo definido para demo
- [ ] Profiling por etapa

## 8) Estabilidade
- [ ] 10 execucoes sem crash
- [ ] 15-20 min sem vazamento de memoria perceptivel
- [ ] Logs de erro claros

## 9) Demo
- [ ] Demo 1: grafico holografico controlado por maos
- [ ] Demo 2: objeto 3D fake controlado por objeto rastreado
- [ ] Roteiro de demo curto (2-3 min)
