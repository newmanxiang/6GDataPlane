#!/usr/bin/env python3
"""Generate the 6-slide section 2.3 architecture-route deck.

Output: reports/6g-data-fabric-section-23-deck.pptx
Does not overwrite the older 16-page 2.3/3/4 deck.
"""

from __future__ import annotations

from pathlib import Path

from lxml import etree
from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

ROOT = Path(__file__).resolve().parents[2]
ASSET = ROOT / "reports" / "data-fabric-assets"
OUT = ROOT / "reports" / "6g-data-fabric-section-23-deck.pptx"

W_IN, H_IN = 13.333, 7.5
W, H = Inches(W_IN), Inches(H_IN)
NAVY = RGBColor(0x0B, 0x1F, 0x3A)
TEAL = RGBColor(0x0E, 0x7C, 0x7B)
CORAL = RGBColor(0xC0, 0x39, 0x2B)
AMBER = RGBColor(0xB8, 0x86, 0x0B)
SLATE = RGBColor(0x2C, 0x3E, 0x50)
INK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x5A, 0x6A, 0x7A)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
OFF = RGBColor(0xF4, 0xF7, 0xF8)
PALE = RGBColor(0xE8, 0xF0, 0xF2)
LINE = RGBColor(0xC5, 0xD0, 0xD4)
GOLD = RGBColor(0xC9, 0xA2, 0x27)
SOFT_TEAL = RGBColor(0xD7, 0xEC, 0xEA)
SOFT_AMBER = RGBColor(0xF6, 0xED, 0xD0)
SOFT_NAVY = RGBColor(0xE6, 0xEC, 0xF2)
SOFT_CORAL = RGBColor(0xF8, 0xE6, 0xE4)
FONT = "WenQuanYi Micro Hei"
TOTAL = 6
EMU = 914400


def _set_run_east_asia(run) -> None:
    rpr = run._r.get_or_add_rPr()
    ea = rpr.find(qn("a:ea"))
    if ea is None:
        ea = etree.SubElement(rpr, qn("a:ea"))
    ea.set("typeface", FONT)


def rgb(shape, color: RGBColor) -> None:
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


def lined(shape, fill: RGBColor, border: RGBColor, width: float = 0.75) -> None:
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill
    shape.line.color.rgb = border
    shape.line.width = Pt(width)


def write_box(tf, lines, *, size=11, color=INK, bold=False, align=PP_ALIGN.LEFT, spacing=1.05, anchor=None):
    tf.word_wrap = True
    tf.auto_size = None
    if anchor is not None:
        tf.paragraphs[0].alignment = align
    tf.clear()
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(1)
        p.line_spacing = spacing
        run = p.add_run()
        run.text = line
        run.font.size = Pt(size)
        run.font.color.rgb = color
        run.font.bold = bold
        run.font.name = FONT
        _set_run_east_asia(run)


def add_text(slide, l, t, w, h, lines, **kw):
    box = slide.shapes.add_textbox(Inches(l), Inches(t), Inches(w), Inches(h))
    write_box(box.text_frame, lines, **kw)
    return box


def new_slide(prs):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    bg = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, H)
    rgb(bg, WHITE)
    return s


def header(slide, number: str, title: str) -> None:
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, W, Inches(0.07))
    rgb(bar, TEAL)
    add_text(slide, 0.38, 0.12, 12.55, 0.22, [number], size=10, color=TEAL, bold=True)
    add_text(slide, 0.38, 0.32, 12.55, 0.36, [title], size=20, color=NAVY, bold=True)


def footer(slide, page: int, chapter: str, refs: str = "") -> None:
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.38), Inches(7.22), Inches(12.55), Inches(0.01))
    rgb(line, LINE)
    left = f"6G 数据架构 × 数据编织 · 2.3 架构路线 · {chapter}"
    if refs:
        left = f"{left}    {refs}"
    add_text(slide, 0.38, 7.26, 10.4, 0.20, [left], size=8, color=MUTED)
    add_text(slide, 11.35, 7.26, 1.58, 0.20, [f"{page} / {TOTAL}"], size=8, color=MUTED, align=PP_ALIGN.RIGHT)


