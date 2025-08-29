from manim import *
import random

class GrafoScene(Scene):
    def construct(self):

        # -------------------
        # TÍTULO INICIAL
        # -------------------
        titulo1 = Text(
            "Una Introducción (Muy algorítmica)",
            font="Palatino Linotype",
            font_size=56,
            color=BLUE_C
        ).move_to(UP*0.5)

        titulo2 = Text(
            "a la Teoría de grafos",
            font="Palatino Linotype",
            font_size=56,
            color=BLUE_C
        ).next_to(titulo1, DOWN, buff=0.4)

        titulo = VGroup(titulo1, titulo2)

        # Mostrar título
        self.play(FadeIn(titulo, scale=1.2), run_time=2)

        # -------------------
        # DIVERSIDAD DE GRAFOS
        # -------------------
        ejemplos = [
            # Triángulo
            (["A","B","C"], [("A","B"),("B","C"),("C","A")]),
            # Cuadrado
            (["1","2","3","4"], [("1","2"),("2","3"),("3","4"),("4","1")]),
            # Camino
            (["u","v","w","x"], [("u","v"),("v","w"),("w","x")]),
            # Estrella
            (["p","q","r","s","t"], [("p","q"),("p","r"),("p","s"),("p","t")]),
            # Ciclo de 5
            (list("abcde"), [("a","b"),("b","c"),("c","d"),("d","e"),("e","a")]),
            # Grafo completo K4
            (list("wxyz"), [("w","x"),("w","y"),("w","z"),("x","y"),("x","z"),("y","z")]),
            # Bipartito simple
            (["a1","a2","b1","b2"], [("a1","b1"),("a1","b2"),("a2","b1"),("a2","b2")]),
            # Árbol pequeño
            (["r","a","b","c"], [("r","a"),("r","b"),("b","c")]),
        ]

        grafos = VGroup()
        for _ in range(75):  # cantidad de grafos de fondo
            nodes, edges = random.choice(ejemplos)

            x = random.uniform(-6, 6)
            y = random.uniform(-3.5, 3.5)

            g = Graph(
                nodes, edges,
                layout="spring",
                vertex_config={"radius": 0.05, "fill_color": GREY},
                edge_config={"stroke_width": 0.8, "stroke_color": GREY},
            ).scale(0.5).move_to([x, y, 0])

            grafos.add(g)

        # Animación aparición rápida en mosaico
        self.play(LaggedStart(*[FadeIn(g) for g in grafos], lag_ratio=0.02, run_time=3))
        
        autores = Text(
            "Por Jerónimo Hoyos Botero y Daniel Fernando Verdecia Goyeneche",
            font="Palatino Linotype",
            font_size=30,
            color=WHITE
        ).next_to(titulo1, DOWN, buff=3)
        
        self.play(FadeIn(autores, scale=1.2), run_time=2)

        self.wait(2)


        self.play(FadeOut(VGroup(titulo, grafos, autores)), run_time=2)

        # -------------------
        # Grafo
        # ------------------- 

        texto1 = Text(
            "¿Puedes dibujar sin levantar el lapiz?",
            font="Palatino Linotype",
            font_size=40,
            color=WHITE
        ).move_to(UP*3)

        self.play(FadeIn(texto1, scale=1.2), run_time=2)

        vertices = ["A", "B", "C", "D", "E"]

        edges = [
            ("A", "B"), ("A", "C"), 
            ("B", "C"),              
            ("B", "D"), ("C", "E"), 
            ("D", "E"),              
            ("B", "E"), ("C", "D")   
        ]

        layout = {
            "A": [0, 2, 0],   
            "B": [-3, 0, 0],
            "C": [3, 0, 0],
            "D": [-3, -3, 0],
            "E": [3, -3, 0],
        }

        g = Graph(
            vertices,
            edges,
            layout=layout,
            labels=True,
            vertex_config={"radius": 0.4, "fill_color": BLUE_C},
            edge_config={"stroke_width": 3},
        )

    
        vertices_mobs = VGroup(*[g[v] for v in g.vertices])


        self.play(FadeIn(vertices_mobs), run_time=1.5)


        for e in edges:
            self.play(FadeIn(g.edges[e]), run_time=0.7)

        self.wait(2)
