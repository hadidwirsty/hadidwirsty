# Pixel RPG Character Sheet — GitHub Profile Implementation Plan

**Tanggal:** 2026-10-22  
**Dokumen Spesifikasi:** `docs/specs/2026-10-22-pixel-rpg-github-profile-design.md`  
**Sequence:** 1  
**Status:** Completed  
**Hasil Verifikasi:** Semua test lulus (3/3 PASS, xmllint valid)  

---

## Ringkasan Eksekutif
Rencana kerja implementasi untuk mengubah profil GitHub `hadidwirsty` menjadi **Retro RPG Character Sheet 16-bit**. Terdiri dari 5 tugas teknis atomik berbasis TDD dengan pembuatan script verifikasi otomatis menggunakan Python untuk memvalidasi sintaks SVG, integritas elemen RPG, dan struktur Markdown `README.md`.

---

## Pre-Execution & Compliance Checklist
- [x] Sesuai dengan `.agents/skills/technical-constitution/SKILL.md` (Keamanan konten, tanpa secret, validasi I/O).
- [x] Sesuai dengan `.agents/skills/clean-code-standards/SKILL.md` (Format standar, penamaan semantik).
- [x] Sesuai dengan `.agents/skills/test-driven-development/SKILL.md` (Siklus Red-Green-Refactor di setiap tugas).
- [x] Bahasa dokumentasi percakapan dan status wajib Bahasa Indonesia.

---

## Rincian Tugas Atomik

### Task 1: Test Harness & Verification Script

**Files:**
- Create: `tests/verify_profile.py`

**Requirements:**
- **Acceptance Criteria**
  1. Script verifikasi dapat memeriksa keabsahan XML file SVG (`assets/pixel-divider.svg` dan `assets/rpg-status-card.svg`).
  2. Script memeriksa keberadaan elemen wajib kartu status RPG (Nama, Class, Sub-Class, Vitals HP/MP/STM/EXP, Attributes INT/DEX/VIT/WIS).
  3. Script memvalidasi keberadaan dan struktur berkas `README.md` (Typing header, embed aset lokal, Inventory, Quests, Stats, Tavern contact).
- **Functional Requirements**
  1. Menggunakan library bawaan Python 3 (`xml.etree.ElementTree`, `re`, `pathlib`) tanpa dependensi eksternal.
  2. Menghasilkan exit code 0 jika seluruh kriteria terpenuhi dan non-zero jika gagal.
- **Non-Functional Requirements**
  1. Eksekusi cepat (< 1 detik).
- **Test Coverage**
  - [Unit] `test_pixel_divider_svg()`: Memeriksa keberadaan file dan keabsahan XML SVG.
  - [Unit] `test_rpg_status_card_svg()`: Memeriksa validitas XML, dimensi, dan konten teks RPG.
  - [Unit] `test_readme_structure()`: Memeriksa section mandatory dan link aset di `README.md`.

**Step 1: Write failing test (RED)**
Tulis skrip uji `tests/verify_profile.py`:
```python
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def test_pixel_divider():
    path = Path("assets/pixel-divider.svg")
    assert path.exists(), "assets/pixel-divider.svg does not exist"
    tree = ET.parse(path)
    root = tree.getroot()
    assert "svg" in root.tag.lower(), "Root element must be <svg>"

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
        "Full-Stack Architect",
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
        "Inventory",
        "Quest",
        "intervals-icu-mcp",
        "linkedin.com/in/hadidwirsty"
    ]
    for sec in sections:
        assert sec in content, f"Missing section/link in README: {sec}"

if __name__ == "__main__":
    tests = [test_pixel_divider, test_rpg_status_card, test_readme_structure]
    failed = False
    for t in tests:
        try:
            t()
            print(f"PASS: {t.__name__}")
        except AssertionError as e:
            print(f"FAIL: {t.__name__} -> {e}")
            failed = True
        except Exception as e:
            print(f"ERROR: {t.__name__} -> {e}")
            failed = True
    sys.exit(1 if failed else 0)
```

