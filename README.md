---

#  Wolfenstein3D Render Engine Recreation

Este projeto é uma recriação do estilo clássico de renderização 3D usado em *Wolfenstein 3D*, totalmente feito com **Python** e **Pygame**. Ele utiliza **Raycasting** para simular uma perspectiva 3D a partir de um mapa 2D, com renderização de paredes, céu, chão e objetos (*sprites*), oferecendo uma base simples para entender como jogos 3D antigos funcionavam internamente.

---

##  Estrutura do Projeto

```
├── main.py                   # Loop principal do jogo
├── Settings.py              # Configurações gerais (resolução, FOV, etc)
├── map.py                   # Definição e parsing do mapa
├── Raycasting.py            # Lógica de Raycasting para renderizar paredes
├── Object_renderer.py       # Renderiza o fundo e as texturas das paredes
├── sprite_object.py         # Representação dos sprites (ex: hambúrguer)
├── object_handler.py        # Gerencia todos os objetos (sprites) do jogo
├── Resources/
│   └── Textures/            # Texturas das paredes e do céu
│   └── Sprites/             # Imagens dos objetos 2D
```

---

## Como Rodar o Projeto

### Pré-requisitos

* Python 3.10+ recomendado
* Instalar a biblioteca Pygame:

```bash
pip install pygame
```

### Executar

```bash
python main.py
```

---

##  Configurações (Settings.py)

O arquivo `Settings.py` permite personalizar diversos parâmetros do jogo:

| Parâmetro      | Descrição                            |
| -------------- | ------------------------------------ |
| `Resolution`   | Tamanho da janela do jogo            |
| `FPS`          | Frames por segundo                   |
| `player_pos`   | Posição inicial do jogador no mapa   |
| `player_speed` | Velocidade de movimentação           |
| `fov`          | Campo de visão (Field of View)       |
| `num_rays`     | Número de raios usados no Raycasting |
| `max_depth`    | Distância máxima de visão            |

Você pode alterar esses valores para ajustar desempenho, sensação de movimento ou estilo gráfico.

---

## Como Funciona

### Raycasting (Raycasting.py)

A técnica de **raycasting** simula a visão 3D disparando vários "raios" a partir da posição do jogador e verificando onde eles colidem com o mundo (paredes do mapa).

* A cada frame, um feixe de raios é lançado em um ângulo baseado na direção do jogador.
* Para cada raio, são calculadas interseções com linhas horizontais e verticais do mapa.
* A profundidade e o deslocamento da textura são usados para calcular a altura e posição da projeção da parede na tela.
* Um efeito de correção de distorção (removendo *fisheye*) é aplicado.

###  Geração do Mapa (map.py)

O mapa é definido em uma lista 2D (`mini_map`), onde cada número representa uma parede ou espaço vazio.

```python
1 = parede com textura 1
2 = parede com textura 2
False = espaço vazio
```

A classe `Map` converte essa lista em um dicionário de coordenadas reais (`world_map`) que o sistema de raycasting usa para checar colisões.

###  Renderização (Object_renderer.py)

A classe `ObjectRenderer` é responsável por:

* Desenhar o **céu** e o **chão**.
* Renderizar as colunas de parede com base nas informações geradas pelo raycasting.
* Organizar os objetos na tela por profundidade (efeito de *depth sorting*).

### Objetos e Sprites (sprite_object.py & object_handler.py)

Os objetos (como sprites 2D) são calculados com base na distância e ângulo do jogador:

* A classe `SpriteObject` calcula a posição do sprite em relação ao jogador.
* Se o sprite estiver dentro do campo de visão, ele é escalado e desenhado proporcionalmente.
* O `ObjectHandler` instancia e atualiza os sprites presentes no mundo.

---

##  Controles (padrão do Pygame)

* `WASD` ou setas direcionais: movimentação
* `Mouse`: mira
* `ESC`: sair do jogo

---

##  Imagens e Recursos

As texturas de parede estão em:

```
Resources/Textures/
```

E sprites de objeto em:

```
Resources/Sprites/
```

Formatos suportados: `.png`, `.jpg`


## Autor

Projeto criado por [Felipe Gomes Amorim] — Feito com visão ao aprendizado e expansão curricular

---

##  Licença

Este projeto é de código aberto sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---
