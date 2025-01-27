from tkinter import messagebox
import svgpathtools
from svgpathtools import svg2paths2
import math

def calculate_scale_and_offset(svg_file, target_width, target_height):
    #Oblicza skalę i przesunięcie, aby zmieścić SVG w określonym rozmiarze.
    _, _, svg_attributes = svg2paths2(svg_file)
    viewBox = svg_attributes.get("viewBox")
    if viewBox:
        # Zamień przecinki na spacje, jeśli istnieją
        viewBox = viewBox.replace(',', ' ')
        x_min, y_min, original_width, original_height = map(float, viewBox.split())

        # Oblicz skalę dla szerokości i wysokości
        scale_x = target_width / original_width
        scale_y = target_height / original_height
        scale = min(scale_x, scale_y)  # Używamy mniejszej skali, aby zmieścić całość

        # Przesunięcie do (0, 0)
        offset_x = -x_min * scale
        offset_y = -y_min * scale

        return scale, offset_x, offset_y
    else:
        raise ValueError("Plik SVG nie zawiera informacji o wymiarach (viewBox).")



def svg_to_gcode(svg_file, output_file, target_width=210, target_height=297):
    # Odczytaj ścieżki z pliku SVG
    paths, _, _ = svg2paths2(svg_file)

    # Oblicz skalę i przesunięcie
    scale, offset_x, offset_y = calculate_scale_and_offset(svg_file, target_width, target_height)

    # Debug: Wyświetl skalę i przesunięcia
    print(f"Skala: {scale}, Offset X: {offset_x}, Offset Y: {offset_y}")

    # Otwórz plik wynikowy
    with open(output_file, 'w') as gcode:
        # Inicjalizacja G-code
        gcode.write("G21 ; Set units to mm\n")  # Jednostki w milimetrach
        gcode.write("G90 ; Absolute positioning\n")  # Pozycjonowanie bezwzględne

        # Zmienna do kontrolowania, czy mamy do czynienia z nowym słowem
        is_new_word = True

        # Przetwarzaj każdą ścieżkę w SVG (każda ścieżka traktowana jako osobne słowo)
        for path in paths:
            # Sprawdzenie, czy zaczynamy nowe słowo (każda ścieżka to osobne słowo)
            if is_new_word:
                gcode.write("G1 Z10 ; Podnieś pióro\n")  # Podnieś pióro przed nowym słowem

            # Ustawienie flagi na False, aby nie podnosić pióra w obrębie tego samego słowa
            is_new_word = False

            # Przetwarzanie segmentów w ścieżce
            for segment in path:
                # Jeżeli to jest linia
                if isinstance(segment, svgpathtools.Line):
                    start = segment.start
                    end = segment.end

                    start_x = start.real * scale + offset_x
                    start_y = target_height - (start.imag * scale + offset_y)
                    end_x = end.real * scale + offset_x
                    end_y = target_height - (end.imag * scale + offset_y)

                    # Jeżeli przechodzimy do nowej ścieżki (nowe słowo), podnieś pióro
                    gcode.write(f"G1 X{start_x:.3f} Y{start_y:.3f} F1000\n")
                    gcode.write(f"G1 X{end_x:.3f} Y{end_y:.3f} F1000\n")

                # Jeśli to jest krzywa
                elif isinstance(segment, svgpathtools.CubicBezier) or isinstance(segment, svgpathtools.QuadraticBezier):
                    points = approximate_curve(segment, num_points=20)
                    for point in points:
                        x = point[0] * scale + offset_x
                        y = target_height - (point[1] * scale + offset_y)

                        # Jeśli przechodzimy do nowego słowa, podnieś pióro
                        gcode.write(f"G1 X{x:.3f} Y{y:.3f} F1000\n")

            # Po każdej ścieżce (słowie) ustalamy, że następne słowo będzie traktowane osobno
            is_new_word = True

        # Kończymy program
        gcode.write("G1 Z10 ; Podnieś pióro\n")  # Upewnij się, że po zakończeniu rysowania pióro jest podniesione
        gcode.write("M02 ; End program\n")
    messagebox.showinfo("Success", "Translated to gcode!")




def approximate_curve(segment, num_points=20):
    """Funkcja aproksymująca krzywe za pomocą prostych odcinków (używane dla krzywych Beziera)."""
    points = []
    for i in range(num_points + 1):
        t = i / num_points
        point = segment.point(t)
        points.append((point.real, point.imag))
    return points

def start():
    svg_to_gcode('img/output.svg', 'gcode/output.gcode')


