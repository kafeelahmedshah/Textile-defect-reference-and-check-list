import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Textile Defect Reference & Checklist",
    page_icon="🧵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- DATA --------------------
DEFECTS = [
    {
        "name": "Slub",
        "category": "Yarn / Appearance",
        "description": "A thick or irregular place in the yarn that appears as an unwanted thick spot in the fabric.",
        "causes": [
            "Irregularity in yarn formation",
            "Poor fiber mixing or uneven fiber distribution",
            "Improper drafting or spinning conditions"
        ],
        "remedies": [
            "Check yarn quality before weaving or knitting",
            "Inspect drafting and spinning settings",
            "Remove or segregate fabric sections with unacceptable slubs"
        ],
        "inspection": "Look for an unwanted thick place or lump that interrupts the normal fabric appearance."
    },
    {
        "name": "Missing Pick",
        "category": "Weaving",
        "description": "A defect in woven fabric where a weft pick is absent from a portion or across the fabric width.",
        "causes": [
            "Weft yarn breakage",
            "Weft insertion or loom stopping problem",
            "Incorrect loom setting or poor machine monitoring"
        ],
        "remedies": [
            "Check the weft insertion system and yarn path",
            "Repair the missing pick where the fabric construction allows",
            "Inspect loom operation and fabric regularly"
        ],
        "inspection": "Check the weft direction for a visible gap or missing yarn line."
    },
    {
        "name": "Hole",
        "category": "Fabric Damage",
        "description": "An opening in the fabric caused by broken, damaged, or missing yarns.",
        "causes": [
            "Mechanical damage during processing",
            "Sharp or rough machine parts",
            "Excessive tension or mishandling"
        ],
        "remedies": [
            "Identify and remove the source of mechanical damage",
            "Check machine surfaces and fabric guiding parts",
            "Repair, mend, or reject the affected area according to quality standards"
        ],
        "inspection": "Examine the fabric surface for an opening or broken yarns."
    },
    {
        "name": "Oil Stain",
        "category": "Stain / Appearance",
        "description": "An unwanted oily mark on the fabric surface that may affect appearance and later processing.",
        "causes": [
            "Oil leakage from machinery",
            "Contact with lubricated machine parts",
            "Improper handling or contaminated surfaces"
        ],
        "remedies": [
            "Locate and stop the oil leakage",
            "Clean machine surfaces and prevent further contact",
            "Use an approved stain-removal process after checking fabric compatibility"
        ],
        "inspection": "Look for dark, greasy, or translucent marks on the fabric."
    }
]

# Additional common reference entries
DEFECTS += [
    {
        "name": "Broken End",
        "category": "Weaving",
        "description": "A warp yarn is broken, creating a visible line or weakness in the fabric.",
        "causes": ["High warp tension", "Weak or poor-quality yarn", "Improper loom settings"],
        "remedies": ["Check warp tension", "Use suitable yarn quality", "Repair the broken end and inspect loom settings"],
        "inspection": "Follow the warp direction and look for a broken or absent yarn."
    },
    {
        "name": "Weft Bar",
        "category": "Weaving",
        "description": "A visible horizontal band caused by a difference in weft yarn or weft-related conditions.",
        "causes": ["Change in weft yarn properties", "Different yarn lot or shade", "Variation in machine or process conditions"],
        "remedies": ["Maintain consistent weft yarn lots", "Check yarn count and shade", "Review machine settings and batch records"],
        "inspection": "Look for a horizontal band across the fabric width."
    },
    {
        "name": "Uneven Dyeing",
        "category": "Dyeing",
        "description": "A non-uniform shade or colour appearance across the fabric.",
        "causes": ["Uneven chemical or dye distribution", "Incorrect process conditions", "Poor preparation or circulation"],
        "remedies": ["Check dye and chemical dosing", "Maintain uniform circulation and process conditions", "Review pretreatment and dyeing records"],
        "inspection": "Compare shade across the width and length under suitable lighting."
    },
    {
        "name": "Crease Mark",
        "category": "Finishing",
        "description": "A visible line or mark formed when fabric is folded or creased during wet processing or finishing.",
        "causes": ["Fabric folding during processing", "Poor fabric movement", "Incorrect machine loading or process conditions"],
        "remedies": ["Improve fabric movement and loading", "Check machine operation", "Use an approved corrective finishing process if suitable"],
        "inspection": "Look for a persistent line or fold mark on the fabric."
    }
]

# -------------------- STYLING --------------------
st.markdown("""
<style>
    .main-header {
        padding: 1.35rem 1.5rem;
        border-radius: 16px;
        background: linear-gradient(115deg, #123b56, #167c80);
        color: white;
        margin-bottom: 1.2rem;
    }
    .main-header h1 { color: white; margin: 0; font-size: 2rem; }
    .main-header p { color: #e6f5f5; margin: .45rem 0 0 0; }
    .info-card {
        padding: 1rem;
        border: 1px solid rgba(120,140,150,.35);
        border-radius: 12px;
        min-height: 110px;
    }
    .small-muted { color: #718096; font-size: .9rem; }
</style>
""", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------
st.sidebar.title("🧵 Textile Defect App")
st.sidebar.caption("Reference • Causes • Remedies • Inspection")
page = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Defect Reference", "Inspection Checklist", "About Project"]
)
st.sidebar.divider()
st.sidebar.markdown("**Project Details**")
st.sidebar.write("Roll No: 25TE052")
st.sidebar.write("Department: Textile Engineering")

