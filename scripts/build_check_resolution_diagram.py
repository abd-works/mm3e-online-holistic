"""Build the check-resolution object model class diagram from scratch.

Re-runnable: regenerates all three pages (Trait, Check, Condition) from the
object model.  Edit this script when the model changes — add/move classes,
adjust anchors, update properties — then re-run to produce a clean diagram.

Usage:
    python scripts/build_check_resolution_diagram.py
"""
import sys
sys.path.insert(0, r"c:\Users\thoma\.cursor\skills\drawio-domain-sync\scripts")
import drawio_tools as dt
import xml.etree.ElementTree as ET

dt.EDGE_STYLES["inheritance-orthogonal"] = (
    f"{dt.EDGE_ORTHOGONAL}endArrow=block;endSize=16;endFill=0;html=1;"
)

PATH = r"c:\dev\mm3e-online-holistic\docs\check-resolution\check-resolution-class-diagram.drawio"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _html(name, base=None, stereotype=None, props=None, ops=None, invs=None):
    props = props or []; ops = ops or []; invs = invs or []
    e = dt.escape
    bl = f" : {e(base)}" if base else ""
    st = f'<i style="font-size:9px;color:#888;">{e(stereotype)}</i><br/>' if stereotype else ""
    ph = "".join(f"{e(p)}<br/>" for p in props) or "<br/>"
    oh = "".join(f"{e(o)}<br/>" for o in ops) or "<br/>"
    lbl = (f'<p style="margin:0px;margin-top:4px;text-align:center;">{st}'
           f'<b>{e(name)}{bl}</b></p><hr size="1"/>'
           f'<p style="margin:0px;margin-left:4px;font-size:10px;">{ph}</p><hr size="1"/>'
           f'<p style="margin:0px;margin-left:4px;font-size:10px;">{oh}</p>')
    if invs:
        ih = "".join(f"<i>{e(i[:90]+'...' if len(i)>90 else i)}</i><br/>" for i in invs)
        lbl += f'<hr size="1"/><p style="margin:0px;margin-left:4px;font-size:9px;color:#666;">{ih}</p>'
    return lbl


def _h(np, no, ni, stereo=False):
    s = 3 if ni > 0 else 2
    return max(80, 30 + (np + no + ni) * 16 + s * 8) + (16 if stereo else 0)


def cls(root, name, base=None, stereotype=None, props=None, ops=None, invs=None,
        x=40, y=40, w=300, imp=None):
    """Add a class cell to the page root. Returns the cell element."""
    props = props or []; ops = ops or []; invs = invs or []
    cid = str(dt.next_id(root))
    st = f"\u00ABfrom: {imp}\u00BB" if imp else stereotype
    lbl = _html(name, base, st, props, ops, invs)
    h = _h(len(props), len(ops), len(invs), st is not None)
    sty = dt.CLASS_STYLE_IMPORT if imp else dt.CLASS_STYLE
    c = ET.SubElement(root, "mxCell")
    c.set("id", cid); c.set("value", lbl); c.set("style", sty)
    c.set("vertex", "1"); c.set("parent", "1")
    g = ET.SubElement(c, "mxGeometry")
    g.set("x", str(int(x))); g.set("y", str(int(y)))
    g.set("width", str(int(w))); g.set("height", str(int(h)))
    g.set("as", "geometry")
    return c


def edg(root, src, tgt, etype, label="", ex=None, ey=None, nx=None, ny=None):
    """Add an edge between two cells. Returns the edge cell."""
    return dt.create_edge(root, src.get("id"), tgt.get("id"), etype, label,
                          exit_x=ex, exit_y=ey, entry_x=nx, entry_y=ny)


def add_waypoints(edge_cell, points):
    """Add explicit waypoints to an edge to control orthogonal routing."""
    geo = edge_cell.find("mxGeometry")
    arr = ET.SubElement(geo, "Array"); arr.set("as", "points")
    for wx, wy in points:
        wp = ET.SubElement(arr, "mxPoint")
        wp.set("x", str(wx)); wp.set("y", str(wy))


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

mxfile = dt.create_empty_mxfile()

# ===================================================================
#  PAGE 1 — TRAIT
# ===================================================================
_, R = dt.add_page(mxfile, "Trait")

