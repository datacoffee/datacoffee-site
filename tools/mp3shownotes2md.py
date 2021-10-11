import argparse
import os

from mutagen.id3 import ID3


def print_shownotes_as_md(path_to_mp3_file: str):
    audio: ID3 = ID3(path_to_mp3_file)
    shownotes_path: str = path_to_mp3_file + ".md"
    with open(shownotes_path, "w") as f:
        f.write(f"# Data Coffee podcast{os.linesep}")
        f.write(f"## {audio['TIT2']}{os.linesep}{os.linesep}")
        f.write(f"Shownotes: {os.linesep}")

        for key, value in audio.items():
            if "CHAP" in key:
                f.write(f"{os.linesep}- {value.sub_frames['TIT2']}")
                if 'WXXX:chapter url' in value.sub_frames:
                    f.write(f"{os.linesep} {value.sub_frames['WXXX:chapter url'].url}")
                f.write(os.linesep)

    print(f"[DONE] Exported shownotes to {shownotes_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MP3 shownotes exports to markdown')
    parser.add_argument('--mp3', type=str, help="Input mp3 file", required=True)
    kwargs = vars(parser.parse_args())
    print_shownotes_as_md(kwargs['mp3'])
