# 📺 Tube Downloader Pro

A sleek, modern desktop application for downloading YouTube videos and audio with an intuitive glassmorphic UI. Built with Python and PyWebView.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

## ✨ Features

- 🎬 **Multiple Quality Options** - Download videos in various resolutions (1080p, 720p, 480p, etc.)
- 🎵 **Audio Extraction** - Download audio-only in MP3 format
- 🖼️ **Video Preview** - See thumbnail, title, uploader, and duration before downloading
- 📊 **Real-time Progress** - Live download progress with speed and ETA indicators
- 📁 **Custom Save Location** - Choose where to save your downloads
- 💎 **Modern UI** - Beautiful glassmorphic design with smooth animations
- ⚡ **Fast & Efficient** - Powered by yt-dlp for reliable downloads

## 🖼️ Screenshots

<!-- Add screenshots of your application here -->

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- FFmpeg (automatically handled by imageio-ffmpeg)

### Clone the Repository

```bash
git clone https://github.com/yourusername/tube-downloader-pro.git
cd tube-downloader-pro
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Required Packages

Create a `requirements.txt` file with:

```
pywebview>=4.0
yt-dlp>=2023.0.0
imageio-ffmpeg>=0.4.8
```

## 🎯 Usage

### Running the Application

Simply run the main Python file:

```bash
python main.py
```

### How to Download

1. **Paste URL** - Copy a YouTube video URL and paste it into the input field
2. **Fetch Info** - Click "Fetch Info" or press Enter to load video details
3. **Select Format** - Choose your preferred video quality or audio-only option
4. **Download** - Click "Download Now" and watch the progress in real-time
5. **Done!** - Files are saved to your selected download folder

## 🛠️ Building Executables

### Windows

Using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --name "TubeDownloaderPro" main.py
```

### macOS

```bash
pyinstaller --onefile --windowed --name "TubeDownloaderPro" --icon=icon.icns main.py
```

### Linux

```bash
pyinstaller --onefile --name "TubeDownloaderPro" main.py
```

## 📁 Project Structure

```
tube-downloader-pro/
│
├── main.py           # Main application logic
├── index.html        # UI interface
├── requirements.txt  # Python dependencies
└── README.md        # This file
```

## 🔧 Configuration

### Default Download Location

By default, videos are saved to your system's Downloads folder. You can change this by:
- Clicking on the folder path in the application
- Selecting a new directory in the file dialog

### Supported Formats

- **Video**: MP4, MKV (various resolutions)
- **Audio**: MP3 (192kbps)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 To-Do

- [ ] Add playlist download support
- [ ] Implement download queue
- [ ] Add subtitle download option
- [ ] Support for more video platforms
- [ ] Dark/Light theme toggle
- [ ] Download history tracking

## 🐛 Known Issues

- Large file downloads (>2GB) may show inaccurate progress on some systems
- Some age-restricted videos may require authentication

## ⚖️ Legal Disclaimer

This tool is for personal use only. Please respect copyright laws and YouTube's Terms of Service. Only download content you have permission to download or content that is freely available.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - The core download engine
- [PyWebView](https://github.com/r0x0r/pywebview) - Cross-platform webview library
- [imageio-ffmpeg](https://github.com/imageio/imageio-ffmpeg) - FFmpeg binaries for Python

## 💬 Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Check existing issues for solutions
- Read the documentation carefully

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐

---

**Made with ❤️ by Nisitha Wijerathna**

*Happy Downloading! 🎉*