def thesis(slide, text: str, top: float = 0.70, height: float = 0.46) -> None:
    box = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.38), Inches(top), Inches(12.55), Inches(height)
    )
    lined(box, PALE, TEAL)
    tf = box.text_frame
    tf.word_wrap = True
    write_box(tf, [text], size=12, color=NAVY, bold=True, spacing=1.05)
    tf.paragraphs[0].space_before = Pt(3)


def card(slide, l, t, w, h, title, body, accent=TEAL, title_size=11, body_size=10, fill=WHITE):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h))
    lined(shp, fill, LINE)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(l), Inches(t), Inches(0.07), Inches(h))
    rgb(bar, accent)
    add_text(slide, l + 0.16, t + 0.07, w - 0.26, 0.26, [title], size=title_size, color=NAVY, bold=True)
    add_text(slide, l + 0.16, t + 0.34, w - 0.26, h - 0.42, body, size=body_size, color=SLATE, spacing=1.06)


def chip(slide, l, t, w, h, text, fill, color=WHITE, size=8):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h))
    rgb(shp, fill)
    add_text(slide, l, t + 0.02, w, h - 0.02, [text], size=size, color=color, bold=True, align=PP_ALIGN.CENTER)


def number_badge(slide, l, t, n, fill=TEAL):
    circ = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(l), Inches(t), Inches(0.26), Inches(0.26))
    rgb(circ, fill)
    add_text(slide, l, t + 0.01, 0.26, 0.24, [str(n)], size=10, color=WHITE, bold=True, align=PP_ALIGN.CENTER)


def evidence_bar(slide, items, y: float = 6.38, h: float = 0.76) -> None:
    box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.38), Inches(y), Inches(12.55), Inches(h))
    lined(box, OFF, LINE)
    n = len(items)
    gap = 0.12
    inner = 12.55 - 0.24
    cw = (inner - gap * (n - 1)) / n
    for i, (label, text, accent) in enumerate(items):
        x = 0.50 + i * (cw + gap)
        add_text(slide, x, y + 0.05, cw, 0.20, [label], size=8, color=accent, bold=True)
        add_text(slide, x, y + 0.24, cw, h - 0.30, [text], size=8, color=SLATE, spacing=1.02)


def add_table(slide, l, t, w, h, rows, col_w=None, font=8.5):
    table_shape = slide.shapes.add_table(len(rows), len(rows[0]), Inches(l), Inches(t), Inches(w), Inches(h))
    table = table_shape.table
    if col_w:
        for i, cw in enumerate(col_w):
            table.columns[i].width = Inches(cw)
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell = table.cell(r, c)
            cell.text = ""
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            fill = NAVY if r == 0 else (OFF if r % 2 else WHITE)
            cell.fill.solid()
            cell.fill.fore_color.rgb = fill
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.LEFT
            run = p.add_run()
            run.text = val
            run.font.size = Pt(font)
            run.font.bold = r == 0 or c == 0
            run.font.color.rgb = WHITE if r == 0 else INK
            run.font.name = FONT
            _set_run_east_asia(run)
            cell.text_frame.word_wrap = True
            cell.text_frame.margin_left = Inches(0.05)
            cell.text_frame.margin_right = Inches(0.04)
            cell.text_frame.margin_top = Inches(0.03)
            cell.text_frame.margin_bottom = Inches(0.03)
    return table


def ensure_png(svg_name: str, png_name: str) -> Path:
    png = ASSET / png_name
    svg = ASSET / svg_name
    if png.exists():
        return png
    if svg.exists():
        import cairosvg

        cairosvg.svg2png(url=str(svg), write_to=str(png), output_width=2200)
        return png
    raise FileNotFoundError(png_name)


def fit_picture(slide, path: Path, box_l, box_t, box_w, box_h):
    with Image.open(path) as im:
        ar = im.size[0] / im.size[1]
    box_ar = box_w / box_h
    if ar >= box_ar:
        pw, ph = box_w, box_w / ar
    else:
        ph, pw = box_h, box_h * ar
    pl = box_l + (box_w - pw) / 2
    pt = box_t + (box_h - ph) / 2
    slide.shapes.add_picture(str(path), Inches(pl), Inches(pt), Inches(pw), Inches(ph))
    frame = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(pl), Inches(pt), Inches(pw), Inches(ph))
    frame.fill.background()
    frame.line.color.rgb = LINE
    frame.line.width = Pt(0.75)
    return pl, pt, pw, ph