**Step 2: Verify test fails**
Run: `python3 tests/verify_profile.py`  
Expected: FAIL dengan `assets/pixel-divider.svg does not exist` (exit code 1).

**Step 3: Minimal implementation (GREEN)**
Buat file `tests/verify_profile.py` dan pastikan runner uji siap.

**Step 4: Verify test passes & Refactor**
Run: `python3 tests/verify_profile.py`  
Expected: Memastikan output fail terdeteksi dengan benar sebelum aset dibuat.

---

### Task 2: Create Custom Pixel Art Divider (`assets/pixel-divider.svg`)

**Files:**
- Create: `assets/pixel-divider.svg`
- Test: `tests/verify_profile.py`

**Requirements:**
- **Acceptance Criteria**
  1. File `assets/pixel-divider.svg` dibuat dengan format SVG valid.
  2. Menampilkan garis hiasan pixel 16-bit (berpola pixel hearts, pixel diamonds, atau pixel bars dengan nuansa hijau GitHub & retro gold).
  3. Memiliki atribut `viewBox="0 0 800 24"` dan mendukung skala lebar 100% responsif.
- **Functional Requirements**
  1. Render grafis SVG berbasis `rect` pixelated untuk ketajaman visual maksimal.
- **Non-Functional Requirements**
  1. Ukuran file ringan (< 5 KB).
- **Test Coverage**
  - `test_pixel_divider()` in `tests/verify_profile.py` passes.

**Step 1: Write failing test (RED)**
Jalankan uji `python3 tests/verify_profile.py`. Target fungsi `test_pixel_divider`.

**Step 2: Verify test fails**
Output: `FAIL: test_pixel_divider -> assets/pixel-divider.svg does not exist`.

**Step 3: Write minimal implementation (GREEN)**
Buat `assets/pixel-divider.svg` dengan grafis pixel bar & diamond retro.

**Step 4: Verify test passes & Refactor**
Run: `python3 -c "import xml.etree.ElementTree as ET; ET.parse('assets/pixel-divider.svg'); print('OK')"`  
Expected: `OK`.

---

### Task 3: Create Custom 16-bit RPG Character Status Card (`assets/rpg-status-card.svg`)

**Files:**
- Create: `assets/rpg-status-card.svg`
- Test: `tests/verify_profile.py`

**Requirements:**
- **Acceptance Criteria**
  1. File `assets/rpg-status-card.svg` berformat XML valid dengan viewBox `0 0 840 460`.
  2. Frame luar bergaya pixel bevel box klasik 16-bit (`#0d1117`, border `#30363d`, aksen `#238636` & `#58a6ff`).
  3. Header memuat nama `MUHAMMAD HADID WIRANSETYO`, Class `Full-Stack Architect`, Sub-Class `Endurance Runner`, Guild `Semarang & Yogyakarta, ID`.
  4. 4 Resource Bars bergaya pixel segmented:
     - `HP` (Coding Energy): 100/100 (Warna hijau emerald `#2ea043`)
     - `MP` (Problem Solving): 99/99 (Warna biru mana `#388bfd`)
     - `STM` (Marathon Distance): 42.195 km (Warna kuning emas `#d29922`)
     - `EXP` (XP to Next Level): 88% (Warna ungu magis `#a371f7`)
  5. Attributes Grid:
     - `INT` : +95 (Backend Engineering: Go, Node.js, Distributed Systems)
     - `DEX` : +90 (Frontend Craftsmanship: React, TypeScript, UI Precision)
     - `VIT` : +99 (Endurance & Discipline: Marathon Grit, Daily Consistency)
     - `WIS` : +88 (System Architecture: TDD, Clean Code, MCP Tooling)
