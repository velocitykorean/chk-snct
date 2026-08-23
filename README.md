# Chakra Healing YouTube Automation Bot 🧘✨🔮

A specialized, fully automated production pipeline for YouTube **Chakra Healing, Solfeggio Frequencies & Spiritual Meditation** channels.

---

## 🌟 Channel Identity & Unique Channel Names

Here are the top suggested brand names for this YouTube channel:

1. **ChakraSanctum** *(Recommended Default)* — Pure, authoritative sanctuary for 7 chakras alignment & meditation.
2. **PranaResonance** — Focuses on cosmic life-force energy (Prana) and healing sound frequencies.
3. **AuraHarmonics** — Highlighting aura cleansing, Solfeggio sound baths & spiritual vibration.
4. **GoldenPrana** — Echoes the golden meditating figure, divine light & higher consciousness.
5. **AnandaChakra** — Rooted in Sanskrit bliss (*Ananda*) and deep energy balancing.

---

## 📁 Architecture Overview

```
Chakra healing/
├── .env                       # Environment configuration & Google Drive folder IDs
├── .env.example               # Configuration template
├── google_drive_fetch.py      # Downloads Video, Audio, Image triplets from Google Drive
├── thumbnail_generator.py     # Generates mystical, high-CTR 1280x720 Chakra thumbnails
├── video_generator.py         # 1080p Lanczos upscale, ping-pong seamless loops & audio sync
├── auto_pipeline.py           # Master end-to-end automation orchestrator
├── generate_chakra_videos.py  # Standalone CLI video renderer
├── publish_youtube.py         # YouTube Data API upload & thumbnail publishing module
├── published_videos.json      # Publication history tracking
├── input_videos/              # Meditating figure loops (Golden_figure_meditating_in_forest_202608231116.mp4)
├── input_audio/               # Spiritual & Solfeggio audio tracks (Golden Resonance.mp3)
├── input_images/              # Thumbnail background frames
├── output_thumbnails/         # Generated YouTube thumbnails (1280x720)
└── output_videos/             # Rendered 1080p full-length videos (1 Hour)
```

---

## ⚙️ Configuration (`.env`)

Add your Google Drive Folder IDs in `.env`:

```env
# Google Drive Folder IDs
GOOGLE_DRIVE_VIDEO_FOLDER_ID=your_video_folder_id
GOOGLE_DRIVE_AUDIO_FOLDER_ID=your_audio_folder_id
GOOGLE_DRIVE_IMAGE_FOLDER_ID=your_image_folder_id

# Google Service Account Key
GOOGLE_SERVICE_ACCOUNT_KEY=service_account.json

# Channel Identity
CHANNEL_NAME=ChakraSanctum
DEFAULT_DURATION=3600
ALLOW_REPOST=true
```

> **Note:** Share each of your 3 Google Drive folders with the Service Account email found in `service_account.json` with **Viewer** access.

---

## 🚀 Usage Commands

### 1. Run Complete Automation Pipeline (1-Hour Video)
```powershell
python auto_pipeline.py --duration 3600
```

### 2. Run Preview Test (5-Minute Video Dry-Run)
```powershell
python auto_pipeline.py --duration 300 --dry-run
```

### 3. Generate Thumbnail Only
```powershell
python thumbnail_generator.py
```

### 4. Standalone Video Render
```powershell
python generate_chakra_videos.py --duration 3600
```

---

## ✨ Features

- **High-Fidelity 1080p Upscaling:** Auto-upscales 720p inputs to 1920x1080 Full HD with Lanczos & Unsharp filters.
- **Zero-Jump Ping-Pong Looping:** Forward + Reverse stitching guarantees seamless continuous visual flow for 1+ hours.
- **Solfeggio & Chakra SEO:** Generates titles, tags, and complete 7 Chakra descriptions (Root to Crown) with frequency breakdowns (396Hz–963Hz).
- **GPU Acceleration:** Auto-detects NVIDIA NVENC (`h264_nvenc`) with CPU fallback (`libx264`).