def layer_box(slide, l, t, w, h, kicker, title, body, fill, title_color=WHITE, body_color=WHITE):
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(l), Inches(t), Inches(w), Inches(h))
    rgb(shp, fill)
    add_text(slide, l + 0.18, t + 0.08, w - 0.36, 0.20, [kicker], size=9, color=GOLD, bold=True)
    add_text(slide, l + 0.18, t + 0.28, w - 0.36, 0.28, [title], size=14, color=title_color, bold=True)
    add_text(slide, l + 0.18, t + 0.58, w - 0.36, h - 0.68, [body], size=10, color=body_color, spacing=1.05)


def slide_p1(prs) -> None:
    s = new_slide(prs)
    header(s, "2.3.1  ·  ARCHITECTURE CHOICE", "6G数据能力不会收敛为单一Fabric；三条路线围绕同一组控制能力竞争")
    thesis(s, "三条路线是不同起点，不是“谁更接近Fabric”的排名；它们分别优先解决低风险演进、近源执行与产品化速度。")

    constraints = [
        ("约束 1  ·  时标", "事实在近源", "无线状态、移动性和断链生存，要求毫秒执行留在网元、边缘或域控制器。"),
        ("约束 2  ·  复用", "语义要跨域", "模型与产品跨RAN、Core、OSS/BSS复用，需要稳定对象、上下文、QoD和版本。"),
        ("约束 3  ·  成本", "少搬运、多计算", "感知、训练和遥测规模推动过滤、特征化与推理向源侧下沉，而不是默认集中。"),
        ("约束 4  ·  风险", "动作要回证", "Agent输出会改变真实网络，数据、模型、策略、动作与结果必须形成证据链。"),
    ]
    for i, (kicker, title, body) in enumerate(constraints):
        y = 1.28 + i * 1.12
        box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.38), Inches(y), Inches(4.15), Inches(1.04))
        lined(box, WHITE, LINE)
        number_badge(s, 0.50, y + 0.12, i + 1)
        add_text(s, 0.84, y + 0.08, 3.55, 0.18, [kicker], size=8.5, color=TEAL, bold=True)
        add_text(s, 0.84, y + 0.26, 3.55, 0.24, [title], size=13, color=NAVY, bold=True)
        add_text(s, 0.50, y + 0.54, 3.87, 0.44, [body], size=10, color=SLATE, spacing=1.04)

    hub = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.68), Inches(3.05), Inches(1.72), Inches(1.55))
    rgb(hub, NAVY)
    add_text(s, 4.78, 3.28, 1.52, 1.10, ["控制权", "如何分配"], size=13, color=WHITE, bold=True, align=PP_ALIGN.CENTER, spacing=1.15)
    arr_l = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(4.68), Inches(2.55), Inches(1.72), Inches(0.28))
    rgb(arr_l, TEAL)
    arr_r = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(4.68), Inches(4.78), Inches(1.72), Inches(0.28))
    rgb(arr_r, TEAL)

    routes = [
        (TEAL, "Ericsson  ·  存量联邦", "连接既有数据岛", "以复杂协调换迁移连续性。权威源与存量产品不可跳过，统一的是治理视图，不是全部运行时。"),
        (AMBER, "Huawei  ·  网络原生拓扑", "重构数据拓扑", "以新平面复杂度换近源控制。把多源、多处理、多汇做成可编排执行，而不是先建企业Catalog。"),
        (NAVY, "Nokia  ·  分层商品化", "组合数据与自治软件", "以分层SKU换产品化速度。先让能力可销售、可组合，再验证各层是否共享同一控制体系。"),
    ]
    for i, (accent, kicker, title, body) in enumerate(routes):
        y = 1.28 + i * 1.50
        box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.58), Inches(y), Inches(6.35), Inches(1.40))
        lined(box, WHITE, LINE)
        bar = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(6.58), Inches(y), Inches(0.08), Inches(1.40))
        rgb(bar, accent)
        add_text(s, 6.82, y + 0.08, 5.95, 0.20, [kicker], size=9, color=accent, bold=True)
        add_text(s, 6.82, y + 0.28, 5.95, 0.26, [title], size=14, color=NAVY, bold=True)
        add_text(s, 6.82, y + 0.58, 5.95, 0.72, [body], size=10.5, color=SLATE, spacing=1.05)

    band = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.38), Inches(5.82), Inches(12.55), Inches(1.28))
    lined(band, SOFT_TEAL, TEAL)
    add_text(s, 0.54, 5.90, 12.23, 0.22, ["共同绕不开的不是平台名称，而是四类控制能力"], size=11, color=NAVY, bold=True)
    for i, label in enumerate(["跨域语义", "QoD / 产品契约", "近源运行时", "动作证据"]):
        x = 0.54 + i * 3.10
        pill = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(6.22), Inches(2.95), Inches(0.68))
        rgb(pill, TEAL)
        add_text(s, x, 6.38, 2.95, 0.38, [label], size=13, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    footer(s, 1, "2.3.1")


def slide_p2(prs) -> None:
    s = new_slide(prs)
    header(s, "2.3.2  ·  STANDARD BOUNDARY", "标准先冻结外部行为，不会先冻结统一平台")
    thesis(s, "标准更关注跨厂商必须一致的对象和接口，不替厂商选择内部拓扑，因此三条路线可以长期并存。")

    layers = [
        (4.88, RGBColor(0x1F, 0x4E, 0x5F), "LAYER 3  ·  外部产品行为", "API  ·  SLA  ·  用途  ·  计量  ·  结算", "消费者看见的是可订购、可计量、可追责的服务，而不是内部网元名称。"),
        (3.18, TEAL, "LAYER 2  ·  跨域控制语义", "稳定ID  ·  最小元数据  ·  QoD  ·  授权  ·  动作证据", "跨域复用真正依赖的是对象能否对齐、质量能否声明、动作能否回证。"),
        (1.48, NAVY, "LAYER 1  ·  网络权威事实", "RAN  ·  Core  ·  OAM  ·  O-RAN接口", "无线、会话和运维事实仍由网络域产生；标准先承认这些权威源，而不是另造一个总库。"),
    ]
    for y, fill, kicker, title, body in layers:
        layer_box(s, 0.38, y, 7.20, 1.52, kicker, title, body, fill)
    for y in (4.58, 2.88):
        arr = s.shapes.add_shape(MSO_SHAPE.UP_ARROW, Inches(3.68), Inches(y), Inches(0.42), Inches(0.28))
        rgb(arr, GOLD)

    card(
        s,
        7.78,
        1.48,
        5.15,
        2.28,
        "较可能先冻结",
        ["角色、稳定标识、最小元数据、交付控制、QoD/授权/证据挂钩点，以及一致性测试。ZSM 029对注册、发现、资产和工作流的研究也指向这一方向。"],
        TEAL,
        title_size=13,
        body_size=11,
        fill=SOFT_TEAL,
    )
    card(
        s,
        7.78,
        3.90,
        5.15,
        2.28,
        "仍然保持开放",
        ["既有NF增强、新NF、边缘Agent、管理侧服务、湖仓、消息运行时，以及是否存在独立Fabric，都仍是实现选择。标准不替厂商选定内部拓扑。"],
        AMBER,
        title_size=13,
        body_size=11,
        fill=SOFT_AMBER,
    )
    evidence_bar(
        s,
        [
            ("制度含义", "竞争从“组件是否存在”转向“接口能否互操作、后端能否替换、责任能否跨域传递”。", TEAL),
            ("停止线", "Kafka、湖仓、完整知识图谱或独立Fabric都不是标准预设终点。", AMBER),
        ],
        y=6.32,
        h=0.80,
    )
    footer(s, 2, "2.3.2", "[S1][S5][S6][S26][S29][S7][S43][S15][S16]")


def slide_p3(prs, fig18: Path, north: Path) -> None:
    s = new_slide(prs)
    header(s, "2.3.4  ·  ERICSSON", "Ericsson以联邦保留存量：迁移连续性最强，跨产品一致性是关键风险")
    thesis(s, "数据在域内加工、按需联邦消费；统一的是治理视图，不是全部运行时。官方血缘是 Mediation→Telco DataOps，不是 EDCA→DataOps。")

    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.38), Inches(1.26), Inches(7.72), Inches(5.00))
    lined(panel, OFF, LINE)
    fit_picture(s, fig18, 0.50, 1.34, 7.48, 2.95)
    chip(s, 0.56, 1.40, 1.55, 0.24, "官方架构  Figure 18", NAVY, WHITE, 7.5)
    add_text(s, 0.50, 4.30, 7.48, 0.20, ["主图：2026 Data Ingestion Architecture。EDCA/DRG仍在，客户侧DMF与Ericsson侧EFDL/Data Fabric构成联邦边界。"], size=8, color=MUTED)

    fit_picture(s, north, 0.50, 4.52, 3.55, 1.64)
    chip(s, 0.56, 4.58, 1.35, 0.22, "参考架构  North Star", TEAL, WHITE, 7.5)
    add_text(
        s,
        4.16,
        4.52,
        3.80,
        1.64,
        [
            "① 近源摄取仍保留：EDCA、DRG在Figure 18继续存在。",
            "② 联邦边界被扩展：客户侧DMF连接Ericsson侧EFDL/Data Fabric。",
            "③ 治理范围上移：North Star增加目录、质量、血缘、语义/KG和数据产品。",
        ],
        size=9.5,
        color=SLATE,
        spacing=1.12,
    )

    card(s, 8.24, 1.26, 4.71, 1.58, "数据与控制如何流动", ["数据在域内采集加工，经联邦访问和智能移动供跨域消费。目录、策略和治理提供统一视图；执行仍分散在DataOps、NWDAF、EIAP/rApps和域系统。"], TEAL, body_size=10)
    card(s, 8.24, 2.96, 4.71, 1.58, "为什么选择联邦", ["RAN、Core、OSS/BSS和边缘权威源天然分散；Mediation、NWDAF、SMO/RIC和客户湖仓不可跳过。先连接数据岛，再逐步补齐治理。"], NAVY, body_size=10)
    card(s, 8.24, 4.66, 4.71, 1.60, "竞争含义", ["优势是渐进接入、多后端、迁移风险低。代价是跨产品Schema、QoD、策略和版本可能长期碎片化。"], AMBER, body_size=10, fill=SOFT_AMBER)

    evidence_bar(
        s,
        [
            ("已证明", "Figure 18延续EDCA/DRG；Mediation、EIAP、NWDAF分别有产品或部署锚点。", TEAL),
            ("关键边界", "官方产品血缘是 Mediation→Telco DataOps，不是 EDCA→DataOps。", CORAL),
            ("决定性验证", "同一版本化数据产品能否跨DataOps、EIAP、NWDAF及第三方后端复用，无需项目级重写。", AMBER),
        ],
    )
    footer(s, 3, "2.3.4", "[S9][S10][S21][S30][S35][S36][S57][S58]")