Trait = cls(R, "Trait", stereotype="\u00ABEntity\u00BB",
    props=["+ character: Character", "+ traitName: String", "+ purchasedRank: Integer"],
    ops=["+ effectiveRank(): Integer",
         "\u2212 conditionPenalty(): Integer",
         "+ realWorldValue(type: MEASUREMENT_TYPE): Number",
         "+ addRank(other: Int, type: MEASUREMENT_TYPE): Int",
         "+ performCheck(dc: DifficultyClass): CheckResult"],
    invs=["effectiveRank = purchasedRank \u2212 sum of active condition penalties",
          "ranks must never be added directly \u2014 convert to measures first"],
    x=40, y=40, w=360)

MT = cls(R, "MEASUREMENT_TYPE", stereotype="\u00ABValueObject\u00BB",
    props=["MASS: Integer = 1", "TIME: Integer = 2",
           "DISTANCE: Integer = 3", "VOLUME: Integer = 4"],
    x=40, y=380, w=260)

Meas = cls(R, "Measurement", stereotype="\u00ABService\u00BB",
    ops=["+ lookup(rank: Int, type: MEASUREMENT_TYPE): Number",
         "+ rankFor(measure: Number, type: MEASUREMENT_TYPE): Int",
         "+ throwingDistanceRank(strRank: Int, massRank: Int): Int",
         "+ travelDistanceRank(timeRank: Int, speedRank: Int): Int",
         "+ travelTimeRank(distRank: Int, speedRank: Int): Int"],
    invs=["values at higher ranks are approximate guidelines"],
    x=500, y=380, w=400)

CharT = cls(R, "Character", imp="Character Construction",
    props=["+ traits: List<Trait>", "+ imposedConditions: ImposedConditions"],
    x=500, y=40, w=280)

edg(R, Trait, CharT, "association", ex=1.0, ey=0.2, nx=0.0, ny=0.5)
edg(R, Trait, Meas, "dependency", "\u00ABuses\u00BB", ex=0.75, ey=1.0, nx=0.3, ny=0.0)
edg(R, Meas, MT, "association", ex=0.0, ey=0.5, nx=1.0, ny=0.5)

# ===================================================================
#  PAGE 2 — CHECK
# ===================================================================
_, R = dt.add_page(mxfile, "Check", page_width=1800, page_height=1400)

TraitI = cls(R, "Trait", imp="Trait",
    props=["+ purchasedRank: Integer", "+ effectiveRank(): Integer"],
    x=40, y=40, w=260)

Check = cls(R, "Check", stereotype="\u00ABEntity\u00BB",
    props=["+ trait: Trait", "+ dc: DifficultyClass", "+ circumstanceModifier: Integer"],
    ops=["+ resolve(): CheckResult",
         "+ resolveGraded(): GradedCheckResult",
         "\u2212 rollD20(): Integer",
         "\u2212 computeDegree(margin: Int, isCrit: Bool, isSucc: Bool): Int"],
    invs=["shape: always rollTotal vs dc.value",
          "critical: raw d20 = 20 \u2192 +1 degree after normal calc"],
    x=400, y=40, w=380)

DC = cls(R, "DifficultyClass", stereotype="\u00ABValueObject\u00BB",
    props=["+ value: Integer"],
    invs=["0 \u2264 value \u2264 40 standard; higher for exceptional"],
    x=900, y=40, w=260)

CR = cls(R, "CheckResult", stereotype="\u00ABValueObject\u00BB",
    props=["+ rollTotal: Integer", "+ dc: DifficultyClass",
           "+ isSuccess: Boolean", "+ margin: Integer", "+ isCritical: Boolean"],
    invs=["isSuccess when rollTotal \u2265 dc.value",
          "isCritical only when raw d20 was exactly 20"],
    x=900, y=250, w=280)

GCR = cls(R, "GradedCheckResult", base="CheckResult", stereotype="\u00ABValueObject\u00BB",
    props=["+ degree: Integer", "+ resultingCondition: Condition"],
    invs=["degree 1\u20134; if isCritical, degree increased by one",
          "resultingCondition from effect\u2019s condition set"],
    x=900, y=490, w=300)

CondI = cls(R, "Condition", imp="Condition",
    props=["+ name: String", "+ gameModifier: GameModifier"],
    x=1280, y=490, w=260)