# -------------------- HEADER --------------------
st.markdown("""
<div class="main-header">
    <h1>Textile Defect Reference & Checklist</h1>
    <p>A practical reference tool for identifying common fabric defects, understanding their causes, and reviewing corrective actions.</p>
</div>
""", unsafe_allow_html=True)

if page == "Dashboard":
    c1, c2, c3 = st.columns(3)
    c1.metric("Defects in Reference", len(DEFECTS))
    c2.metric("Main Assigned Defects", "4")
    c3.metric("Inspection Tool", "Checklist")

    st.subheader("Assigned Defects")
    cols = st.columns(4)
    for col, name in zip(cols, ["Slub", "Missing Pick", "Hole", "Oil Stain"]):
        item = next(d for d in DEFECTS if d["name"] == name)
        with col:
            st.markdown(f'<div class="info-card"><h3>{item["name"]}</h3><p class="small-muted">{item["category"]}</p>{item["description"]}</div>', unsafe_allow_html=True)

    st.subheader("How to use this application")
    st.markdown("""
    1. Open **Defect Reference** to search for a fabric defect.
    2. Select a defect to read its description, possible causes, inspection points, and remedies.
    3. Open **Inspection Checklist** while checking a fabric sample.
    4. Record the result and download the checklist as a CSV file.
    """)
    st.info("Note: Causes and remedies are general educational guidance. Actual corrective action should be confirmed with the relevant production and quality-control team.")

elif page == "Defect Reference":
    st.subheader("Search Defects")
    search = st.text_input("Search by defect name, category, cause, or keyword", placeholder="Example: slub, weaving, oil...")
    categories = ["All"] + sorted(set(d["category"] for d in DEFECTS))
    selected_category = st.selectbox("Filter by category", categories)

    filtered = []
    for d in DEFECTS:
        searchable = " ".join([d["name"], d["category"], d["description"], " ".join(d["causes"]), " ".join(d["remedies"])]).lower()
        matches_search = search.lower().strip() in searchable
        matches_category = selected_category == "All" or d["category"] == selected_category
        if matches_search and matches_category:
            filtered.append(d)

    st.caption(f"{len(filtered)} matching defect(s)")
    if not filtered:
        st.warning("No matching defect found. Try another keyword or category.")
    else:
        for d in filtered:
            with st.expander(f'{d["name"]}  ·  {d["category"]}', expanded=(len(filtered) == 1)):
                st.write(d["description"])
                left, right = st.columns(2)
                with left:
                    st.markdown("**Possible causes**")
                    for cause in d["causes"]:
                        st.markdown(f"- {cause}")
                with right:
                    st.markdown("**Simple remedies**")
                    for remedy in d["remedies"]:
                        st.markdown(f"- {remedy}")
                st.markdown("**Inspection point**")
                st.info(d["inspection"])

elif page == "Inspection Checklist":
    st.subheader("Fabric Inspection Checklist")
    st.write("Select the defects observed in your fabric sample and record their inspection status.")
    sample_id = st.text_input("Sample / Roll ID", placeholder="Enter sample or roll number")
    inspector = st.text_input("Inspector name (optional)")
    date = st.date_input("Inspection date")
    st.divider()

    checklist_rows = []
    for d in DEFECTS:
        with st.container():
            col1, col2, col3 = st.columns([2, 2, 3])
            with col1:
                st.markdown(f"**{d['name']}**")
                st.caption(d["category"])
            with col2:
                status = st.selectbox(
                    "Status",
                    ["Not checked", "Not found", "Found"],
                    key=f"status_{d['name']}",
                    label_visibility="collapsed"
                )
            with col3:
                note = st.text_input(
                    "Observation / location",
                    key=f"note_{d['name']}",
                    placeholder="Optional note",
                    label_visibility="collapsed"
                )
            checklist_rows.append({
                "Sample / Roll ID": sample_id,
                "Inspector": inspector,
                "Inspection Date": str(date),
                "Defect": d["name"],
                "Category": d["category"],
                "Status": status,
                "Observation / Location": note
            })

    df = pd.DataFrame(checklist_rows)
    found_count = sum(1 for row in checklist_rows if row["Status"] == "Found")
    checked_count = sum(1 for row in checklist_rows if row["Status"] != "Not checked")
    a, b = st.columns(2)
    a.metric("Defects marked Found", found_count)
    b.metric("Items checked", f"{checked_count}/{len(DEFECTS)}")

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "⬇️ Download Inspection Checklist (CSV)",
        data=csv,
        file_name=f"textile_inspection_{sample_id or 'sample'}.csv",
        mime="text/csv",
        use_container_width=True
    )
    st.caption("The checklist is downloaded to your device. This basic version does not store inspection records online.")

else:
    st.subheader("About This Project")
    st.write("**Application:** Textile Defect Reference & Checklist App")
    st.write("**Student Roll No:** 25TE052")
    st.write("**Department:** Textile Engineering")
    st.write("**Platform:** Python and Streamlit")
    st.markdown("""
    **Project objective**

    To provide a searchable educational guide to common textile fabric defects, including their descriptions, possible causes, and simple remedies. The checklist helps users record observations during basic fabric inspection.

    **Included assigned defects**
    - Slub
    - Missing Pick
    - Hole
    - Oil Stain

    **Technology used**
    - Python
    - Streamlit
    - Pandas
    """)
    st.warning("This application is an educational reference. Final fabric acceptance or rejection must follow the applicable inspection standard and the organization's quality procedures.")

st.divider()
st.caption("Textile Defect Reference & Checklist App | Roll No. 25TE052 | Textile Engineering")
