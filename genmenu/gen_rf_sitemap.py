import os
import re


def gen_sitemap(md_file):
    pattern = re.compile(r'<loc>(.*?).</loc>', re.S)
    res = []
    if not os.path.exists(md_file):
        print('ERROR: 没有找到文件', md_file)
        return
    with open(md_file) as md:
        for line in md.readlines():
            line = str(line)
            cur_urls = re.findall(pattern, line)
            if len(cur_urls) > 0:
                if cur_urls[0] == '/':
                    continue
                res.append(cur_urls[0])

    return res


if __name__ == '__main__':
    print("生成博客站的sitemap")
    site_map = gen_sitemap('/Users/rustfisher/Desktop/ws/rust_hexo/rust_hexo/public/sitemap.xml')
    print(len(site_map))
    print(site_map)

    sitemap_file = 'rf-sitemap.txt'
    if os.path.exists(sitemap_file):
        os.remove(sitemap_file)
    with open(sitemap_file, 'w') as s:
        for url in site_map:
            s.write(url)
            s.write('\n')
