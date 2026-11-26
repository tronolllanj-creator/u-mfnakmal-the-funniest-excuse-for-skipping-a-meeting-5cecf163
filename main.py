"""Make.fun entry to output a mandatory ergonomic chair excuse."""

import os

EXCUSE = 'My ergonomic office chair has agreed to log in and nod blankly on my behalf while I lie face down on the carpet.'


def main():
    output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, 'entry.txt')
    
    content = EXCUSE + '\n'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    with open(file_path, 'r', encoding='utf-8') as f:
        written_data = f.read()
        
    stripped = written_data.strip()
    assert 1 <= len(stripped) <= 200
    
    print(f'wrote entry.txt {len(written_data)} chars')


if __name__ == '__main__':
# Runner-up considered and rejected in session: 'My mute button just filed a formal grievance with HR regarding unsafe working conditions caused by yet another meeting that could have been an email.'
    main()
