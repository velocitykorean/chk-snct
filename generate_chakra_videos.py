"""
CLI Video Generator Utility for Chakra Healing
- Easily test and render custom durations (e.g. 5-minute preview or 1-hour full render)
- Auto-upscales 720p to 1080p HD
- Seamless ping-pong loop units with audio synchronization
"""

import os
import sys
import argparse
from video_generator import build_chakra_healing_video

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    parser = argparse.ArgumentParser(description="Chakra Healing Video Renderer")
    parser.add_argument("--duration", type=int, default=3600, help="Target duration in seconds (3600 for 1h, 300 for 5m)")
    parser.add_argument("--video", type=str, default=None, help="Path to input video MP4")
    parser.add_argument("--audio", type=str, default=None, help="Path to input audio MP3")
    parser.add_argument("--output", type=str, default=None, help="Path to output video MP4")
    args = parser.parse_args()

    vid_path = args.video or os.path.join(SCRIPT_DIR, "input_videos", "Golden_figure_meditating_in_forest_202608231116.mp4")
    aud_path = args.audio or os.path.join(SCRIPT_DIR, "input_audio", "Golden Resonance.mp3")
    
    dur_label = f"{args.duration//60}min" if args.duration >= 60 else f"{args.duration}s"
    safe_name = os.path.splitext(os.path.basename(aud_path))[0].replace(" ", "_")
    
    out_dir = os.path.join(SCRIPT_DIR, "output_videos")
    os.makedirs(out_dir, exist_ok=True)
    out_path = args.output or os.path.join(out_dir, f"Chakra_{safe_name}_{dur_label}.mp4")

    build_chakra_healing_video(
        input_video=vid_path,
        input_audio=aud_path,
        output_path=out_path,
        duration_seconds=args.duration,
        remove_watermark=False,
        upscale_to_1080p=True
    )

if __name__ == "__main__":
    main()
