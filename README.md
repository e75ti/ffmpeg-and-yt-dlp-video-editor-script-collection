### Black frames in video detector
`ffmpeg -i "video" -vf "blackdetect=d=2:pix_th=0.00" -an -f null - 2>&1`
### Silence in video detector
`ffmpeg -i "video" -af silencedetect=noise=-60dB:d=0.001 -f null -

### Premiere Pro MP4 from YT downloader (no audio)
`ffmpeg -f 299/298/137/136/135/134/133 "link"`
### Premiere Pro MP4 from YT downloader (with audio)
`ffmpeg -f 299+140/298+140/137+140/136+140/135+140/134+140/133+140 "link"`



**Python scripts are WIP for now, will be updated soon.**


[Youtube Formats](https://gist.github.com/AgentOak/34d47c65b1d28829bb17c24c04a0096f)

Also, will add more things soon, thanks for reading.

