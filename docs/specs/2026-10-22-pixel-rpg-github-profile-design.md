# Pixel RPG Character Sheet — GitHub Profile Design Document

**Tanggal:** 2026-10-22  
**Status:** In Review  
**Target File:** `README.md`, `assets/rpg-status-card.svg`, `assets/pixel-divider.svg`

---

## 1. Ringkasan Proyek
Membangun tampilan GitHub Profile README untuk Muhammad Hadid Wiransetyo (`hadidwirsty`) dengan tema **Retro RPG Character Sheet 16-bit** yang selaras dengan foto profil pixel art pengguna. Desain memadukan identitas profesional sebagai *Full-Stack Software Engineer* (Go, TypeScript, React) dengan identitas personal sebagai *Endurance Athlete / Marathoner*.

---

## 2. Tujuan & Kriteria Sukses
- [ ] Menghasilkan tampilan profil yang imersif bertema game RPG retro 16-bit.
- [ ] Menyediakan aset visual SVG kustom (`rpg-status-card.svg` & `pixel-divider.svg`) yang tajam, ringan, dan kompatibel dengan GitHub Dark & Light Mode.
- [ ] Menampilkan *Vitals* (HP, MP, Stamina, EXP) dan *Attributes* (INT, DEX, VIT, WIS) yang seimbang antara engineering dan running endurance.
- [ ] Mengelompokkan Tech Stack sebagai *Inventory Equipment*.
- [ ] Menampilkan *Quest Log* untuk repositori unggulan (`intervals-icu-mcp`, project Transjakarta Fleet Management, dll).
- [ ] Mengintegrasikan GitHub Stats dan Streak cards dengan palet retro yang harmonis.
- [ ] Memberikan tautan kontak (LinkedIn, lokasi) dengan aksen retro RPG.

---

## 3. Komponen Desain & Arsitektur

### 3.1. Banner & Typing Header
- Menampilkan teks retro animasi dengan pesan dinamis:
  - *"Welcome, Adventurer! I'm Muhammad Hadid Wiransetyo."*
  - *"Full-Stack Software Engineer & Endurance Runner."*
  - *"Level 2X Adventurer exploring distributed systems & marathon miles."*

### 3.2. Custom SVG: RPG Character Status Card (`assets/rpg-status-card.svg`)
- Kartu berbingkai pixel 16-bit dengan palet `#0d1117`, aksen border `#30363d` & `#238636`.
- **Player Info:**
  - Name: `MUHAMMAD HADID WIRANSETYO`
  - Class: `Full-Stack Architect`
  - Sub-Class: `Endurance Runner`
  - Origin / Guild: `Semarang & Yogyakarta, ID`
- **Health / Resource Bars:**
  - `HP` (Coding Energy): `100 / 100` [Hijau Pixel Bar]
  - `MP` (Problem Solving): `99 / 99` [Biru Pixel Bar]
  - `STM` (Marathon Distance): `42.195 km` [Kuning Emas Bar]
  - `EXP` (XP to Next Level): `88%` [Ungu Pixel Bar]
- **Stats Matrix:**
  - `INT` : +95 (Backend Engineering: Go, Node.js, Distributed Architecture)
  - `DEX` : +90 (Frontend Craftsmanship: React, TypeScript, Responsive UI)
  - `VIT` : +99 (Endurance & Discipline: Marathon Grit, Consistent Routine)
  - `WIS` : +88 (System Quality: TDD, Clean Architecture, MCP Tooling)

### 3.3. Custom SVG: Pixel Art Dividers (`assets/pixel-divider.svg`)
- Pembatas segmen bernuansa 8-bit / 16-bit (pixel coins, pixel hearts, atau retro dashed bars).

### 3.4. Inventory & Equipment Slots (Tech Stack)
- **Main Weapon (Backend Core):** Go, TypeScript, Node.js
- **Secondary Gear (Frontend):** React, Next.js, Tailwind CSS, Vite
- **Storage & Relics (Databases & DevOps):** PostgreSQL, Redis, Docker, Git, Linux
- **Enchantments (Specialties):** Model Context Protocol (MCP), Intervals.icu API, Telemetry Systems

### 3.5. Active Quests (Featured Repositories)
- Repositori kunci ditampilkan dalam format Quest Log dengan ikon status kustom:
  - 🛡️ **`intervals-icu-mcp`** — MCP Server menghubungkan AI dengan platform analisis olahraga Intervals.icu.
  - 🚌 **`frontend-assessment-tj-hadid` & `backend-assessment-tj-hadid`** — Sistem monitoring armada Transjakarta (Go & React).
  - ⚡ **`hiblow-fleet` & `node-backend-mastery`** — Skalabilitas backend & arsitektur telemetri.

### 3.6. Dynamic Battle Records (GitHub Stats)
- Integrasi `github-readme-stats` & `streak-stats` dengan tema custom yang selaras dengan palet retro GitHub (`theme=tokyonight` atau custom palette retro green & dark navy).

### 3.7. Tavern & Guild Hall (Contact Information)
- Tautan LinkedIn, GitHub profile, dan lokasi dengan badge pixel yang rapi.

---

## 4. Struktur File Proyek
```
hadidwirsty/
├── assets/
│   ├── rpg-status-card.svg
│   └── pixel-divider.svg
├── docs/
│   └── specs/
│       └── 2026-10-22-pixel-rpg-github-profile-design.md
└── README.md
```

---

## 5. Rencana Pengujian & Verifikasi
- [ ] Validasi rendering SVG di Dark Mode dan Light Mode pada GitHub.
- [ ] Uji responsivitas kartu SVG pada layar desktop dan mobile.
- [ ] Verifikasi semua tautan (repositori, profil LinkedIn, badge) mengarah ke URL yang valid dan aktif.
- [ ] Pastikan tidak ada tautan rusak atau gambar yang gagal dimuat.
