from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'STB）更新 1.0.3.5'
if marker in s:
    print('already present')
else:
    anchor = '<ul class="announcement-list">\n        <li class="announcement-item">'
    item = '''<ul class="announcement-list">
        <li class="announcement-item">
  <time datetime="2026-11-27">2026-11-27</time>
  <p class="announcement-content">SchoolToolsBoard（STB）更新 1.0.3.5「图标统一、设置页裁切与速度」：主工具条图标统一为 20px，函数图标按视觉面积校准到 14px 并去掉下方“函数”文字，修复浮动栏底部裁切；设置页导航图标加宽到 20px、描边调细到 1.6，修复部分图标右侧显示不全；删除“PPT 批注”中的空格；图标启用绘制缓存与布局取整，减少重复重绘。下载：安装包（GitHub Release v1.0.3.5）。</p>
  </li>
        <li class="announcement-item">'''
    assert anchor in s, 'announcement anchor not found'
    s = s.replace(anchor, item, 1)
    p.write_text(s, encoding='utf-8')
    print('updated')
