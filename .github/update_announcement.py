from pathlib import Path

p = Path('index.html')
t = p.read_text(encoding='utf-8')
marker = '    <ul class="announcement-list">\n'
ann = '''        <li class="announcement-item">
  <time datetime="2026-11-27">2026-11-27</time>
  <p class="announcement-content">SchoolToolsBoard（STB）更新 1.0.3.4「函数图标尺寸与描边」：函数图标从 20px / 2.2 描边调整为 16px / 1.8 描边，和旁边工具图标的视觉大小、线宽保持一致；主工具条与批注工具条的函数入口保留，黑板模式仍可直接打开函数画板。下载：安装包（GitHub Release v1.0.3.4）。</p>
  </li>
'''

if 'STB）更新 1.0.3.4' not in t:
    assert marker in t
    t = t.replace(marker, marker + ann, 1)
    p.write_text(t, encoding='utf-8')
    print('announcement inserted')
else:
    print('announcement already present')
