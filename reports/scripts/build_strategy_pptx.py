#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 24-page strategy PPT from the 6G Data Fabric HTML report."""

from __future__ import annotations

from pathlib import Path

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

# Canvas: 16:9 widescreen
W, H = Inches(13.333), Inches(7.5)

NAVY = RGBColor(0x07, 0x1F, 0x3D)
INK = RGBColor(0x0A, 0x27, 0x44)
TEAL = RGBColor(0x0F, 0x9F, 0x9A)
CYAN = RGBColor(0x5E, 0xB6, 0xE4)
LIME = RGBColor(0xCA, 0xE8, 0x5E)
CORAL = RGBColor(0xFF, 0x8A, 0x4C)
SAND = RGBColor(0xF4, 0xF7, 0xFB)
MIST = RGBColor(0xDC, 0xE7, 0xF2)
MUTED = RGBColor(0x5A, 0x73, 0x8A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
CARD = RGBColor(0xFF, 0xFF, 0xFF)
SOFT = RGBColor(0xE8, 0xF1, 0xF6)
WARN_BG = RGBColor(0xFF, 0xF0, 0xE7)
DARK_CARD = RGBColor(0x0B, 0x31, 0x57)
ROW_ALT = RGBColor(0xF0, 0xF5, 0xF8)


def rgb_fill(shape, color: RGBColor):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color


def no_line(shape):
    shape.line.fill.background()


def set_run(run, text, size=12, bold=False, color=INK, font="Microsoft YaHei"):
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = font
    rPr = run._r.get_or_add_rPr()
    east = rPr.find(qn("a:eastAsian"))
    if east is None:
        east = rPr.makeelement(qn("a:eastAsian"), {})
        rPr.append(east)
    east.set("typeface", font)


def add_text(tf, text, size=12, bold=False, color=INK, align=PP_ALIGN.LEFT, space_after=4):
    p = tf.paragraphs[0] if not tf.paragraphs[0].text else tf.add_paragraph()
    if not tf.paragraphs[0].text and p is tf.paragraphs[0]:
        pass
    else:
        if tf.paragraphs[0].text == "" and len(tf.paragraphs) == 1:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    run = p.add_run()
    set_run(run, text, size=size, bold=bold, color=color)
    return p


def write_box(shape, lines, *, default_size=11, default_color=INK, valign=MSO_ANCHOR.TOP):
    """lines: str | (text, size, bold, color)"""
    tf = shape.text_frame
    tf.word_wrap = True
    tf.auto_size = None
    try:
        tf._txBody.bodyPr.set("anchor", "t" if valign == MSO_ANCHOR.TOP else "ctr")
    except Exception:
        pass
    # clear
    p0 = tf.paragraphs[0]
    p0.clear()
    first = True
    for item in lines:
        if isinstance(item, str):
            text, size, bold, color, after = item, default_size, False, default_color, 3
        elif len(item) == 2:
            text, size = item
            bold, color, after = False, default_color, 3
        elif len(item) == 3:
            text, size, bold = item
            color, after = default_color, 3
        elif len(item) == 4:
            text, size, bold, color = item
            after = 3
        else:
            text, size, bold, color, after = item
        p = p0 if first else tf.add_paragraph()
        first = False
        p.alignment = PP_ALIGN.LEFT
        p.space_after = Pt(after)
        run = p.add_run()
        set_run(run, text, size=size, bold=bold, color=color)


def rect(slide, left, top, width, height, fill, *, radius=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE if radius else MSO_SHAPE.RECTANGLE,
        left, top, width, height,
    )
    rgb_fill(shape, fill)
    no_line(shape)
    if radius:
        try:
            shape.adjustments[0] = 0.12
        except Exception:
            pass
    return shape


def pill(slide, left, top, width, height, fill, text, *, size=10, color=WHITE, bold=True):
    shape = rect(slide, left, top, width, height, fill, radius=True)
    write_box(shape, [(text, size, bold, color)], default_size=size, default_color=color)
    tf = shape.text_frame
    try:
        tf._txBody.bodyPr.set("anchor", "ctr")
    except Exception:
        pass
    for p in tf.paragraphs:
        p.alignment = PP_ALIGN.CENTER
    return shape


def footer(slide, page, total, chapter):
    line = rect(slide, Inches(0.45), Inches(7.12), Inches(12.4), Emu(12700), MIST)
    left = slide.shapes.add_textbox(Inches(0.45), Inches(7.18), Inches(9.5), Inches(0.28))
    write_box(left, [(f"6G 数据架构 × 数据编织 · {chapter}", 9, False, MUTED)])
    right = slide.shapes.add_textbox(Inches(10.2), Inches(7.18), Inches(2.6), Inches(0.28))
    write_box(right, [(f"{page:02d} / {total:02d}", 9, True, NAVY)])
    for p in right.text_frame.paragraphs:
        p.alignment = PP_ALIGN.RIGHT


def topbar(slide, kicker, title):
    rect(slide, Inches(0), Inches(0), W, Inches(0.08), TEAL)
    kb = slide.shapes.add_textbox(Inches(0.45), Inches(0.18), Inches(12.4), Inches(0.28))
    write_box(kb, [(kicker, 10, True, TEAL)])
    tb = slide.shapes.add_textbox(Inches(0.45), Inches(0.42), Inches(12.4), Inches(0.42))
    write_box(tb, [(title, 22, True, NAVY)])


def thesis_box(slide, text, top=Inches(0.92), height=Inches(0.72)):
    box = rect(slide, Inches(0.45), top, Inches(12.4), height, NAVY, radius=True)
    write_box(box, [("本页论点", 9, True, LIME, 1), (text, 12, False, WHITE, 0)], default_color=WHITE)
    return box


def card(slide, left, top, width, height, lines, *, fill=WHITE, accent=None):
    shape = rect(slide, left, top, width, height, fill, radius=True)
    if accent is not None:
        rect(slide, left, top, Emu(63500), height, accent)
    write_box(shape, lines)
    # padding via margins
    tf = shape.text_frame
    tf.margin_left = Inches(0.12)
    tf.margin_right = Inches(0.1)
    tf.margin_top = Inches(0.08)
    tf.margin_bottom = Inches(0.06)
    return shape


def add_table(slide, left, top, width, height, headers, rows, *, col_w=None, font_size=9):
    table_shape = slide.shapes.add_table(len(rows) + 1, len(headers), left, top, width, height)
    table = table_shape.table
    if col_w:
        for i, w in enumerate(col_w):
            table.columns[i].width = w
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.text = ""
        p = cell.text_frame.paragraphs[0]
        run = p.add_run()
        set_run(run, h, size=font_size, bold=True, color=WHITE)
        cell.fill.solid()
        cell.fill.fore_color.rgb = NAVY
        cell.vertical_anchor = MSO_ANCHOR.MIDDLE
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.text = ""
            p = cell.text_frame.paragraphs[0]
            run = p.add_run()
            set_run(run, str(val), size=font_size - 0.5 if font_size > 9 else font_size, bold=False, color=INK)
            cell.fill.solid()
            cell.fill.fore_color.rgb = WHITE if i % 2 == 0 else ROW_ALT
            cell.vertical_anchor = MSO_ANCHOR.TOP
            cell.text_frame.word_wrap = True
    return table_shape


def bg(slide, dark=False):
    if dark:
        rect(slide, 0, 0, W, H, NAVY)
    else:
        rect(slide, 0, 0, W, H, SAND)
        # subtle side accent
        rect(slide, 0, 0, Inches(0.12), H, TEAL)


def new_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])


