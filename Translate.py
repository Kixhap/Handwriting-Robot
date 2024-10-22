import svgpathtools
from svgpathtools import svg2paths
import math


def svg_to_gcode(svg_file, output_file, scale=1.0):
    # Odczytaj ścieżki z pliku SVG
    paths, _ = svg2paths(svg_file)

    # Otwórz plik wynikowy
    with open(output_file, 'w') as gcode:
        # Inicjalizacja G-code
        gcode.write("G21 ; Set units to mm\n")  # Jednostki w milimetrach
        gcode.write("G90 ; Absolute positioning\n")  # Pozycjonowanie bezwzględne

        # Przetwarzaj kazdą sciezkę w SVG
        for path in paths:
            for segment in path:
                # Jesli to jest linia (Line, Move)
                if isinstance(segment, svgpathtools.Line):
                    start = segment.start
                    end = segment.end

                    # Zapisz ruch G-code dla rysowania linii (linia X,Y w mm, gdzie start i end to wspolrzędne)
                    gcode.write(
                        f"G1 X{start.real * scale:.3f} Y{start.imag * scale:.3f} F1000\n")  # Ruch do punktu startowego
                    gcode.write(
                        f"G1 X{end.real * scale:.3f} Y{end.imag * scale:.3f} F1000\n")  # Narysuj linie do punktu koncowego

                # jesli to jest krzywa (Arc, Bezier Curve)
                elif isinstance(segment, svgpathtools.CubicBezier) or isinstance(segment, svgpathtools.QuadraticBezier):
                    points = approximate_curve(segment, num_points=20)
                    for point in points:
                        gcode.write(f"G1 X{point[0] * scale:.3f} Y{point[1] * scale:.3f} F1000\n")

        gcode.write("G1 Z10 ; Move pen up\n")
        gcode.write("M02 ; End program\n")


def approximate_curve(segment, num_points=20):
    """Funkcja aproksymujaca krzywe za pomoca prostych odcinkow (uzywane dla krzywych Beziera)"""
    points = []
    for i in range(num_points + 1):
        t = i / num_points
        point = segment.point(t)
        points.append((point.real, point.imag))
    return points

def start():
    svg_to_gcode('img\output.svg', 'gcode\output.gcode')
