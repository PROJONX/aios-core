# Holo Squad Prototype

MVP rapido para tracking de maos/objeto e composicao de hologramas em video.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Rodar (video gravado)

```bash
python scripts/run_video.py --input path/to/video.mp4 --output outputs/out.mp4 --mode hand --preset green --glow 0.4 --scanlines 6 --metrics --kalman --k-preset stable
```

## Rodar (live)

```bash
python scripts/run_live.py --camera 0 --mode both --preset blue --glow 0.3 --scanlines 8 --metrics --kalman --k-preset responsive
```

## Gravar live

```bash
python scripts/run_live.py --camera 0 --mode both --preset magenta --glow 0.3 --scanlines 8 --metrics --kalman --k-preset responsive --record outputs/live.mp4
```

## Atalhos no live

- `1` modo hand
- `2` modo object (abre ROI se necessario)
- `3` modo both
- `ESC` sair

## Estrutura

- `pipeline/` Modulos do pipeline (tracking, mapping, render)
- `scripts/` Entradas principais (CLI)
- `assets/` Assets 2D/3D simples
- `outputs/` Saidas geradas