OC = cls(R, "OpposedCheck", base="Check", stereotype="\u00ABEntity\u00BB",
    props=["+ opponent: Character", "+ isPassive: Boolean"],
    ops=["+ resolve(): CheckResult",
         "\u2212 resolveTie(active: CheckResult, opposing: CheckResult): CheckResult"],
    invs=["passive: DC = opponent modifier + 10",
          "active: both roll, higher total wins",
          "tie: higher bonus wins; equal \u2192 d20"],
    x=40, y=700, w=380)

RC = cls(R, "RoutineCheck", base="Check", stereotype="\u00ABEntity\u00BB",
    ops=["+ resolve(): CheckResult"],
    invs=["substitutes 10 for d20; modifiers still apply",
          "if routine total < DC, caller may roll normally"],
    x=500, y=700, w=320)

TC = cls(R, "TeamCheck", base="Check", stereotype="\u00ABEntity\u00BB",
    props=["+ helpers: List<Character>"],
    ops=["+ resolve(): CheckResult",
         "\u2212 computeHelperModifier(): Integer"],
    invs=["1\u20132 helper successes \u2192 +2; 3+ \u2192 +5; failure \u2192 \u22122",
          "only leader\u2019s rollTotal determines outcome"],
    x=900, y=700, w=340)

CharC = cls(R, "Character", imp="Character Construction",
    props=["+ traits: List<Trait>", "+ imposedConditions: ImposedConditions"],
    ops=["+ traitMatching(other: Trait): Trait",
         "+ makeCheck(dc: DC, trait: Trait): CheckResult"],
    x=440, y=980, w=340)

# Edges — Check page
edg(R, Check, TraitI, "association", ex=0.0, ey=0.3, nx=1.0, ny=0.5)
edg(R, Check, DC, "association", ex=1.0, ey=0.2, nx=0.0, ny=0.5)
edg(R, Check, CR, "dependency", "\u00ABcreates\u00BB", ex=1.0, ey=0.7, nx=0.0, ny=0.3)
edg(R, GCR, CR, "inheritance", ex=0.5, ey=0.0, nx=0.5, ny=1.0)
edg(R, GCR, CondI, "association", ex=1.0, ey=0.5, nx=0.0, ny=0.5)
edg(R, OC, Check, "inheritance-orthogonal", ex=0.5, ey=0.0, nx=0.15, ny=1.0)
edg(R, RC, Check, "inheritance", ex=0.5, ey=0.0, nx=0.4, ny=1.0)
edg(R, TC, Check, "inheritance-orthogonal", ex=0.25, ey=0.0, nx=0.85, ny=1.0)
edg(R, OC, CharC, "association", "\u00ABopponent\u00BB", ex=0.5, ey=1.0, nx=0.0, ny=0.3)
edg(R, TC, CharC, "association", "\u00ABhelpers\u00BB", ex=0.5, ey=1.0, nx=1.0, ny=0.3)

# ===================================================================
#  PAGE 3 — CONDITION
# ===================================================================
_, R = dt.add_page(mxfile, "Condition", page_width=1600, page_height=1400)

CombCond = cls(R, "CombinedCondition", stereotype="\u00ABValueObject\u00BB",
    props=["+ name: String", "+ \u00ABcomposition\u00BB constituents: List<Condition>"],
    invs=["each constituent superseded/resolved independently"],
    x=40, y=40, w=320)

Cond = cls(R, "Condition", stereotype="\u00ABValueObject\u00BB",
    props=["+ name: String", "+ gameModifier: GameModifier",
           "+ supersedes: Condition", "+ supersededBy: Condition"],
    invs=["supersession chain navigable through Condition data"],
    x=440, y=40, w=300)

CSrc = cls(R, "ConditionSource", stereotype="\u00ABValueObject\u00BB",
    props=["+ identity: String"],
    invs=["shared identity \u2192 same-source supersession rules"],
    x=820, y=40, w=260)

GM = cls(R, "GameModifier", stereotype="\u00ABValueObject\u00BB",
    props=["+ appliesTo: String", "+ amount: Integer"],
    invs=["null appliesTo \u2192 applies to all checks",
          "negative = penalty; positive = bonus"],
    x=40, y=260, w=260)

