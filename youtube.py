#!/usr/bin/env python3
"""
YouTube Video Downloader - with Quality & Volume options
==========================================================

Requirements (ek baar install karo):
    pip install yt-dlp

Aur FFmpeg zaroor install hona chahiye (volume change / video+audio merge ke liye):
    Windows: https://ffmpeg.org/download.html se download karo aur PATH me add karo
    Mac:     brew install ffmpeg
    Linux:   sudo apt install ffmpeg

Kaise chalayein:
    python youtube_downloader.py
"""

import os
import sys

try:
    import yt_dlp
except ImportError:
    print("yt-dlp installed nahi hai. Ye command chalao:")
    print("    pip install yt-dlp")
    sys.exit(1)


def check_ffmpeg():
    """Check karta hai ki ffmpeg system me hai ya nahi."""
    return os.system("ffmpeg -version >nul 2>&1" if os.name == "nt" else "ffmpeg -version >/dev/null 2>&1") == 0


def get_quality_format(choice):
    """User ke choice ke hisaab se yt-dlp format string return karta hai."""
    formats = {
        "1": "bestvideo[height<=2160]+bestaudio/best",   # 4K
        "2": "bestvideo[height<=1080]+bestaudio/best",   # 1080p Full HD
        "3": "bestvideo[height<=720]+bestaudio/best",    # 720p HD
        "4": "bestvideo[height<=480]+bestaudio/best",    # 480p
        "5": "bestaudio/best",                           # Audio only
    }
    return formats.get(choice, "bestvideo+bestaudio/best")


def get_volume_postprocessor(volume_choice):
    """Volume adjust karne ke liye ffmpeg audio filter args banata hai."""
    volume_map = {
        "1": None,     # Original volume, kuch change nahi
        "2": "1.5",    # Volume badhao (1.5x)
        "3": "2.0",    # Volume aur zyada badhao (2x)
        "4": "0.5",    # Volume kam karo (0.5x)
    }
    return volume_map.get(volume_choice)


def main():
    print("=" * 55)
    print("   YouTube Video Downloader")
    print("=" * 55)

    if not check_ffmpeg():
        print("\n⚠  WARNING: FFmpeg nahi mila!")
        print("   Video+audio merge aur volume change ke liye FFmpeg zaroori hai.")
        print("   Install karo: https://ffmpeg.org/download.html\n")

    url = input("\nYouTube video ka URL daalo: ").strip()
    if not url:
        print("URL nahi diya. Program band ho raha hai.")
        return

    print("\nQuality choose karo:")
    print("  1. 4K (2160p)")
    print("  2. Full HD (1080p)")
    print("  3. HD (720p)")
    print("  4. SD (480p)")
    print("  5. Sirf Audio (MP3)")
    quality_choice = input("Apna choice number daalo (default 2): ").strip() or "2"

    print("\nVolume adjust karna hai?")
    print("  1. Original (koi change nahi)")
    print("  2. Zyada volume (1.5x)")
    print("  3. Bahut zyada volume (2x)")
    print("  4. Kam volume (0.5x)")
    volume_choice = input("Apna choice number daalo (default 1): ").strip() or "1"

    output_folder = input("\nDownload folder ka path daalo (blank = current folder): ").strip() or "."
    os.makedirs(output_folder, exist_ok=True)

    output_template = os.path.join(output_folder, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": get_quality_format(quality_choice),
        "outtmpl": output_template,
        "merge_output_format": "mp4",
        "noplaylist": True,
        "progress_hooks": [progress_hook],
    }

    postprocessors = []

    # Agar audio-only choose kiya hai, MP3 me convert karo
    if quality_choice == "5":
        postprocessors.append({
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        })

    volume_factor = get_volume_postprocessor(volume_choice)
    if volume_factor:
        postprocessors.append({
            "key": "FFmpegPostProcessor",
            "when": "post_process",
        })
        # Volume change ke liye ffmpeg args
        ydl_opts["postprocessor_args"] = {
            "ffmpeg": ["-af", f"volume={volume_factor}"]
        }

    if postprocessors:
        ydl_opts["postprocessors"] = postprocessors

    print("\nDownload shuru ho raha hai...\n")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\nDownload safaltapoorvak (successfully) complete ho gaya!")
        print(f"   File yahan mili: {os.path.abspath(output_folder)}")
    except Exception as e:
        print(f"\nKuch error aaya: {e}")
        print("   Check karo: URL sahi hai, internet connection theek hai, aur FFmpeg installed hai.")


def progress_hook(d):
    """Download progress dikhata hai."""
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "")
        speed = d.get("_speed_str", "")
        print(f"\rDownloading... {percent} at {speed}", end="", flush=True)
    elif d["status"] == "finished":
        print("\nProcessing file, thoda wait karo...")


if __name__ == "__main__":
    main()