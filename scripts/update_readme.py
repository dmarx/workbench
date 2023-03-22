from pathlib import Path
import random
import re
import subprocess

random.seed(0)

def get_last_modified_date(fpath, verbose=True):
    cmd = "git log -n 1 --pretty=format:%as --".split( )
    cmd += [str(fpath)]
    if verbose:
        print(cmd)
    response = subprocess.run(cmd, capture_output=True)
    outv = response.stdout.decode()
    if verbose:
        print(outv)
    return outv


def badges2kv(text):
    testpat = r'\/([a-zA-Z]+-[a-zA-Z]+-[a-zA-Z]+)'

    badges = re.findall(testpat, text)
    #return {b.split('-')[0]:b.split('-')[1] for b in badges}
    return [(b.split('-')[0], b.split('-')[1]) for b in badges]


def make_badge(label, prefix='tag', color='lightgrey'):
    return f"![](https://img.shields.io/badge/{prefix}-{label}-{color})"


#def make_badges(unq_tags, sep=' '):
#    return sep.join([make_badge(tag) for tag in unq_tags])


def random_hex_color():
    """generates a string for a random hex color"""
    # https://stackoverflow.com/questions/13998901/generating-a-random-hex-color-in-python
    # https://stackoverflow.com/questions/52843385/python-using-format-f-string-to-output-hex-with-0-padding-and-center
    r = lambda: random.randint(0,255)
    return  f"{r():x}{r():x}{r():x}"

md_files = Path('.').glob('*.md')
TOC = []
unq_tags = set()
for fpath in list(md_files):
    if fpath.name == 'README.md':
        continue
    with open(fpath) as f: 
        header = f.readline()
        if header.startswith('# '):
            text = f.read()
            badge_meta = badges2kv(text)
            d_ = {'fpath':fpath}
            d_['title'] = header[2:].strip()
            d_['last_modified'] = get_last_modified_date(fpath)
            d_['n_char'] = len(text)
            d_['tags'] = [v for k,v in badge_meta if k =='tag']
            d_['tags'].sort()
            unq_tags.update(d_['tags'])
            TOC.append(d_)

tag_badges_map = {tag_name:make_badge(label=tag_name, color = random_hex_color()) for tag_name in unq_tags}

def make_badges(unq_tags, sep=' '):
    return sep.join([tag_badges_map[tag] for tag in unq_tags])
    
    
TOC = sorted(TOC, key=lambda x:x['last_modified'])[::-1]

url_root = '' # "https://github.com/dmarx/bench-warmers/blob/main/"

header= "|last_modified|title|est. idea maturity|tags\n|:---|:---|---:|:---|\n"
recs = [f"|{d['last_modified']}|[{d['title']}]({url_root}{d['fpath']})|{d['n_char']}|{make_badges(d['tags'])}|" for d in TOC]
toc_str= header + '\n'.join(recs)

#readme_stub = "# title \n\n text goes here\n\n{TOC}\n\n# another section"

readme = None
if Path('README.stub').exists():
    with open('README.stub') as f:
        readme_stub = f.read()
    readme = readme_stub.replace('{TOC}', toc_str)
    readme = readme.replace('{tags}', make_badges(unq_tags))
    readme = readme.strip()
if not readme:
    with open('empty.stub') as f:
        readme = f.read()

with open('README.md','w') as f:
    f.write(readme)