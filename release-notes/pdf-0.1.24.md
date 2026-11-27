# SCHOOL_TOOLS_PDF 0.1.24

UInk 导入导出按 UInk 1.1 Beta 公开规范重写。

- 主文件 `.uink` 改为 MessagePack 对象流（Header + Header Extension + Canvas + Ink），不再是自编 JSON
- Header 版本号 11，末尾 Header Extension 登记一个 Display 设备与一个白板工作区
- 每页一个 Canvas（pageGuid、pageIndex、页码、图层号、白色背景、视口），空白页也写，页码连续
- 每笔一个 Ink 块（inkType、颜色、透明度、纹理、逐点坐标与宽度）；荧光笔按 nib 矩形 1:8 写入
- 压感烘焙进逐点宽度；首点绝对坐标，其余写相对位移
- 读取容错：同页 GUID 后出现者整体替代、未知块跳过、Clear 清空该页、尾部不完整丢弃末对象、中间损坏保留已读部分
- 声明写入基础级、读取标准级，可与智绘教 Inkeys、ICC-CE 直接互导

下载：安装包 / 免安装压缩包（GitHub Release v0.1.24）。
