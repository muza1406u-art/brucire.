from flask import Flask, render_template

app = Flask(__name__)


def build_brucine_model():
    atoms = [
        {"id": "C1", "x": 0.0, "y": 0.0, "z": 0.0, "type": "C", "chiral": "S"},
        {"id": "C5", "x": 1.4, "y": 0.8, "z": 0.5, "type": "C", "chiral": "R"},
        {"id": "C6", "x": -1.2, "y": 1.0, "z": 0.3, "type": "C", "chiral": "S"},
        {"id": "C7", "x": 0.4, "y": -1.3, "z": 1.0, "type": "C", "chiral": "S"},
        {"id": "C9", "x": 2.2, "y": 1.2, "z": 0.9, "type": "C", "chiral": "R"},
        {"id": "C10", "x": -2.0, "y": 1.7, "z": 0.7, "type": "C", "chiral": "R"},
        {"id": "C11", "x": 1.1, "y": -2.1, "z": 1.8, "type": "C", "chiral": "S"},
        {"id": "O", "x": 0.2, "y": 0.2, "z": -1.6, "type": "O", "chiral": ""},
        {"id": "N1", "x": -0.9, "y": 2.0, "z": -0.2, "type": "N", "chiral": ""},
        {"id": "N2", "x": 0.5, "y": -2.4, "z": 0.1, "type": "N", "chiral": ""},
    ]

    bonds = [(0, 1), (0, 2), (0, 3), (0, 7), (1, 4), (2, 5), (3, 6), (2, 8), (3, 9)]
    return atoms, bonds


def atom_color(atom_type, chiral):
    if chiral:
        return "#facc15"
    if atom_type == "O":
        return "#f87171"
    if atom_type == "N":
        return "#a78bfa"
    return "#60a5fa"


def render_2d_svg(atoms, bonds, width=720, height=360):
    scale = 85
    ox, oy = width / 2, height / 2

    def p(a):
        return ox + a["x"] * scale, oy - a["y"] * scale

    lines = [
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="2D Brucine structure">',
        f'<rect width="{width}" height="{height}" rx="14" fill="#0b1220"/>',
    ]

    for i, j in bonds:
        x1, y1 = p(atoms[i])
        x2, y2 = p(atoms[j])
        lines.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#93c5fd" stroke-width="3"/>')

    for atom in atoms:
        x, y = p(atom)
        color = atom_color(atom["type"], atom["chiral"])
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="10" fill="{color}"/>')
        label = atom["id"] if not atom["chiral"] else f'{atom["id"]}({atom["chiral"]})'
        lines.append(f'<text x="{x + 12:.1f}" y="{y - 12:.1f}" font-size="13" fill="#e2e8f0">{label}</text>')

    lines.append('<text x="20" y="30" fill="#22d3ee" font-size="18">Brucine 2D structure (educational schematic)</text>')
    lines.append('</svg>')
    return "".join(lines)


def render_3d_svg(atoms, bonds, width=720, height=400):
    ox, oy, scale = width / 2, height / 2 + 10, 95

    projected = []
    for atom in atoms:
        px = ox + (atom["x"] - atom["z"] * 0.6) * scale
        py = oy - (atom["y"] + atom["z"] * 0.45) * scale
        projected.append((atom, px, py, atom["z"]))

    lines = [
        f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="3D Brucine projection">',
        f'<rect width="{width}" height="{height}" rx="14" fill="#020617"/>',
    ]

    for i, j in bonds:
        ai, aj = projected[i], projected[j]
        x1, y1 = ai[1], ai[2]
        x2, y2 = aj[1], aj[2]
        lines.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#cbd5e1" stroke-width="3" opacity="0.75"/>')

    for atom, x, y, z in sorted(projected, key=lambda t: t[3]):
        radius = 8 + (z + 2.5) * 1.6
        color = atom_color(atom["type"], atom["chiral"])
        lines.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" fill="{color}"/>')
        lines.append(f'<text x="{x + 10:.1f}" y="{y - 10:.1f}" font-size="12" fill="#e2e8f0">{atom["id"]}</text>')

    lines.append('<text x="20" y="32" fill="#22d3ee" font-size="18">Brucine 3D structure (Python isometric projection)</text>')
    lines.append('</svg>')
    return "".join(lines)


@app.route('/')
def home():
    atoms, bonds = build_brucine_model()

    brucine_data = {
        "name": "Brucine",
        "molecular_formula": "C23H26N2O4",
        "chiral_center_count": 7,
        "rs_configuration": ["C1: S", "C5: R", "C6: S", "C7: S", "C9: R", "C10: R", "C11: S"],
    }

    student = {
        "name": "Nalla Hari Hara Krishna",
        "roll_no": "RA2511026050036",
        "dept": "CSE-AIML",
        "section": "A",
    }

    return render_template(
        'index.html',
        brucine=brucine_data,
        student=student,
        svg_2d=render_2d_svg(atoms, bonds),
        svg_3d=render_3d_svg(atoms, bonds),
    )


if __name__ == '__main__':
    app.run(debug=True)