def build():
    prs = Presentation()
    prs.slide_width = W
    prs.slide_height = H
    total = 24
    slides_meta = []

    # ========== 01 Cover ==========
    s = new_slide(prs)
    bg(s, dark=True)
    rect(s, 0, 0, W, H, NAVY)
    # atmosphere bars
    rect(s, Inches(0), Inches(0), W, Inches(0.18), TEAL)
    rect(s, Inches(0), Inches(7.32), W, Inches(0.18), CYAN)
    for i, c in enumerate([TEAL, CYAN, LIME, CORAL]):
        rect(s, Inches(0.45 + i * 0.35), Inches(1.55), Inches(0.28), Inches(0.08), c)
    box = s.shapes.add_textbox(Inches(0.55), Inches(1.9), Inches(12), Inches(0.4))
    write_box(box, [("产业战略研究 · 中兴通讯视角 · 非公司正式立场", 12, False, CYAN)])
    box = s.shapes.add_textbox(Inches(0.55), Inches(2.35), Inches(12), Inches(1.6))
    write_box(box, [
        ("6G 数据架构 × 数据编织", 34, True, WHITE, 8),
        ("行业趋势与中兴战略定位", 28, True, LIME, 10),
    ])
    box = s.shapes.add_textbox(Inches(0.55), Inches(4.2), Inches(11.5), Inches(1.1))
    write_box(box, [
        ("从「连接如何建立」转向「数据如何生产、理解、治理并驱动可信行动」。", 14, False, MIST, 6),
        ("对应模板：需求 · 现状 · 趋势 · 3/5年 · 定位 · 机会 · 策略 · 关键 AP", 13, False, CYAN, 4),
        ("标准锚点：ITU · 3GPP SA2/SA5 · O-RAN · ETSI ZSM　｜　公司锚点：AIR Net · Fault Agent · ZSM 029　｜　截点：2026-08", 11, False, MUTED, 0),
    ])
    box = s.shapes.add_textbox(Inches(0.55), Inches(6.5), Inches(12), Inches(0.4))
    write_box(box, [("完整论证版胶片 · 24 页 · 与 HTML 报告章节一一对应 · 非信息预览版", 11, False, LIME)])
    slides_meta.append("封面")

    # ========== 02 Agenda / Logic ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "00  READING LOGIC", "阅读逻辑：八章不是平行清单，而是一条因果链")
    thesis_box(s, "先看清「为何需要数据管理层」与「行业抢什么控制点」，再推「趋势不变量」，最后落到中兴「定位—机会—策略—可验收 AP」。跳过前四章会把后四章变成口号。")
    steps = [
        ("01", "需求和目标", "定义问题与七个可交付判断"),
        ("02", "行业与竞争", "范式、Fabric适配、标准与三强抢位"),
        ("03", "产业趋势", "T1–T8 因果链，非平行产品"),
        ("04", "3年/5年", "看透不变量，看清控制点复利"),
        ("05", "中兴定位", "证据分层 + C1–C4 控制点"),
        ("06", "机会选择", "六维评分 → 主攻/配合/不做"),
        ("07", "策略建议", "Build边界、节奏、阶段门、风险"),
        ("08", "关键 AP", "AP0–AP10 与 90 天决策输出"),
    ]
    for i, (n, t, d) in enumerate(steps):
        col = i % 4
        row = i // 4
        left = Inches(0.45 + col * 3.2)
        top = Inches(1.9 + row * 2.35)
        card(s, left, top, Inches(3.05), Inches(2.15), [
            (n, 18, True, TEAL, 2),
            (t, 15, True, NAVY, 6),
            (d, 11, False, MUTED, 8),
            ("↓ 输出喂给下一章" if i < 7 else "→ 可验收行动包", 10, False, CORAL if i < 7 else TEAL, 0),
        ], accent=TEAL if i < 4 else CORAL)
    footer(s, 2, total, "阅读逻辑")
    slides_meta.append("阅读逻辑")

    # ========== 03 Ch01 Need ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "01  REQUIREMENT & OBJECTIVE", "需求和目标：不是再建平台，而是建立可信数据能力")
    thesis_box(s, "当6G网络同时成为数据生产者、AI载体、感知系统和自治执行体时，真正要解决的是：跨RAN/Core/管理域/边云的可信数据能力，以及哪些能力会成为标准与产业竞争中的控制点。")
    needs = [
        ("需求1", "识别架构范式变化", "为何不能只沿用「会话连接+中央分析」；数据管理为何上升为AI原生、通感、孪生与自治的共同底座。"),
        ("需求2", "建立统一能力地图", "用数据编织组织目录/语义/质量/集成/编排/产品/安全；划清快环慢环、控制面与执行面边界。"),
        ("需求3", "看清标准与竞争窗口", "区分既定积木、Rel-20研究、Rel-21规范、厂商主张与商用产品，避免误判与错过语义/任务适用性话语权。"),
    ]
    for i, (tag, title, body) in enumerate(needs):
        card(s, Inches(0.45 + i * 4.2), Inches(1.85), Inches(4.0), Inches(2.0), [
            (tag, 10, True, TEAL, 2),
            (title, 14, True, NAVY, 6),
            (body, 11, False, MUTED, 0),
        ], accent=TEAL)
    deliverables = [
        ("1张范式图", "连接→数据—智能—行动"),
        ("1套能力栈", "编织与生命周期统一"),
        ("1个竞争矩阵", "标准域+爱立信/华为/诺基亚"),
        ("2个时间窗", "3年底座 / 5年控制点"),
        ("1个中兴定位", "坐标系中的强弱与主攻位"),
        ("1组机会选择", "主攻·中期·路标分层"),
        ("1张策略表", "先做后做与组织抓手"),
        ("边界声明", "公开证据≠正式承诺"),
    ]
    for i, (t, d) in enumerate(deliverables):
        col, row = i % 4, i // 4
        card(s, Inches(0.45 + col * 3.2), Inches(4.1 + row * 1.25), Inches(3.05), Inches(1.12), [
            (t, 12, True, NAVY, 2),
            (d, 10, False, MUTED, 0),
        ], fill=SOFT)
    footer(s, 3, total, "01 需求和目标")
    slides_meta.append("01需求")

    # ========== 04 Evidence chain + R1-R8 ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "01  REQUIREMENT · EVIDENCE CHAIN", "研究对象是一条「事实—数据—智能—行动」证据链")
    thesis_box(s, "目标不是搬运更多原始数据，而是让每次数据使用与网络动作都可解释、可约束、可验证、可回退。核心一句话：把数据从网络运行副产物升级为可发现、可理解、可组合、可约束、可证明的生产要素。")
    chain = [
        ("网络与环境事实", "RAN·Core·云\n终端·感知·业务"),
        ("近源处理", "过滤·聚合·特征\n匿名·时间对齐"),
        ("数据编织控制面", "目录·语义· 任务适用性\n血缘·契约·策略·证据"),
        ("智能与孪生", "训练·推理·NDT\n意图·策略·Agent"),
        ("行动与反馈", "控制·开放·变现\n效果·回滚·审计"),
    ]
    for i, (t, d) in enumerate(chain):
        left = Inches(0.4 + i * 2.55)
        fill = NAVY if i == 2 else WHITE
        tc = LIME if i == 2 else NAVY
        dc = WHITE if i == 2 else MUTED
        card(s, left, Inches(1.85), Inches(2.4), Inches(1.55), [
            (t, 12, True, tc, 4),
            (d, 10, False, dc, 0),
        ], fill=fill, accent=CORAL if i != 2 else LIME)
        if i < 4:
            arr = s.shapes.add_textbox(Inches(2.7 + i * 2.55), Inches(2.4), Inches(0.3), Inches(0.35))
            write_box(arr, [("→", 16, True, CORAL)])
    # R1-R8 compact
    rs = [
        ("R1", "统一发现与语义寻址"),
        ("R2", "按需采集与近源减量"),
        ("R3", "跨时标多模式交付"),
        ("R4", "通信级任务适用性"),
        ("R5", "数据—模型—策略—动作血缘"),
        ("R6", "用途、安全与主权强制"),
        ("R7", "有界智能与冲突治理"),
        ("R8", "数据产品与跨组织运营"),
    ]
    note = s.shapes.add_textbox(Inches(0.45), Inches(3.55), Inches(12.4), Inches(0.3))
    write_box(note, [("由 AI原生 / 通感 / 边云 / 孪生 / 跨域自治 / 生态开放 六类场景反推：数据管理层八项刚性需求", 11, True, TEAL)])
    for i, (rid, title) in enumerate(rs):
        col, row = i % 4, i // 4
        card(s, Inches(0.45 + col * 3.2), Inches(3.95 + row * 1.35), Inches(3.05), Inches(1.2), [
            (rid, 13, True, CORAL, 2),
            (title, 12, True, NAVY, 0),
        ])
    footer(s, 4, total, "01 需求和目标")
    slides_meta.append("01证据链与R")

    # ========== 05 Ch02 Paradigm ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "02  INDUSTRY · PARADIGM SHIFT", "行业窗口：愿景已定、规范未冻、厂商抢位")
    thesis_box(s, "6G变化不是「多一个数据湖」，而是几乎每个域都同时生产/消费数据、运行模型并执行动作。竞争焦点从连接中心转向数据理解、策略与证据层。")
    card(s, Inches(0.45), Inches(1.85), Inches(6.0), Inches(4.7), [
        ("5G / 5G-A 主导范式", 14, True, NAVY, 6),
        ("· 连接、会话、网络功能与暴露为中心", 11, False, MUTED, 3),
        ("· 分析集中在 NWDAF / MDA / 湖仓", 11, False, MUTED, 3),
        ("· RAN/Core 主要上送测量与流量", 11, False, MUTED, 3),
        ("· 输出多为报表与优化建议", 11, False, MUTED, 8),
        ("局限", 12, True, CORAL, 4),
        ("中央分析难覆盖多时标、多主体与动作风险；数据语义与权威源分散。", 11, False, INK, 0),
    ], fill=SOFT)
    card(s, Inches(6.85), Inches(1.85), Inches(6.0), Inches(4.7), [
        ("6G 数据—智能原生范式", 14, True, LIME, 6),
        ("· RAN：无线事实 / ISAC / 本地AI", 11, False, WHITE, 3),
        ("· Core：意图 / 会话 / 暴露", 11, False, WHITE, 3),
        ("· 边云：训练 / 推理 / 孪生", 11, False, WHITE, 3),
        ("· SMO/RIC：跨时标策略与闭环", 11, False, WHITE, 8),
        ("可信数据管理层", 12, True, LIME, 4),
        ("语义 · 任务适用性· 契约 · 策略 · 证据\n统一理解与约束，不统一所有存储与时延", 11, False, MIST, 0),
    ], fill=NAVY)
    arrow = s.shapes.add_textbox(Inches(6.15), Inches(3.8), Inches(0.7), Inches(0.4))
    write_box(arrow, [("→", 22, True, CORAL)])
    footer(s, 5, total, "02 行业环境")
    slides_meta.append("02范式转变")

    # ========== 06 Fabric fit ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "02  DATA FABRIC FIT", "Data Fabric：总体适配，但必须通信级增强")
    thesis_box(s, "Data Fabric可做6G数据管理层的设计骨架（尤其Non-RT/跨域供给），但不能原样进入通信网：缺RAN语义、无线数据适用性、时标隔离、动作安全与多Agent治理；绝不能成为毫秒快环的远端在线依赖。", height=Inches(0.78))
    card(s, Inches(0.45), Inches(1.9), Inches(6.1), Inches(1.55), [
        ("结论：架构机制总体适配", 13, True, TEAL, 4),
        ("数据分布但元数据统一、控制与执行分离、多模式集成、主动元数据、数据产品和贯穿治理 → 对应 R1/R2/R3、R5、R8、R6。", 11, False, INK, 0),
    ], fill=SOFT, accent=TEAL)
    card(s, Inches(6.75), Inches(1.9), Inches(6.1), Inches(1.55), [
        ("必须通信级增强", 13, True, CORAL, 4),
        ("补齐 RAN 对象与时空语义、无线数据适用性、亚秒时标隔离、动作安全、NDT 证据门槛、多 Agent 冲突治理；不替代 RAN 协议 / SA2·SA5 / O-RAN。", 11, False, INK, 0),
    ], fill=WARN_BG, accent=CORAL)
    layers = [
        ("L6", "业务/生态/行动", "受治Agent低"),
        ("L5", "数据产品与契约", "跨域语义弱"),
        ("L4", "主动元数据控制面", "主动闭环中"),
        ("L3", "跨时标集成编排", "语义统一不足"),
        ("L2", "近源处理与存储", "跨域编排中"),
        ("L1", "分布式权威源", "权威语义散"),
    ]
    for i, (lid, name, st) in enumerate(layers):
        card(s, Inches(0.45 + i * 2.12), Inches(3.7), Inches(2.02), Inches(1.55), [
            (lid, 12, True, NAVY, 2),
            (name, 11, True, INK, 4),
            (st, 10, False, MUTED, 0),
        ])
    ddaa = Path("/workspace/reports/data-fabric-assets/6g-ddaa-architecture.png")
    card(s, Inches(0.45), Inches(5.4), Inches(7.4), Inches(1.3), [
        ("成熟度：企业Fabric已产品化；6G通信级管理层总体G1—G2、局部G3。", 11, True, NAVY, 3),
        ("闸门：G0边界语义→G1只读可观察→G2产品契约→G3影子闭环→G4–G5有界自治。", 10, False, MUTED, 3),
        ("原则：快环本地确定性；Near-RT边缘缓存；Non-RT治理；跨域只供最小必要产品。", 10, False, MUTED, 0),
    ], fill=SOFT)
    if ddaa.exists():
        rect(s, Inches(8.05), Inches(5.4), Inches(4.8), Inches(1.3), WHITE, radius=True)
        s.shapes.add_picture(str(ddaa), Inches(8.15), Inches(5.48), height=Inches(1.14))
        cap = s.shapes.add_textbox(Inches(8.15), Inches(6.55), Inches(4.6), Inches(0.22))
        write_box(cap, [("参考：6G DDAA学术架构（非3GPP规范）", 8, False, MUTED)])
    footer(s, 6, total, "02 行业环境")
    slides_meta.append("02Fabric适配")

    # ========== 07 Competition ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "02  STANDARDS & VENDORS", "标准与厂商：能力方向趋同，架构形态与控制权未收敛")
    thesis_box(s, "标准竞争的核心不是出现名为 Data Fabric 的新网元，而是谁定义来源、语义、质量、发现、处理、暴露、安全与行动边界。产品先于6G验证部分能力，但尚无中立证据证明完整跨域 Fabric 广泛部署。")
    add_table(
        s, Inches(0.45), Inches(1.8), Inches(12.4), Inches(1.55),
        ["标准域", "可确认进展", "对 Fabric 的贡献", "不能扩大化为"],
        [
            ["ITU IMT-2030", "M.2160 已生效", "目标与能力边界", "未定义编织网元"],
            ["3GPP Rel-20/21", "Rel-20研究；Rel-21首个规范Release", "2026–2028收敛窗口", "研究文本≠最终规范"],
            ["SA2 KI#21 / SA5 DMFW", "Draft；数据框架研究", "发现/处理/暴露与管理侧框架", "不预判统一网元"],
        ],
        col_w=[Inches(2.4), Inches(3.5), Inches(3.3), Inches(3.2)],
        font_size=9,
    )
    assets = Path("/workspace/reports/data-fabric-assets")
    vendors = [
        ("Ericsson", "联邦数据管理 + EIAP/DataOps + API生态｜底座强、独立网元叙事弱",
         assets / "ericsson-data-ingestion-architecture.png"),
        ("Huawei", "DO/DA/DCP研究 + AUTINOps商用桥｜研究与商用平面易混读",
         assets / "huawei-6g-data-plane-architecture.jpg"),
        ("Nokia", "AN Fabric / Data Suite产品化最清晰｜跨厂商统一仍缺中立证明",
         assets / "nokia-autonomous-network-fabric.png"),
    ]
    for i, (name, blurb, img) in enumerate(vendors):
        left = Inches(0.45 + i * 4.2)
        card(s, left, Inches(3.5), Inches(4.0), Inches(0.85), [
            (name, 13, True, NAVY, 2),
            (blurb, 9, False, MUTED, 0),
        ], accent=CYAN)
        if img.exists():
            rect(s, left, Inches(4.45), Inches(4.0), Inches(2.2), WHITE, radius=True)
            s.shapes.add_picture(
                str(img),
                left + Inches(0.15),
                Inches(4.55),
                width=Inches(3.7),
                height=Inches(2.0),
            )
    footer(s, 7, total, "02 行业环境")
    slides_meta.append("02标准与厂商")

    # ========== 08 Industry summary ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "02  INDUSTRY SUMMARY", "现状小结：确认「需要哪些能力」，仍在竞争「谁控制、如何证明」")
    thesis_box(s, "最稳健的断言不是「谁已拥有完整6G Data Fabric」，而是：产业已确认能力清单，但仍在竞争架构组合、控制权归属与价值证明方式。")
    items = [
        ("共识已形成", "分布式接入、近源处理、统一语义/任务适用性、产品化供给，并与AI/Agent和闭环证据关联。"),
        ("标准未冻结", "SA2/SA5仍是Rel-20研究；独立数据面、新NF、增强既有功能或混合实现均未定型。"),
        ("产品先于6G", "EIAP/DataOps、AUTINOps、Nokia AN Fabric已用5G-A/OAM验证部分能力，成为前置桥梁。"),
        ("成熟度不均", "采集/湖仓/流/目录成熟；跨域主动元数据、任务适用性、Agent治理和高风险闭环仍在G1—G3。"),
        ("竞争跨层展开", "设备商争语义与执行；云争运行时；聚合商争渠道；运营商争主权与可替换性。"),
        ("尚无绝对领先", "没有运营商中立证据证明任一家已在多运营商、多厂商环境广泛部署完整跨域Fabric。"),
    ]
    for i, (t, b) in enumerate(items):
        col, row = i % 3, i // 3
        card(s, Inches(0.45 + col * 4.2), Inches(1.9 + row * 2.35), Inches(4.0), Inches(2.15), [
            (t, 14, True, NAVY, 6),
            (b, 12, False, MUTED, 0),
        ], accent=TEAL if row == 0 else CORAL)
    footer(s, 8, total, "02 行业环境")
    slides_meta.append("02现状小结")

    # ========== 09 Trends overview ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "03  TREND CAUSAL CHAIN", "产业趋势：八条不是平行产品，而是一条因果链")
    thesis_box(s, "数据越分布，越需要元数据事件；机器消费越多，越需要显式语义与契约；自动化权限越大，越需要策略、证明和可回滚性；跨组织流通越多，越需要数据空间式信任与商业运营。")
    chain = [
        ("分布式数据生产", "RAN/Core/Edge/ISAC"),
        ("元数据事件化", "发现变化与影响"),
        ("语义与产品契约", "机器可理解可组合"),
        ("智能/Agent行动", "建议→低风险执行"),
        ("可信控制与生态", "策略·证明·回滚·计量"),
    ]
    for i, (t, d) in enumerate(chain):
        card(s, Inches(0.4 + i * 2.55), Inches(1.9), Inches(2.4), Inches(1.35), [
            (t, 12, True, WHITE, 4),
            (d, 10, False, LIME, 0),
        ], fill=NAVY)
        if i < 4:
            a = s.shapes.add_textbox(Inches(2.7 + i * 2.55), Inches(2.35), Inches(0.3), Inches(0.3))
            write_box(a, [("→", 14, True, CORAL)])
    mains = [
        ("工程主线", "从管道到事件化控制面：差异化转向元数据激活、跨接口语义、任务适用性、影响分析与策略强制。"),
        ("标准主线", "从研究问题到规范能力包：Rel-20验证候选，Rel-21选最小可标准化集合；统一网元概率低于统一语义/接口。"),
        ("产品主线", "从平台功能到场景闭环：客户为故障/能耗/移动性/QoE/模型泛化/开放收入的可测结果买单。"),
        ("竞争主线", "从设备份额到控制点份额：语义、任务适用性、近源运行时、证据链与API渠道决定软件与生态复利。"),
    ]
    for i, (t, b) in enumerate(mains):
        col, row = i % 2, i // 2
        card(s, Inches(0.45 + col * 6.4), Inches(3.5 + row * 1.55), Inches(6.2), Inches(1.4), [
            (t, 13, True, TEAL, 4),
            (b, 11, False, INK, 0),
        ])
    footer(s, 9, total, "03 产业趋势")
    slides_meta.append("03趋势主线")

    # ========== 10 T1-T4 ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "03  TRENDS T1–T4", "前半因果链：产品化 → 事件控制面 → 两级部署 → 有界智能耦合")
    thesis_box(s, "T1–T4回答「数据如何被消费与控制」：先把输出变成带SLO的产品，再用事件化元数据驱动控制，以边缘子Fabric守住时限，最后与AI/Agent耦合但保持责任边界。")
    trends = [
        ("T1 · 高确定性", "网络数据从采集对象变为可运营产品",
         "价值单位从表/Topic/PB转为满足消费者与SLO的数据产品。",
         "为何：AI/NDT/跨域自动化需要稳定契约；Nokia Data Suite、Ericsson mesh、Open Gateway均要求一致行为。",
         "落地：先做移动性/节能/故障/QoE/模型训练高复用产品；必须带对象范围、事件时间、语义版本、任务适用性、用途、Owner。",
         "反证：只有Marketplace页面、无Owner/SLO/退出；长期无人消费仍重复采集。"),
        ("T2 · 高确定性", "元数据事件化成为可信控制面输入",
         "目录从定期盘点升级为感知结构/配置/质量/权限/成本/模型变化的事件网络。",
         "为何：目录延迟数小时意味着错误结构进入生产决策；OpenLineage等已验证工程可行性。",
         "落地：跨O1/E2/A1/R1统一事件标识；高风险阻断/审批；事件总线不得成为快环同步依赖。",
         "反证：目录仍靠人工扫描，变更后靠事故发现。"),
        ("T3 · 高确定性", "边缘子Fabric与两级控制成主流形态",
         "全局控制面管语义/策略，本地子Fabric保时限、自治与断链生存。",
         "为何：RAN快环/MEC/专网/NTN无法依赖远端联邦查询；三强部署原则趋同。",
         "落地：明确<10ms/Near-RT/Non-RT/训练依赖清单；支持断链、冲突合并、版本回退。",
         "反证：所有查询必须经中心，或各域无法共享语义。"),
        ("T4 · 中高确定性", "Fabric与AI/Agent耦合，但不合并成无边界大脑",
         "编排对象扩展为数据—模型—算力—动作组合；共同证据图，责任不混。",
         "为何：训练/验证/部署/推理共享可信数据；Agent需工具目录、身份与委托。",
         "落地：IPOE约束；先OAM/Non-RT与低风险动作；快环保留确定性执行。",
         "反证：只有聊天入口，无身份、作用域和动作证据。"),
    ]
    for i, (tag, title, claim, why, how, anti) in enumerate(trends):
        col, row = i % 2, i // 2
        card(s, Inches(0.4 + col * 6.45), Inches(1.85 + row * 2.45), Inches(6.25), Inches(2.3), [
            (tag, 9, True, TEAL, 1),
            (title, 12, True, NAVY, 2),
            (claim, 10, False, INK, 2),
            (why, 9, False, MUTED, 1),
            (how, 9, False, MUTED, 1),
            (anti, 9, False, CORAL, 0),
        ])
    footer(s, 10, total, "03 产业趋势")
    slides_meta.append("03 T1-T4")

    # ========== 11 T5-T8 ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "03  TRENDS T5–T8", "后半因果链：证据闸门 → 任务适用性标尺 → 商业分层 → 能力集合化")
    thesis_box(s, "T5–T8回答「如何证明、计量与标准化」：高风险动作要孪生证据，无线数据要通信级任务适用性，商业走内部产品→API→渠道分层，标准更可能冻结能力集合而非固定新网元。")
    trends = [
        ("T5 · 中高确定性", "NDT由规划工具走向高风险闭环证据闸门",
         "竞争点从可视化/仿真规模，转向为生产动作提供可量化反事实证据。",
         "落地：定义保真度、最大同步滞后、可接受误差；孪生通过须与灰度/风险预算/熔断/接管组合；超误差退回建议模式。",
         "反证：只有可视化模型，无误差门槛与生产反馈。"),
        ("T6 · 中高确定性", "任务适用性规则成为6G数据接口与产品竞争核心标尺",
         "可用性由网络状态、采样与误差决定，不能只用完整性与新鲜度。",
         "落地：按数据族建适用性信封；纳入采样覆盖、时空代表性、同步、配置、标签来源、训练—服务偏差；绑定产品SLO与动作风险。",
         "反证：只统计记录量、接口成功率或单一完整性分数。"),
        ("T7 · 中等确定性", "内部Fabric、数据空间与网络API形成分层商业链",
         "内部治理=可信生产；网络API=标准消费；Operate API/聚合渠道=规模运营。",
         "落地：先产品化内部服务再映射CAMARA；计价走向交易/会话/结果；数据空间补跨组织信任，但不进RAN快环。",
         "反证：API数量增加但无跨网一致、活跃开发者与收入。"),
        ("T8 · 低—中确定性", "专用数据面可能标准化为「能力集合」而非固定新网元",
         "需求留下，拓扑与名称未必留下；发现/编排/处理/PubSub/存储/暴露/治理可分布到新旧功能。",
         "落地：跟踪能力语义与接口，不押注厂商网元名；可插拔运行时与多后端；独立平面若增时延/状态重复则退回增强方案。",
         "反证：3GPP明确冻结独立统一数据平面及必选NF。"),
    ]
    for i, (tag, title, claim, how, anti) in enumerate(trends):
        col, row = i % 2, i // 2
        card(s, Inches(0.4 + col * 6.45), Inches(1.85 + row * 2.45), Inches(6.25), Inches(2.3), [
            (tag, 9, True, TEAL, 1),
            (title, 12, True, NAVY, 2),
            (claim, 10, False, INK, 3),
            (how, 9, False, MUTED, 2),
            (anti, 9, False, CORAL, 0),
        ])
    footer(s, 11, total, "03 产业趋势")
    slides_meta.append("03 T5-T8")

    # ========== 12 Horizon 3/5 ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "04  3-YEAR / 5-YEAR", "3年看透不变量，5年看清控制点复利")
    thesis_box(s, "「看透」=标准冻结前看清不会改变的底层需求与可验证能力；「看清」=首批6G商用准备期，看清产品控制点、生态分工与商业闭环归属。")
    card(s, Inches(0.45), Inches(1.85), Inches(6.15), Inches(4.8), [
        ("未来 1–3 年 · 看透", 15, True, NAVY, 8),
        ("标准窗口", 11, True, TEAL, 2),
        ("Rel-21于2027定包与Stage1，2028完成Stage2/3主要冻结；数据框架向最小规范集合收敛。", 10, False, MUTED, 5),
        ("工程底座", 11, True, TEAL, 2),
        ("元数据事件、跨O1/E2/A1/R1映射、RAN数据适用性、数据契约、模型/动作血缘成领先试点基线。", 10, False, MUTED, 5),
        ("产品形态", 11, True, TEAL, 2),
        ("SMO/Non-RT能力、近源运行时、NDT预演、受治RAG/Agent先以外挂/增强落地，不一次性重构全网。", 10, False, MUTED, 5),
        ("竞争与商业", 11, True, TEAL, 2),
        ("市场用现网闭环收益与多厂商互操作过滤营销；Open Gateway瓶颈转向行业工作流、跨网一致与结果定价。", 10, False, MUTED, 0),
    ], fill=SOFT)
    card(s, Inches(6.8), Inches(1.85), Inches(6.05), Inches(4.8), [
        ("未来 3–5 年 · 看清", 15, True, LIME, 8),
        ("架构落位", 11, True, CYAN, 2),
        ("控制面集中协调、数据/算力分布执行；独立数据面是否存在不如能力可组合与可证明重要。", 10, False, MIST, 5),
        ("智能边界", 11, True, CYAN, 2),
        ("低风险有界自治；高风险强制「策略—孪生—灰度—回滚—证据」；全面无人治理仍不可信。", 10, False, MIST, 5),
        ("产业分层", 11, True, CYAN, 2),
        ("设备商控语义与近源；云控模型与工具；聚合商控分发；运营商要求主权与可替换性。", 10, False, MIST, 5),
        ("胜负手", 11, True, CYAN, 2),
        ("多厂商语义映射、任务适用性表达与测试规则、Agent可信运行时、NDT证据门槛、跨域产品运营形成长期壁垒。", 10, False, MIST, 0),
    ], fill=NAVY)
    footer(s, 12, total, "04 3年/5年")
    slides_meta.append("04时间窗")

    # ========== 13 Ten judgements ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "04  TEN JUDGEMENTS", "十条趋势判断：第四章对 T1–T8 的决策压缩，不是另起三条")
    thesis_box(s, "十条判断用于决策筛选：高确定性条目应进入工程与标准基线；中等确定性条目进入时间盒验证；最终验证点是 Rel-21 文本、跨厂商互操作、现网闭环收益与可持续收入。")
    judgements = [
        ("01", "高", "需要通用数据能力，未必需要独立「数据面」网元"),
        ("02", "高", "RAN语义与任务适用性比原始数据规模更稀缺"),
        ("03", "高", "Fabric价值从集成上移到可信智能控制"),
        ("04", "高", "快环不会被中央Fabric接管"),
        ("05", "中高", "Agent先辅助、后有界执行，不跨越治理成熟度"),
        ("06", "中高", "NDT是重要证据源，不是绝对安全证明"),
        ("07", "高", "Mesh/Fabric/Lakehouse组合，而非唯一赢家"),
        ("08", "中高", "网络API商业化倒逼内部数据产品化"),
        ("09", "中", "云与数据平台是关键竞合方，难独代RAN语义"),
        ("10", "中", "跨企业完全无人治理五年内仍非普遍现实"),
    ]
    for i, (n, cert, text) in enumerate(judgements):
        col, row = i % 2, i // 2
        color = TEAL if cert == "高" else (CORAL if cert.startswith("中高") else MUTED)
        card(s, Inches(0.4 + col * 6.45), Inches(1.8 + row * 0.95), Inches(6.25), Inches(0.88), [
            (f"{n}  [{cert}确定性]  {text}", 11, True, NAVY, 0),
        ], accent=color)
    footer(s, 13, total, "04 3年/5年")
    slides_meta.append("04十条判断")

    # ========== 14 ZTE assets ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "05  ZTE POSITION · ASSETS", "中兴定位：强于网络智能产品化，弱于通用 Fabric 完整产品")
    thesis_box(s, "正确战略不是再造对标 IBM/Informatica/Nokia Data Suite 的通用编织平台，而是把 AIR Net 数据引擎升级为主航道共用的横向数据控制能力；争夺「语义+任务适用性+近源执行+有界供数」，而非「大一统数据面」品牌。", height=Inches(0.8))
    anchors = [
        ("产品锚点", "AIR Net 三引擎", "数据引擎 + 大模型引擎 + 数字孪生引擎，支撑 Copilot/Agent 与跨域闭环；数据引擎提供资产、AI Ready 治理与智能分析。"),
        ("场景锚点", "Fault Agent", "浙江移动：根因识别>90%，诊断约30→<5分钟，工单-20%；中国电信多省试点。案例口径，非独立审计。"),
        ("标准锚点", "ETSI ZSM 029", "Data Management Agent for AN；中兴为 Supporting Organization；覆盖注册/发现/资产/认证/采集/编排——与控制语义高度重合。"),
    ]
    for i, (tag, title, body) in enumerate(anchors):
        card(s, Inches(0.45 + i * 4.2), Inches(1.95), Inches(4.0), Inches(2.35), [
            (tag, 10, True, TEAL, 2),
            (title, 14, True, NAVY, 4),
            (body, 10, False, MUTED, 0),
        ])
    evid = [
        ("E4 API", "中国移动Quality on Demand（QoD）：CAMARA+中兴NEF；25家客户、月调用>3400万、收入证据"),
        ("E4 故障", "GSMA浙江移动具名闭环结果"),
        ("E3 产品", "CUDR、AIR Net、Co-Sight、Ready for ODA"),
        ("E2 试点", "中国电信Fault Agent「piloted」"),
        ("E1 标准", "ZSM029席位；SA5 Unified data framework输入"),
        ("E0 假设", "RAN数据适用性/近源Agent/跨接口事件 → 待PoC与付费验证"),
    ]
    for i, (t, b) in enumerate(evid):
        col, row = i % 3, i // 3
        card(s, Inches(0.45 + col * 4.2), Inches(4.5 + row * 1.1), Inches(4.0), Inches(1.0), [
            (t, 11, True, CORAL if t.startswith("E0") else NAVY, 1),
            (b, 9, False, MUTED, 0),
        ], fill=WARN_BG if t.startswith("E0") else WHITE)
    footer(s, 14, total, "05 公司定位")
    slides_meta.append("05资产与证据")

    # ========== 15 Control points ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "05  CONTROL POINTS C1–C4", "目标定位：四个必须掌握的控制点，三个开放边界")
    thesis_box(s, "工作定位（研究命名）：Telecom Trusted Data Control Fabric——统一「理解、质量、契约与证据」，不统一所有存储、模型、协议与毫秒级执行。")
    ctrls = [
        ("C1 语义与任务适用性", "对象映射·适用性信封·配置/时空/采样", "中兴必须主导", TEAL),
        ("C2 产品/契约/主权", "Owner·SLO·用途·驻留·保留·删除传播", "掌握电信模板", CYAN),
        ("C3 近源 Data Agent", "过滤·特征·缓存·本地策略·断链生存", "差异化主场", NAVY),
        ("C4 Agent/NDT 证据", "身份·策略·仿真·动作·结果·回滚", "与生态联合", CORAL),
    ]
    for i, (t, d, role, c) in enumerate(ctrls):
        card(s, Inches(0.4 + i * 3.2), Inches(1.9), Inches(3.05), Inches(2.35), [
            (t, 13, True, WHITE, 6),
            (d, 11, False, MIST, 8),
            (role, 11, True, LIME, 0),
        ], fill=c)
    card(s, Inches(0.45), Inches(4.45), Inches(12.4), Inches(0.7), [
        ("分布式执行载体：RAN/Edge本地代理 · SMO/Non-RT服务 · Core/NWDAF/DCCF · OSS数据引擎 · 云侧数据服务", 11, False, NAVY, 0),
    ], fill=SOFT)
    opens = [
        ("开放边界 A", "湖仓 / Catalog", "开放格式、可替换后端，不重建通用栈"),
        ("开放边界 B", "模型 / Agent", "多模型多Agent；统一身份与证据"),
        ("开放边界 C", "API / 渠道", "对接CAMARA/聚合商，不垄断消费入口"),
    ]
    for i, (a, b, c) in enumerate(opens):
        card(s, Inches(0.45 + i * 4.2), Inches(5.35), Inches(4.0), Inches(1.25), [
            (a, 10, True, CORAL, 1),
            (b, 13, True, NAVY, 2),
            (c, 10, False, MUTED, 0),
        ], fill=WARN_BG)
    footer(s, 15, total, "05 公司定位")
    slides_meta.append("05控制点")

    # ========== 16 Capability + conclusion ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "05  CAPABILITY & CONCLUSION", "能力自评与战略定位结论：成为横向组件，不当通用挑战者")
    thesis_box(s, "用 AIR Net 数据引擎抢占「电信语义—任务适用性—近源执行—有界供数」四位一体控制点；以 ZSM 029 / SA2·SA5 把接口与语义写成标准事实，以场景闭环证明价值——而不是先宣称拥有完整 6G Data Fabric。")
    scores = [
        ("自智/Agent场景", "4.0", "AIR Net+Fault Agent有试点与认证"),
        ("语义/KG生产化", "3.5", "故障域强；缺跨RAN/Core标准语义"),
        ("标准接口话语权", "3.0", "ZSM029在手；SA2/SA5需加码"),
        ("通用Fabric产品", "1.5", "不宜与IT巨头/Nokia正面比完整度"),
    ]
    for i, (t, v, n) in enumerate(scores):
        card(s, Inches(0.45 + i * 3.2), Inches(1.9), Inches(3.05), Inches(1.45), [
            (t, 11, False, MUTED, 2),
            (v, 22, True, TEAL, 2),
            (n, 9, False, MUTED, 0),
        ])
    add_table(
        s, Inches(0.45), Inches(3.5), Inches(12.4), Inches(2.0),
        ["能力议题", "位置", "映射", "含义"],
        [
            ["数据产品化与契约", "邻近", "R8·T1/T7", "从资产目录升级为Owner/SLO/任务适用性/退出"],
            ["元数据事件化", "探索", "R1/R5·T2", "优先变更→影响分析与血缘闸门"],
            ["RAN/边缘子Fabric", "有载体", "R2/R3·T3", "优势×空白重叠，适合时间盒PoC"],
            ["Agent有界执行", "相对亮点", "R7·T4", "最短延长线：用数Agent→供数工具"],
            ["RAN数据适用性", "关键缺口", "R4·T6", "差异化必争标尺"],
            ["主权策略强制", "相邻", "R6·T4/T7", "目录标签→策略即代码与删除传播"],
        ],
        col_w=[Inches(2.8), Inches(1.5), Inches(2.0), Inches(6.1)],
        font_size=9,
    )
    card(s, Inches(0.45), Inches(5.7), Inches(6.15), Inches(1.0), [
        ("应成为：主航道共用横向数据能力组件", 11, True, TEAL, 2),
        ("服务无线/核网/承载/SMO/行业；统一控制语义+分布式执行；数据引擎升级为产品/任务适用性/证据/供数底座。", 9, False, MUTED, 0),
    ], fill=SOFT)
    card(s, Inches(6.8), Inches(5.7), Inches(6.05), Inches(1.0), [
        ("不应成为：通用 Data Fabric 平台挑战者", 11, True, CORAL, 2),
        ("不打IT湖仓目录；不复制华为网元命名/不机械站队mesh；不承诺编织进入亚毫秒快环。", 9, False, MUTED, 0),
    ], fill=WARN_BG)
    footer(s, 16, total, "05 公司定位")
    slides_meta.append("05能力结论")

    # ========== 17 Opportunity scoring ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "06  OPPORTUNITY PORTFOLIO", "机会组合：六维加权筛选，避免因技术新颖立项")
    thesis_box(s, "排序维度：战略契合25% · 存量复用20% · 客户牵引20% · 标准窗口15% · 差异化10% · 执行可控10%。分数表达相对优先级，不表达市场规模；O3必须服务O2/O1/O7/O8，O8是跨域供数合规前提。")
    add_table(
        s, Inches(0.35), Inches(1.85), Inches(12.6), Inches(4.7),
        ["机会", "一句话", "加权/5", "角色", "建议"],
        [
            ["O2", "数据引擎→6G数据能力组件外溢", "4.55", "P0 主航道", "首选主攻"],
            ["O3", "ZSM029 + SA2/SA5 标准双入口", "4.30", "P0 放大器", "首选主攻"],
            ["O7", "NDT+Agent高风险动作证据闸门", "4.10", "P1 差异化", "并行主攻"],
            ["O1", "RAN近源流式元数据/子Fabric PoC", "4.05", "P1 技术期权", "中期押注"],
            ["O6", "国内运营商显式数据产品试点", "3.75", "P1 商业验证", "中期绑定"],
            ["O8", "跨路径数据主权与策略即代码", "3.45", "P1 合规底座", "必备底座"],
            ["O4", "承载SLA与数据策略语义映射", "3.35", "P2 路标接口", "路标建议"],
            ["O5", "终端/行业侧轻量数据代理", "2.45", "P3 观察期权", "低成本观察"],
        ],
        col_w=[Inches(0.9), Inches(5.2), Inches(1.2), Inches(2.4), Inches(2.0)],
        font_size=10,
    )
    footer(s, 17, total, "06 机会选择")
    slides_meta.append("06机会组合")

    # ========== 18 Main opportunities ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "06  MAIN ATTACKS", "主攻机会：落到买方任务、最小交付包与止损线")
    thesis_box(s, "中兴最优解是「数据引擎外溢 + 标准卡位 + RAN近源任务适用性+ 动作/主权双证据」；用跨场景复用、闭环收益、可回滚性与策略持续强制证明「可信供数」，而不是用功能清单证明「拥有Fabric」。")
    ops = [
        ("O2 首选", "数据引擎外溢为能力组件",
         "买方：无线优化对象对齐；OSS故障/节能/投诉复用；核网/API上游可信供给。",
         "交付：语义Registry+五类产品模板；目录/血缘/订阅/策略四工具；两后端两产品线可移植。",
         "止损：9个月仍不能跨第二场景复用，或每次接入仍需项目定制→降级为OSS内部能力。"),
        ("O3 首选", "标准双入口卡位",
         "买方/场景：用参考实现影响ZSM029与SA2/SA5互操作语义，而非预设最终文本。",
         "交付：语义/任务适用性信息模型；DMA服务与生命周期；DCP类总线/DCCF-NWDAF双栈映射。",
         "止损：连续两会期无运营商联署或工作组讨论→收缩议题。"),
        ("O1 中期", "RAN近源子Fabric PoC",
         "边界：一种高频遥测+一种消费者；不进<10ms同步；不建中心化原始湖。",
         "验收：标注时延/资源、字节减量、断链可用、任务适用性对模型/闭环改善。",
         "止损：收益不覆盖站点开销，或必须侵入快环→停止产品化。"),
        ("O7 并行", "NDT+Agent证据闸门",
         "买方买的是降低错误变更、缩短审批、可证明回滚，不是「一个孪生」。",
         "交付：快照/保真度/滞后/误差门槛；身份委托/风险预算/灰度熔断。",
         "止损：误差不可标定或收益不超人工基线→保留分析辅助。"),
        ("O8 底座", "跨路径主权策略即代码",
         "用途/同意/驻留/保留/删除贯穿查询、API、导出、向量与训练。",
         "交付：策略DSL+四类执行点适配器+决策/例外证据。",
         "止损：无法脱离项目定制或开销超预算→收缩为管理域参考架构。"),
    ]
    for i, (tag, title, a, b, c) in enumerate(ops):
        card(s, Inches(0.35 + i * 2.58), Inches(1.85), Inches(2.5), Inches(4.75), [
            (tag, 10, True, TEAL, 2),
            (title, 12, True, NAVY, 6),
            (a, 9, False, MUTED, 5),
            (b, 9, False, INK, 5),
            (c, 9, False, CORAL, 0),
        ])
    footer(s, 18, total, "06 机会选择")
    slides_meta.append("06主攻机会")

    # ========== 19 Supporting + resources ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "06  SUPPORTING & DEPENDENCY", "配合项有触发条件；资源不是八支平行队伍")
    thesis_box(s, "依赖顺序：O2是共用内核 → O3放大并约束O2 → O1/O7/O8分别提供近源、动作与主权证据 → O6验证客户是否为结果付费；O4/O5只能消费前述成果，不能反向拉出两套新平台。")
    card(s, Inches(0.45), Inches(1.85), Inches(4.0), Inches(3.5), [
        ("共享核心 55–65%", 14, True, WHITE, 6),
        ("O2 + O3", 16, True, LIME, 6),
        ("语义、任务适用性、契约、工具接口与标准参考实现由同一核心团队负责；标准文稿必须来自可运行代码，核心代码必须对齐标准对象。", 11, False, MIST, 0),
    ], fill=NAVY)
    card(s, Inches(4.65), Inches(1.85), Inches(4.0), Inches(3.5), [
        ("差异验证 25–35%", 14, True, NAVY, 6),
        ("O1 + O7 + O8", 16, True, TEAL, 6),
        ("分别验证分布式近源执行、高风险动作证据与跨路径主权强制。三者共用O2语义/契约，不另造目录与策略体系。", 11, False, MUTED, 0),
    ], fill=SOFT)
    card(s, Inches(8.85), Inches(1.85), Inches(4.0), Inches(3.5), [
        ("客户与期权 10–15%", 14, True, NAVY, 6),
        ("O6 + O4 + O5", 16, True, CORAL, 6),
        ("O6负责商业证伪；O4/O5仅保留接口与观察资源。O6升级需业务Owner、多厂商数据、结果计量与联合案例。", 11, False, MUTED, 0),
    ], fill=WARN_BG)
    card(s, Inches(0.45), Inches(5.55), Inches(6.15), Inches(1.15), [
        ("集中火力", 12, True, TEAL, 2),
        ("优先保证O2+O3，并行验证O7/O8；O1软件侧时间盒；O6专家组牵线；O4/O5路标观察。先自用验证再产品化。", 10, False, MUTED, 0),
    ])
    card(s, Inches(6.8), Inches(5.55), Inches(6.05), Inches(1.15), [
        ("明确不选 / 缓选", 12, True, CORAL, 2),
        ("不自建通用企业Fabric；不押注独立数据面网元胜负手；不为ZB级感知建全量湖；治理成熟前不推无边界Agent改网。", 10, False, MUTED, 0),
    ])
    footer(s, 19, total, "06 机会选择")
    slides_meta.append("06资源依赖")

    # ========== 20 Strategy overview ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "07  STRATEGY OVERVIEW", "具体策略：先卡位叙事与标准，再加深原型，后铺开近源与试点")
    thesis_box(s, "策略总断言：先把数据引擎做成主航道共用的「可信供数控制面」——用标准写下语义与接口，用近源能力守住RAN数据适用性，用动作证据与主权策略约束自治和跨组织流通；其余一律后置。【D】条线可推，【R】需公司决策。")
    strategies = [
        ("1【D】", "数据引擎战略叙事", "90天白皮书对齐R/T/友商/主攻位"),
        ("2【D】", "标准双入口卡位", "ZSM029参考实现+SA2/SA5≥2篇有效输入"),
        ("3【D】", "语义层与五类产品", "故障/节能/移动性/QoE/模型特征"),
        ("4【D】", "Agentic供数接口", "MCP/OpenAPI+IPOE；Reasoner/Actor分离"),
        ("5【D+R】", "RAN近源PoC", "12–18月时间盒；不进<10ms"),
        ("6【R】", "跨线虚拟团队", "统一对象/任务适用性/北向；禁重复造目录"),
        ("7【D】", "NDT证据链", "快照/误差/灰度/回滚成放行条件"),
        ("8【R】", "运营商试点与路标", "独立ROI；承载映射与API写入路标"),
        ("9【D+R】", "Build/Partner/Buy", "自研语义/任务适用性近源证据；合作湖仓模型"),
        ("10【R】", "阶段门与复盘", "G0–G4；允许停止"),
        ("11【D+R】", "主权策略即代码", "跨查询/API/导出/向量/训练强制"),
    ]
    for i, (n, t, d) in enumerate(strategies):
        col, row = i % 4, i // 4
        if i >= 11:
            break
        # last row has 3 items - place 11 in remaining
        card(s, Inches(0.4 + col * 3.2), Inches(1.85 + row * 1.55), Inches(3.05), Inches(1.4), [
            (n, 10, True, TEAL, 1),
            (t, 12, True, NAVY, 2),
            (d, 9, False, MUTED, 0),
        ])
    # BPB strip
    bpb = s.shapes.add_textbox(Inches(0.45), Inches(6.5), Inches(12.4), Inches(0.4))
    write_box(bpb, [("Build：语义/任务适用性/近源Agent/产品契约与动作证据　｜　Partner：湖仓Catalog流批/模型/隐私计算　｜　Buy：连接器扫描可观察工具", 10, False, NAVY)])
    footer(s, 20, total, "07 策略建议")
    slides_meta.append("07策略总览")

    # ========== 21 Rhythm gates metrics ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "07  RHYTHM · GATES · RISK", "实施节奏、阶段门与风险：每一步都能加码、转向或停止")
    thesis_box(s, "全部策略遵循「需求驱动 + 证据分层 + 时间盒」。标准成功≠产品成功；产品演示≠跨厂商互操作。若12个月内仍无法形成至少两类可复用数据产品与一篇有效标准输入，应复盘主攻是否过于分散。")
    timeline = [
        ("0–3月", "看齐与卡位", "叙事；冻结O2/O3；ZSM029与首批文稿；五类产品Owner"),
        ("3–9月", "原型与证据", "语义/供数MVP；非故障闭环扩展；任务适用性与主权DSL v0"),
        ("9–18月", "近源与试点", "RAN PoC；1个运营商显式试点；证据与策略进基线"),
        ("18–36月", "产品化收敛", "随Rel-21沉淀进主航道；API只映射已产品化能力"),
    ]
    for i, (y, t, d) in enumerate(timeline):
        card(s, Inches(0.4 + i * 3.2), Inches(1.85), Inches(3.05), Inches(1.55), [
            (y, 11, True, TEAL, 2),
            (t, 13, True, NAVY, 3),
            (d, 9, False, MUTED, 0),
        ])
    gates = [
        ("G0", "资产核验", "五张清单；无真实资产不进G1"),
        ("G1", "双场景原型", "两类场景两种后端；否则降级"),
        ("G2", "工程基线", "性能/权限/证据/升级回退"),
        ("G3", "客户验证", "Owner+对照基线；可归因审计"),
        ("G4", "产品/标准收敛", "两条主航道+互操作+商业模型"),
    ]
    for i, (g, t, d) in enumerate(gates):
        card(s, Inches(0.4 + i * 2.55), Inches(3.6), Inches(2.45), Inches(1.35), [
            (g, 12, True, CORAL, 1),
            (t, 11, True, NAVY, 2),
            (d, 9, False, MUTED, 0),
        ], fill=SOFT)
    risks = [
        ("平台化过度", "无新增消费者→冻结通用功能"),
        ("产品线碎片化", "绕过公共schema→架构否决"),
        ("标准—产品脱节", "无实现→停扩写并绑定Owner"),
        ("近源开销过大", "超预算→减代理或终止O1"),
        ("Agent越权", "证据不全→退回建议模式"),
        ("主权策略失效", "跨路径不一致→停新路径"),
        ("ROI无法归因", "无基线→不进试点/不对外宣称"),
    ]
    for i, (t, d) in enumerate(risks):
        card(s, Inches(0.35 + i * 1.85), Inches(5.15), Inches(1.78), Inches(1.5), [
            (t, 10, True, NAVY, 3),
            (d, 8, False, MUTED, 0),
        ])
    footer(s, 21, total, "07 策略建议")
    slides_meta.append("07节奏风险")

    # ========== 22 AP table ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "08  ACTION PROGRAMS", "关键 AP：按共同控制点组织，而非按部门各自立项")
    thesis_box(s, "每个AP必须同时具备业务/产品Owner、技术Owner、标准接口（如适用）、可运行交付物、量化验收和停止条件。没有真实消费者、没有基线、没有退出门的任务，不进入清单。")
    add_table(
        s, Inches(0.3), Inches(1.8), Inches(12.7), Inches(4.9),
        ["AP", "内容", "关键交付物", "验收/决策门", "优先级"],
        [
            ["AP0", "存量资产盘点", "代码/接口/数据/标准/客户五清单", "关键资产有Owner；BPB决策", "P0"],
            ["AP1", "可信供数控制面章程", "C1–C4边界、对象模型、开放边界", "两产品线签字；进G1", "P0"],
            ["AP2", "ZSM029+SA2/SA5标准包", "DMA参考实现；语义/任务适用性/双栈提案", "联署+有效输入+产品同步", "P0"],
            ["AP3", "语义包与任务适用性信封v1", "核心对象+质量规则+评测集", "跨两域；准确率/覆盖门槛", "P0"],
            ["AP4", "五类产品+供数工具", "契约模板；四类MCP/OpenAPI工具", "两类产品两类消费者两后端", "P0"],
            ["AP5", "Agent身份策略证据运行时", "身份委托租约白名单证据schema", "高风险100%过策略；可回放", "P0/P1"],
            ["AP6", "NDT高风险动作闸门", "快照/误差/灰度/熔断/回滚链", "历史回放+影子运行；超差退回", "P1"],
            ["AP7", "RAN近源Agent时间盒", "流内标注/任务适用性/断链/异步证据", "资源P99达标否则停止", "P1"],
            ["AP8", "运营商灯塔与独立ROI", "业务问题+对照+成本收益模型", "持续使用；转版本/合同", "P1"],
            ["AP9", "主航道产品化与互操作", "版本清单/兼容矩阵/开放SDK", "两产品线+异构后端+第三方", "P1/P2"],
            ["AP10", "跨路径主权策略即代码", "DSL+四路径执行点+例外证据", "高敏数据跨路径一致+删除传播", "P1"],
        ],
        col_w=[Inches(0.85), Inches(2.6), Inches(3.5), Inches(3.7), Inches(1.0)],
        font_size=8,
    )
    footer(s, 22, total, "08 关键AP")
    slides_meta.append("08 AP总表")

    # ========== 23 90 days + D1-D6 ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "08  90 DAYS & DECISIONS", "前90天六个输出 + 公司层六个待裁决问题")
    thesis_box(s, "AP总断言：先用90天完成「一个Owner、两类数据产品、一套标准—代码映射、两个带退出门的PoC」；随后只对跨场景可复用、客户价值可归因、风险证据完整的能力加码。")
    outs = [
        ("输出1", "唯一组合Owner", "Sponsor+组合负责人+C1–C4技术Owner"),
        ("输出2", "资产事实底稿", "AIR Net/引擎/Co-Sight/NDT/NEF/边缘可复用证据"),
        ("输出3", "两类种子数据产品", "有Owner、消费者、基线与退出条件"),
        ("输出4", "标准—代码映射", "每个主张对应模块/对象/接口/测试"),
        ("输出5", "PoC资源与红线", "O1/O7/O8预算、边界、停止阈值"),
        ("输出6", "首个客户问题", "愿提供多厂商数据与业务基线；否则先内部验证"),
    ]
    for i, (n, t, d) in enumerate(outs):
        col, row = i % 3, i // 3
        card(s, Inches(0.45 + col * 4.2), Inches(1.85 + row * 1.35), Inches(4.0), Inches(1.2), [
            (f"{n}  {t}", 12, True, NAVY, 2),
            (d, 10, False, MUTED, 0),
        ], accent=TEAL)
    decisions = [
        ("D1", "数据引擎是OSS内部能力，还是公司级横向组件？→建议后者，以两产品线复用为条件"),
        ("D2", "谁拥有电信语义与任务适用性最终定义权？→跨线架构Owner；产品线仅域扩展"),
        ("D3", "标准投入是否绑定参考实现与客户联署？→绑定；无代码与运营商问题不进P0"),
        ("D4", "Agent自动动作允许到哪一级？→低风险有界执行；高风险仿真/灰度/回滚/接管"),
        ("D5", "如何与云/数据平台分工？→掌握语义/任务适用性近源证据；湖仓Catalog模型开放合作"),
        ("D6", "谁对跨路径数据主权执行负责？→治理与安全共有规则；引擎统一执行框架"),
    ]
    for i, (n, t) in enumerate(decisions):
        col, row = i % 2, i // 2
        card(s, Inches(0.45 + col * 6.4), Inches(4.7 + row * 0.7), Inches(6.2), Inches(0.65), [
            (f"{n}  {t}", 9, False, INK, 0),
        ], fill=SOFT if row % 2 == 0 else WHITE)
    footer(s, 23, total, "08 关键AP")
    slides_meta.append("08九十天与裁决")

    # ========== 24 Closing ==========
    s = new_slide(prs)
    bg(s)
    topbar(s, "08  DO / DON'T / VERIFY", "行动摘要与边界：把逻辑收束为可执行纪律")
    thesis_box(s, "产业断言：6G Data Fabric不会以「大一统平台」胜出，而以「统一控制语义 + 分布式执行 + 场景化数据产品 + 有界智能」进入网络。中兴用控制点与证据竞争，而不是用平台名竞争。")
    add_table(
        s, Inches(0.45), Inches(1.85), Inches(12.4), Inches(2.6),
        ["做什么", "不做什么", "遗留 / 待验证"],
        [
            ["升级AIR Net为C1–C4共用控制能力；两类产品验证复用", "不另建覆盖所有湖仓/目录/模型/协议的大平台", "内部资产范围、代码权属、跨线Owner"],
            ["ZSM029+SA2/SA5建立语义/任务适用性/接口/测试话语权", "不押注独立数据面名称；不以提案数代替采纳", "Rel-20/21最终能力包与运营商联署"],
            ["O1/O7/O8验证近源、可信自治与主权强制并设停止线", "Fabric不进快环同步单点；Agent无证据不改网", "站点开销、任务适用性增益、NDT误差、策略一致率"],
            ["O6验证客户是否为场景结果付费；独立ROI", "不因「建平台」预算先做重资产集成", "灯塔场景、持续使用、转版本/合同"],
        ],
        col_w=[Inches(4.3), Inches(4.2), Inches(3.9)],
        font_size=9,
    )
    card(s, Inches(0.45), Inches(4.7), Inches(12.4), Inches(1.9), [
        ("最终边界", 13, True, CORAL, 4),
        ("本胶片基于截至2026年8月的标准进度、公开产品与研究主张推演，不等于3GPP已采纳方案，也不构成中兴正式技术路线或市场承诺。", 11, False, INK, 4),
        ("真正的趋势验证点：Rel-21规范文本 · 跨厂商互操作 · 现网闭环收益 · 可持续商业收入。", 11, True, NAVY, 4),
        ("完整论证与引用见：reports/6g-data-fabric-industry-trends-first-four-sections.html", 10, False, MUTED, 0),
    ], fill=WARN_BG)
    footer(s, 24, total, "结语")
    slides_meta.append("结语")

    out = Path("/workspace/reports/6g-data-fabric-strategy-deck.pptx")
    prs.save(out)
    print(f"Wrote {out} with {len(prs.slides)} slides")
    for i, name in enumerate(slides_meta, 1):
        print(f"  {i:02d} {name}")
    return out


if __name__ == "__main__":
    build()