def slide_p4(prs, huawei: Path) -> None:
    s = new_slide(prs)
    header(s, "2.3.5  ·  HUAWEI", "Huawei重构数据拓扑：近源执行控制最强，电信级可靠性是验证门")
    thesis(s, "DO编排拓扑，DA近源处理，DCP异步分发。这首先是6G数据面机制，不能把“补成Fabric”当成唯一终点。")

    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.38), Inches(1.26), Inches(7.72), Inches(5.00))
    lined(panel, OFF, LINE)
    fit_picture(s, huawei, 0.50, 1.36, 7.48, 3.55)
    chip(s, 0.56, 1.42, 1.55, 0.24, "研究架构  非3GPP方案", AMBER, NAVY, 7.5)
    notes = [
        (TEAL, "① DO", "能力注册、操作DAG分解、选点与策略下发。登记的是执行能力，不是通用资产目录。"),
        (NAVY, "② DA / DPF / DSF", "在UE、RAN、边缘和Core近源采集、处理、推理与存储。"),
        (CORAL, "③ DCP / Data Spine", "以Pub/Sub解耦生产者和多消费者，服务AI/ISAC扇出。"),
    ]
    for i, (accent, title, body) in enumerate(notes):
        x = 0.50 + i * 2.50
        add_text(s, x, 5.00, 2.40, 0.20, [title], size=9.5, color=accent, bold=True)
        add_text(s, x, 5.20, 2.40, 0.92, [body], size=9, color=SLATE, spacing=1.04)

    card(s, 8.24, 1.26, 4.71, 1.58, "控制流", ["服务意图进入DO。DO选择执行能力、生成数据处理拓扑，并下发访问、隐私与资源策略。"], TEAL, body_size=10.5)
    card(s, 8.24, 2.96, 4.71, 1.58, "数据流", ["源DA发布数据，DCP异步分发；DA/DPF沿途过滤、压缩、特征化和推理，上游模型输出可成为下游输入。"], NAVY, body_size=10.5)
    card(
        s,
        8.24,
        4.66,
        4.71,
        1.60,
        "为什么需要新平面",
        ["AI/ISAC的多源、多处理、多汇和派生数据链，不完全适配围绕控制消息与连接设计的CP/UP。AUTINOps不是DCP商用证明。"],
        AMBER,
        body_size=10,
        fill=SOFT_AMBER,
    )
    evidence_bar(
        s,
        [
            ("原型信号", "DCP公开实验约2ms；10 broker、128KB消息约2,394.6MB/s。", TEAL),
            ("比较局限", "DCP移除持久化，RocketMQ对照开启持久化，不能外推为同功能全面领先。", CORAL),
            ("决定性验证", "同等持久化条件下的跨站故障、移动性、断链回退、多租户SLA和第三方算子。", AMBER),
        ],
    )
    footer(s, 4, "2.3.5", "[S12][S14][S37][S38]")