IC = cls(R, "ImposedCondition", stereotype="\u00ABEntity\u00BB",
    props=["+ condition: Condition", "+ source: ConditionSource",
           "+ isActive: Boolean", "+ blockingCondition: ImposedCondition"],
    ops=["+ activate(): void", "+ deactivate(blocker: ImposedCondition): void"],
    invs=["only active imposed condition applies its modifier"],
    x=440, y=280, w=340)

TraitIC = cls(R, "Trait", imp="Trait",
    props=["+ traitName: String", "+ effectiveRank(): Integer"],
    x=40, y=490, w=260)

ICs = cls(R, "ImposedConditions", stereotype="\u00ABEntity\u00BB",
    props=[
        "+ \u00ABcomposition\u00BB appliedConditions: List<ImposedCondition>",
        "+ dyingSuccessCount: Integer",
        "+ dyingFailureCount: Integer"],
    ops=[
        "+ activeConditions(): List<ImposedCondition>",
        "+ applyCondition(cond: Condition, src: ConditionSource): void",
        "+ penaltyFor(trait: Trait): Integer",
        "+ revealBlockedConditions(removed: ImposedCondition): void",
        "+ remove(imposed: ImposedCondition): void",
        "+ recordDyingFortitudeResult(result: GradedCheckResult): String"],
    invs=["same-source more severe replaces; less severe ignored",
          "different-source more severe supersedes",
          "different-source less severe added inactive"],
    x=400, y=530, w=440)

CharCN = cls(R, "Character", imp="Character Construction",
    props=["+\u00ABcomposition\u00BB imposedConditions: ImposedConditions",
           "+ \u00ABcomposition\u00BB appliedEffects: List<AppliedEffect>"],
    x=40, y=820, w=300)

AE = cls(R, "AppliedEffect", stereotype="\u00ABEntity\u00BB",
    props=["+ effect: Effect", "+ character: Character",
           "+ isOngoing: Boolean",
           "+ \u00ABcomposition\u00BB imposedConditions: List<ImposedCondition>"],
    ops=["+ resist(defenseTrait: Trait): GradedCheckResult",
         "+ end(): void"],
    invs=["on resist success \u2192 ends; on failure \u2192 persists",
          "when ended, removes all imposed conditions it created"],
    x=420, y=860, w=380)

EffI = cls(R, "Effect", imp="Power",
    props=["+ name: String", "+ rank: Integer"],
    ops=["+ effectDc(): Integer", "+ conditionFor(degree: Int, isSuccess: Bool): Condition"],
    invs=["resistance check DC = 10 + rank"],
    x=880, y=860, w=340)

GCRI = cls(R, "GradedCheckResult", imp="Check",
    props=["+ degree: Integer", "+ resultingCondition: Condition"],
    x=880, y=1100, w=280)

# Edges — Condition page
edg(R, CombCond, Cond, "composition", ex=1.0, ey=0.5, nx=0.0, ny=0.3)
edg(R, Cond, GM, "composition", ex=0.0, ey=0.8, nx=1.0, ny=0.3)
edg(R, IC, Cond, "association", ex=0.3, ey=0.0, nx=0.5, ny=1.0)
edg(R, IC, CSrc, "association", ex=1.0, ey=0.2, nx=0.5, ny=1.0)
edg(R, ICs, IC, "composition", ex=0.5, ey=0.0, nx=0.5, ny=1.0)
edg(R, CharCN, ICs, "composition", ex=1.0, ey=0.3, nx=0.0, ny=0.3)
edg(R, CharCN, AE, "composition", ex=1.0, ey=0.7, nx=0.0, ny=0.3)
edg(R, AE, EffI, "association", ex=1.0, ey=0.3, nx=0.0, ny=0.5)
ae_ic = edg(R, AE, IC, "composition", ex=1.0, ey=0.1, nx=1.0, ny=0.7)
add_waypoints(ae_ic, [(870, 880), (870, 407)])
edg(R, AE, GCRI, "dependency", "\u00ABcreates\u00BB", ex=1.0, ey=0.8, nx=0.0, ny=0.5)
edg(R, ICs, TraitIC, "association", ex=0.0, ey=0.7, nx=1.0, ny=0.5)

# ---------------------------------------------------------------------------
# Save and audit
# ---------------------------------------------------------------------------
dt.save_drawio(PATH, mxfile)
report = dt.audit_diagram_report(PATH)
print(report)
sys.exit(0 if "ALL PAGES PASS" in report else 1)