- **Functional Requirements**
  1. Menggunakan font stack monospace sistem / pixel retro (`ui-monospace, SFMono-Regular, "Courier New", monospace`).
  2. Kompatibel pada tema gelap (dark background) dan tidak tembus pandang di light background.
- **Test Coverage**
  - `test_rpg_status_card()` in `tests/verify_profile.py` passes.

**Step 1: Write failing test (RED)**
Jalankan uji `python3 tests/verify_profile.py`. Target fungsi `test_rpg_status_card`.

**Step 2: Verify test fails**
Output: `FAIL: test_rpg_status_card -> assets/rpg-status-card.svg does not exist`.

**Step 3: Write minimal implementation (GREEN)**
Buat file `assets/rpg-status-card.svg` dengan seluruh komponen visual RPG yang disyaratkan.

**Step 4: Verify test passes & Refactor**
Run: `python3 tests/verify_profile.py`  
Expected: `test_rpg_status_card` menghasilkan `PASS`.

---

### Task 4: Compose the Complete GitHub Profile `README.md`

**Files:**
- Create: `README.md`
- Test: `tests/verify_profile.py`

**Requirements:**
- **Acceptance Criteria**
  1. Header menyertakan banner retro dinamis dari `readme-typing-svg` dengan font monospace & teks selamat datang petualang.
  2. Embed `assets/rpg-status-card.svg` dan `assets/pixel-divider.svg` berada di posisi tengah (*centered*).
  3. Bagian **Inventory & Equipment** mengelompokkan tech stack (Go, TypeScript, Node.js, React, Next.js, Tailwind, Docker, Postgres, MCP) menggunakan badge berpenampilan bersih dan terorganisir.
  4. Bagian **Active Quests** menampilkan link dan deskripsi proyek unggulan: `intervals-icu-mcp`, project Transjakarta Fleet Management (`frontend-assessment-tj-hadid` & `backend-assessment-tj-hadid`), serta `node-backend-mastery`.
  5. Bagian **Battle Records** menyematkan kartu dynamic GitHub Stats & Streak Stats dengan tema gelap retro (misal: `tokyonight` / custom palette yang serasi).
  6. Bagian **Tavern & Guild Hall** menyediakan tautan kontak LinkedIn dan lokasi.
- **Functional Requirements**
  1. Seluruh link markdown mengarah ke URL yang valid tanpa broken syntax.
- **Test Coverage**
  - `test_readme_structure()` in `tests/verify_profile.py` passes.

**Step 1: Write failing test (RED)**
Jalankan `python3 tests/verify_profile.py`.

**Step 2: Verify test fails**
Output: `FAIL: test_readme_structure -> README.md does not exist`.

**Step 3: Write minimal implementation (GREEN)**
Tulis file `README.md` secara lengkap.

**Step 4: Verify test passes & Refactor**
Run: `python3 tests/verify_profile.py`  
Expected: Seluruh test suite (3/3) menghasilkan `PASS` dengan exit code 0.

---

### Task 5: End-to-End Visual & Syntax Verification

**Files:**
- Read & Validate: `assets/rpg-status-card.svg`, `assets/pixel-divider.svg`, `README.md`

**Requirements:**
- **Acceptance Criteria**
  1. Jalankan `xmllint` pada semua file SVG untuk menjamin keabsahan XML standar.
  2. Periksa rendering dan kontras warna pada background gelap dan terang.
  3. Lakukan verifikasi menyeluruh terhadap kelengkapan profile.

**Verification Command:**
```bash
xmllint --noout assets/*.svg && python3 tests/verify_profile.py
```
Expected: Tidak ada error XML dan semua unit test lulus (exit code 0).

---

## Urutan Eksekusi
1. Task 1: Setup script pengujian `tests/verify_profile.py`.
2. Task 2: Implementasi `assets/pixel-divider.svg`.
3. Task 3: Implementasi `assets/rpg-status-card.svg`.
4. Task 4: Komposisi berkas utama `README.md`.
5. Task 5: Verifikasi akhir end-to-end.