def slide_p5(prs, nokia: Path) -> None:
    s = new_slide(prs)
    header(s, "2.3.6  ·  NOKIA", "Nokia分层商品化：产品进入现网最快，统一控制与开放性仍待证明")
    thesis(s, "Data Suite是数据管理层，AN Fabric是智能消费层；动作仍回OSS/RIC/SON，数据默认留域。两套Fabric不是同一层。")

    panel = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.38), Inches(1.26), Inches(7.72), Inches(5.00))
    lined(panel, OFF, LINE)
    add_text(s, 0.52, 1.32, 4.55, 0.22, ["主视觉  ·  自绘五段链"], size=9, color=TEAL, bold=True)

    stages = [
        (NAVY, "1  域数据底座", "Domain lakehouse  ·  本地权威事实"),
        (TEAL, "2  Common Fabric / Lakehouse", "适配  ·  抽象  ·  联邦访问，而非强制集中"),
        (TEAL, "3  Data Suite", "语义  ·  QoD  ·  血缘  ·  数据产品"),
        (AMBER, "4  AN Fabric / AN Apps", "Sense  ·  Think  ·  Act  智能消费层"),
        (NAVY, "5  域控制器 + API / Marketplace", "OSS / RIC / SON 动作  ·  商业外延"),
    ]
    for i, (fill, title, body) in enumerate(stages):
        y = 1.56 + i * 0.88
        box = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.52), Inches(y), Inches(4.55), Inches(0.72))
        rgb(box, fill)
        add_text(s, 0.66, y + 0.06, 4.27, 0.28, [title], size=12, color=WHITE, bold=True)
        add_text(s, 0.66, y + 0.34, 4.27, 0.30, [body], size=9.5, color=WHITE)
        if i < len(stages) - 1:
            arr = s.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, Inches(2.62), Inches(y + 0.70), Inches(0.22), Inches(0.16))
            rgb(arr, GOLD)

    fit_picture(s, nokia, 5.20, 1.56, 2.72, 2.55)
    chip(s, 5.26, 1.62, 2.20, 0.22, "官方图  仅证智能消费层", AMBER, NAVY, 7.5)
    add_text(
        s,
        5.20,
        4.20,
        2.72,
        1.90,
        [
            "官方AN Fabric图只证明Sense–Think–Act智能层。",
            "Data Suite、域数据底座和公共湖仓不在这张图里，必须靠左侧自绘链路补齐。",
            "高风险动作仍经AN Apps回到域控制器。",
        ],
        size=9.5,
        color=SLATE,
        spacing=1.10,
    )

    card(s, 8.24, 1.26, 4.71, 1.58, "必须分层", ["Data Suite管目录、语义、质量、血缘和产品；AN Fabric管智能消费与编排。数据默认留域，公共层只做适配、抽象和联邦访问。"], TEAL, body_size=10)
    card(s, 8.24, 2.96, 4.71, 1.58, "数据与控制如何流动", ["域湖仓完成本地加工，经公共层进入Data Suite，再进入Sense。Think之后，Act通过AN Apps调用既有OSS/RIC/SON。"], NAVY, body_size=10)
    card(s, 8.24, 4.66, 4.71, 1.60, "竞争含义", ["优势是SKU可组合、进入现网快。代价是各层可能只在品牌层组合，并形成语义、应用与云后端的软锁定。"], AMBER, body_size=10, fill=SOFT_AMBER)

    evidence_bar(
        s,
        [
            ("域应用已证", "KDDI覆盖20万4G/5G RAN；stc披露超过1万次自动动作；Indosat证明节能应用可扩展。", TEAL),
            ("规模信号", "匿名Tier-1：25万小区、27万报告/秒，仅支持摄取与关联潜力。", AMBER),
            ("决定性验证", "同一契约是否共享、第三方后端/Agent能否双向替换、动作与回滚证据能否贯通。", CORAL),
        ],
    )
    footer(s, 5, "2.3.6", "[S23][S24][S31][S32][S33][S34][S39]")


