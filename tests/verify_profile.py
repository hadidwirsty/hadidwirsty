import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def test_pixel_divider():
    path = Path("assets/pixel-divider.svg")
    assert path.exists(), "assets/pixel-divider.svg does not exist"
    tree = ET.parse(path)
    root = tree.getroot()
    assert "svg" in root.tag.lower(), "Root element must be <svg>"
    # Check width/height/viewBox
    assert "viewBox" in root.attrib or ("width" in root.attrib and "height" in root.attrib), "Must have viewBox or dimensions"

def test_rpg_status_card():
    path = Path("assets/rpg-status-card.svg")
    assert path.exists(), "assets/rpg-status-card.svg does not exist"
    content = path.read_text(encoding="utf-8")
    tree = ET.parse(path)
    root = tree.getroot()
    assert "svg" in root.tag.lower(), "Root element must be <svg>"
    
    # Required RPG elements
    required_keywords = [
        "MUHAMMAD HADID WIRANSETYO",
        "Frontend Architect",
        "Endurance Runner",
        "HP", "MP", "STM", "EXP",
        "INT", "DEX", "VIT", "WIS"
    ]
    for kw in required_keywords:
        assert kw in content, f"Missing required RPG keyword: {kw}"

def test_readme_structure():
    path = Path("README.md")
    assert path.exists(), "README.md does not exist"
    content = path.read_text(encoding="utf-8")
    
    sections = [
        "assets/rpg-status-card.svg",
        "assets/pixel-divider.svg",
        "inventory",
        "quest",
        "intervals-icu-mcp",
        "linkedin.com/in/hadidwirsty"
    ]
    for sec in sections:
        assert sec.lower() in content.lower(), f"Missing section/link in README: {sec}"

if __name__ == "__main__":
    tests = [test_pixel_divider, test_rpg_status_card, test_readme_structure]
    results = {}
    for t in tests:
        try:
            t()
            results[t.__name__] = "PASS"
            print(f"PASS: {t.__name__}")
        except AssertionError as e:
            results[t.__name__] = f"FAIL: {e}"
            print(f"FAIL: {t.__name__} -> {e}")
        except Exception as e:
            results[t.__name__] = f"ERROR: {e}"
            print(f"ERROR: {t.__name__} -> {e}")
    
    failed = [k for k, v in results.items() if not v.startswith("PASS")]
    if failed:
        sys.exit(1)
    else:
        sys.exit(0)
