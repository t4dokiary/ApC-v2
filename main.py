from core import node # Ejemplo de uso
from core import render
from core import interpolacion
import cv2,os

# Ejemplo de uso
if __name__ == "__main__":
    # Configuración y creación de carpetas
    os.makedirs('img/input', exist_ok=True)
    os.makedirs('img/output', exist_ok=True)

    # Crear lienzo e interpolar puntos
    lienzo = interpolacion.LienzoConInterpolacion("img/input/calle.png", fps=24, segundos=5)
    # Agregar puntos de anclaje
    lienzo.agregar_punto_anclaje(50, 400)
    lienzo.agregar_punto_anclaje(100, 150)
    lienzo.agregar_punto_anclaje(150, 250)
    lienzo.agregar_punto_anclaje(200, 350)
    lienzo.agregar_punto_anclaje(250, 250)
    lienzo.agregar_punto_anclaje(300, 150)
    lienzo.agregar_punto_anclaje(400, 150)
    lienzo.agregar_punto_anclaje(450, 250)
    lienzo.agregar_punto_anclaje(700, 400)
    lienzo.agregar_punto_anclaje(950, 150)
    puntos_interpolados = lienzo.interpolar()

    # Crear nodos y aplicar movimientos
    canvas = cv2.imread("img/input/calle.png", cv2.IMREAD_UNCHANGED)
    personaje = node.NodeImagens("img/input/character.png", (100, 100), scale=0.2)
    patineta = node.NodeImagens("img/input/skateboard.png", (55, 230), scale=0.2, parent=personaje)
    fuego = node.NodeImagens("img/input/fire.png", (170, 100), scale=0.6, parent=personaje)
    personaje.set_position(40, 400)

    for i, (dx, dy) in enumerate(puntos_interpolados):
        node.NodeImagens.clear_canvas(canvas, "img/input/calle.png")
        personaje.set_position(dx, dy)
        fuego.move(3, 1)
        personaje.draw(canvas)
        node.NodeImagens.save_image(canvas, f"img/output/frame_{i:03}.png")
    #lienzo.mostrar_lienzo()
    #lienzo.guardar_lienzo("img/output/lienzo_interpolado.png")
    # valores para la generacion del video
    input_dir = 'img/output/'
    output_file = 'video_salida.avi'
    img_format = 'png'
    output_format = 'avi'
    fps = 24
    # video creado
    renderer = render.VideoRenderer(input_dir, output_file, img_format, output_format, fps)
    renderer.create_video_from_images()