def slide_p6(prs) -> None:
    s = new_slide(prs)
    header(s, "2.3.3 + 2.3.7  ·  SYNTHESIS", "三条路线不构成成熟度序列；最终胜负由四类接口控制权决定")
    thesis(s, "Ericsson争联邦治理，Huawei争近源运行时，Nokia争语义产品与应用入口。平台地位取决于外部契约，而不是把数据集中到一个名字。")

    add_table(
        s,
        0.38,
        1.24,
        12.55,
        2.58,
        [
            ["比较项", "Ericsson  ·  存量联邦", "Huawei  ·  网络原生拓扑", "Nokia  ·  分层商品化"],
            ["架构起点", "连接既有数据岛", "重构数据处理拓扑", "组合数据与自治软件"],
            ["控制中心", "联邦目录、治理与策略", "DO与网络原生拓扑", "Data Suite + AN Fabric分层"],
            ["执行位置", "域内产品与数据湖", "UE / RAN / 边缘 / Core近源", "域湖仓与OSS / RIC / SON"],
            ["换取优势", "迁移连续性", "近源执行控制", "产品化速度"],
            ["结构性代价", "跨产品协调复杂度", "新平面可靠性与状态复杂度", "多层SKU与软锁定"],
            ["决定性验证", "跨产品、跨后端复用", "同功能可靠性与多厂商测试", "统一契约、动作贯通、后端可替换"],
        ],
        col_w=[1.70, 3.62, 3.62, 3.61],
        font=9,
    )

    controls = [
        ("1  跨域语义与身份", "稳定ID、权威源、配置版本和对象映射，使同一小区、会话、模型能跨接口关联。"),
        ("2  QoD与产品契约", "用途适用性、Owner、SLO、计量、降级与退出，决定数据对特定任务是否可交付。"),
        ("3  近源运行时", "算子放置、策略下发、断链生存和版本回退，决定快环能否留在故障域内。"),
        ("4  动作证据与接口", "数据—模型—策略—动作—结果—回滚的关联，并能被导出、审计与一致性测试。"),
    ]
    for i, (title, body) in enumerate(controls):
        x = 0.38 + i * 3.20
        card(s, x, 3.94, 3.08, 1.42, title, [body], TEAL, title_size=11, body_size=9.5)

    land = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.38), Inches(5.46), Inches(12.55), Inches(1.66))
    lined(land, SOFT_NAVY, NAVY)
    add_text(s, 0.54, 5.52, 12.23, 0.22, ["路线落点"], size=10, color=TEAL, bold=True)
    add_text(
        s,
        0.54,
        5.74,
        12.23,
        0.42,
        ["Ericsson争夺联邦目录与渐进治理控制权。  Huawei争夺数据拓扑与近源运行时控制权。  Nokia争夺语义产品与自治应用入口控制权。"],
        size=11,
        color=NAVY,
        bold=True,
        spacing=1.05,
    )
    add_text(
        s,
        0.54,
        6.16,
        12.23,
        0.42,
        ["真正的平台地位不是把所有数据收到一个平台，而是让跨域消费者遵循自己的语义、QoD和证据契约，同时证明运行时、后端和渠道仍可互操作、可替换。"],
        size=11,
        color=SLATE,
        spacing=1.05,
    )
    add_text(
        s,
        0.54,
        6.58,
        12.23,
        0.42,
        ["竞合边界：设备商更接近网络语义、近源执行与动作权限；云和湖仓更接近规模数据/模型运行时；聚合商更接近跨网分发与结算。三者可以组合，但RAN快环和网元动作权限不能外移。"],
        size=9.5,
        color=MUTED,
        spacing=1.04,
    )
    footer(s, 6, "2.3.3 / 2.3.7", "[S18][S25] 及 P3–P5 厂商证据")


