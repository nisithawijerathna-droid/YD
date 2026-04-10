import webview
import yt_dlp
import os
import threading
import sys
import imageio_ffmpeg
class Api:
    def __init__(self):
        self.window = None
        self.downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')

    def get_video_info(self, url):
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'extract_flat': False,
                'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe()
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                
                best_audio = None
                video_by_res = {}
                
                for f in info_dict.get('formats', []):
                    if f.get('vcodec') == 'none' and f.get('acodec') != 'none':
                        f_size = f.get('filesize') or f.get('filesize_approx') or 0
                        if not best_audio or f_size > best_audio['filesize']:
                            best_audio = {'format_id': f.get('format_id'), 'filesize': f_size}

                audio_size = best_audio['filesize'] if best_audio else 0
                audio_id = best_audio['format_id'] if best_audio else 'bestaudio'

                parsed_formats = []
                
                for f in info_dict.get('formats', []):
                    if f.get('vcodec') != 'none' and f.get('acodec') == 'none':
                        res = f.get('format_note') or f.get('resolution')
                        if not res:
                            res = f"{f.get('height', 'Unknown')}p" if f.get('height') else "Unknown"
                            
                        h = f.get('height') or 0
                        f_size = f.get('filesize') or f.get('filesize_approx') or 0
                        
                        if res not in video_by_res or f_size > video_by_res[res]['video_size']:
                            video_by_res[res] = {
                                'id': f"{f.get('format_id')}+{audio_id}",
                                'label': f"🎬 Video - {res}",
                                'size': f_size + audio_size,
                                'video_size': f_size,
                                'height': h,
                                'type': 'video'
                            }
                
                sorted_videos = sorted(video_by_res.values(), key=lambda x: x['height'], reverse=True)
                
                for v in sorted_videos:
                    parsed_formats.append({
                        'id': v['id'],
                        'label': v['label'],
                        'size': v['size'],
                        'type': 'video'
                    })
                
                if best_audio:
                    parsed_formats.append({
                        'id': 'bestaudio',
                        'label': '🎵 Audio Only (MP3)',
                        'size': audio_size,
                        'type': 'audio'
                    })
                    
                if len(parsed_formats) == 0:
                     parsed_formats.append({
                         'id': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                         'label': '🎬 Best Quality Video',
                         'size': 0,
                         'type': 'video'
                     })

                return {
                    'status': 'success',
                    'title': info_dict.get('title', 'Unknown Title'),
                    'thumbnail': info_dict.get('thumbnail', ''),
                    'duration': info_dict.get('duration_string', ''),
                    'uploader': info_dict.get('uploader', ''),
                    'formats': parsed_formats
                }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def my_hook(self, d):
        if d['status'] == 'downloading':
            try:
                percent_str = d.get('_percent_str', '0.0%').strip()
                import re
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                percent_str = ansi_escape.sub('', percent_str).replace('%', '')
                
                speed_str = ansi_escape.sub('', d.get('_speed_str', 'N/A')).strip()
                eta_str = ansi_escape.sub('', d.get('_eta_str', 'N/A')).strip()
                
                try:
                    percent = float(percent_str)
                except:
                    percent = 0.0

                if self.window:
                    self.window.evaluate_js(f"updateProgress({percent}, '{speed_str}', '{eta_str}')")
            except Exception as e:
                pass
        elif d['status'] == 'finished':
            if self.window:
                self.window.evaluate_js("updateProgress(100, 'Done', '00:00'); downloadComplete();")

    def download_video(self, url, format_id, format_type):
        def _download():
            ydl_opts = {
                'outtmpl': os.path.join(self.downloads_dir, '%(title)s.%(ext)s'),
                'progress_hooks': [self.my_hook],
                'quiet': True,
                'no_warnings': True,
                'ffmpeg_location': imageio_ffmpeg.get_ffmpeg_exe()
            }
            
            if format_type == 'audio':
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            else:
                ydl_opts['format'] = format_id
                if '+' in format_id:
                    ydl_opts['merge_output_format'] = 'mkv'
            
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            except Exception as e:
                message = str(e).replace('"', '\\"').replace("'", "\\'")
                if self.window:
                    self.window.evaluate_js(f"downloadError('{message}')")
                    
        threading.Thread(target=_download, daemon=True).start()
        return {'status': 'started'}
        
    def select_directory(self):
        if self.window:
            result = self.window.create_file_dialog(webview.FOLDER_DIALOG)
            if result and len(result) > 0:
                self.downloads_dir = result[0]
                return self.downloads_dir
        return self.downloads_dir

    def get_directory(self):
        return self.downloads_dir

if __name__ == '__main__':
    api = Api()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    html_file = os.path.join(dir_path, 'index.html')
    
    window = webview.create_window('Pro Downloader', url=html_file, js_api=api, width=900, height=650, min_size=(600, 500))
    api.window = window
    webview.start()