def verify(prs: Presentation) -> None:
    n = len(prs.slides)
    if n != TOTAL:
        raise SystemExit(f"expected {TOTAL} slides, got {n}")

    pics = []
    tables = []
    overflow = []
    for i, slide in enumerate(prs.slides, 1):
        pic_n = 0
        table_n = 0
        for shp in slide.shapes:
            if shp.shape_type == MSO_SHAPE_TYPE.PICTURE:
                pic_n += 1
            if shp.has_table:
                table_n += 1
            right = (shp.left + shp.width) / EMU
            bottom = (shp.top + shp.height) / EMU
            if right > W_IN + 0.03 or bottom > H_IN + 0.03 or shp.left < Emu(-0.02 * EMU) or shp.top < Emu(-0.02 * EMU):
                overflow.append((i, getattr(shp, "name", "?"), round(right, 3), round(bottom, 3)))
        pics.append(pic_n)
        tables.append(table_n)

    if pics[2] != 2:
        raise SystemExit(f"P3 must embed 2 Ericsson images, got {pics[2]}")
    if pics[3] != 1:
        raise SystemExit(f"P4 must embed 1 Huawei image, got {pics[3]}")
    if pics[4] != 1:
        raise SystemExit(f"P5 must embed 1 Nokia image, got {pics[4]}")
    if sum(tables) != 1 or tables[5] != 1:
        raise SystemExit(f"deck must contain exactly 1 table on P6, got {tables}")
    if overflow:
        raise SystemExit(f"shapes overflow canvas: {overflow}")
    print("verify ok:", {"slides": n, "pictures": pics, "tables": tables})


def build() -> Path:
    fig18 = ensure_png("ericsson-data-ingestion-architecture-2026.svg", "ericsson-data-ingestion-architecture-2026.png")
    north = ensure_png("ericsson-ai-ready-data-management-2026.svg", "ericsson-ai-ready-data-management-2026.png")
    huawei = ASSET / "huawei-6g-data-plane-architecture.jpg"
    nokia = ASSET / "nokia-autonomous-network-fabric.png"
    for path in (fig18, north, huawei, nokia):
        if not path.exists():
            raise FileNotFoundError(path)

    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    slide_p1(prs)
    slide_p2(prs)
    slide_p3(prs, fig18, north)
    slide_p4(prs, huawei)
    slide_p5(prs, nokia)
    slide_p6(prs)
    verify(prs)
    prs.save(OUT)
    print(f"wrote {OUT}")
    return OUT


if __name__ == "__main__":
    build()
