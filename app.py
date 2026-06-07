import streamlit as st
import plotly.graph_objects as go

from src.preprocess import clean_text
from src.preprocess import sentence_tokenization
from src.kmp import kmp_search
from src.rabin_karp import rabin_karp_search
from src.similarity import calculate_similarity


# PAGE CONFIG
st.set_page_config(
    page_title="Plagiarism Detection Engine",
    page_icon="🔍",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #020617
    );
    color: white;
}

/* HEADER */
.main-title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    background: linear-gradient(
        90deg,
        #00F5A0,
        #00D9F5
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from {
        opacity: 0.8;
    }
    to {
        opacity: 1;
    }
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

/* GLASS CARD */
.glass-card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.12);
    box-shadow:
        0 8px 32px rgba(0,0,0,0.3);
}

/* MATCH CARD */
.match-card {
    background: rgba(255,255,255,0.08);
    border-left: 5px solid #00F5A0;
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 20px;
    transition: 0.3s;
}

.match-card:hover {
    transform: scale(1.01);
}

/* STATS */
.metric-card {
    background: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    backdrop-filter: blur(15px);
}

/* FOOTER */
.footer {
    text-align: center;
    margin-top: 40px;
    color: gray;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    """
    <div class="main-title">
        🔍 Plagiarism Detection Engine
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Built with KMP • Rabin–Karp • String Matching Algorithms
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# ---------------- FILE UPLOAD ----------------
col1, col2 = st.columns(2)

with col1:
    original_file = st.file_uploader(
        "📄 Upload Original Document",
        type=["txt"]
    )

with col2:
    submitted_file = st.file_uploader(
        "📝 Upload Submitted Document",
        type=["txt"]
    )

st.write("")

if original_file and submitted_file:

    if st.button("🚀 Analyze Plagiarism"):

        with st.spinner(
            "Analyzing documents..."
        ):

            original_text = (
                original_file.read()
                .decode("utf-8")
            )

            submitted_text = (
                submitted_file.read()
                .decode("utf-8")
            )

            cleaned_original = clean_text(
                original_text
            )

            cleaned_submitted = clean_text(
                submitted_text
            )

            original_sentences = (
                sentence_tokenization(
                    cleaned_original
                )
            )

            submitted_sentences = (
                sentence_tokenization(
                    cleaned_submitted
                )
            )

            plagiarism_scores = []
            matched_results = []

            # Detection Logic
            for submitted in (
                submitted_sentences
            ):

                for original in (
                    original_sentences
                ):

                    similarity = (
                        calculate_similarity(
                            original,
                            submitted
                        )
                    )

                    if similarity >= 50:

                        pattern = " ".join(
                            submitted.split()[:2]
                        )

                        kmp_found = (
                            kmp_search(
                                original,
                                pattern
                            )
                        )

                        rk_found = (
                            rabin_karp_search(
                                original,
                                pattern
                            )
                        )

                        plagiarism_scores.append(
                            similarity
                        )

                        matched_results.append({
                            "original":
                            original,

                            "submitted":
                            submitted,

                            "similarity":
                            similarity,

                            "kmp":
                            kmp_found,

                            "rk":
                            rk_found
                        })

            # FINAL SCORE
            if plagiarism_scores:

                final_score = round(
                    sum(plagiarism_scores)
                    /
                    len(
                        plagiarism_scores
                    ),
                    2
                )

            else:
                final_score = 0

        st.divider()

        # ---------------- DASHBOARD ----------------
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class="metric-card">
            <h3>📊 Matches Found</h3>
            <h1>{len(matched_results)}</h1>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-card">
            <h3>🧠 Detection</h3>
            <h1>KMP + RK</h1>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            risk = (
                "High"
                if final_score > 70
                else "Medium"
            )

            st.markdown(f"""
            <div class="metric-card">
            <h3>⚠ Risk</h3>
            <h1>{risk}</h1>
            </div>
            """, unsafe_allow_html=True)

        st.write("")

        # ---------------- CIRCULAR SCORE ----------------
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=final_score,
            title={
                'text':
                "Plagiarism Score"
            },
            gauge={
                'axis': {
                    'range':
                    [0, 100]
                }
            }
        ))

        fig.update_layout(
            height=400
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        st.subheader(
            "📌 Matched Content"
        )

        # ---------------- MATCH CARDS ----------------
        for result in matched_results:

            st.markdown(
                f"""
                <div class="match-card">

                <h3>
                ✅ Match Found
                </h3>

                <b>Original:</b>
                <br>
                {result['original']}

                <br><br>

                <b>Submitted:</b>
                <br>
                {result['submitted']}

                <br><br>

                <b>Similarity:</b>
                {result['similarity']}%

                <br><br>

                <span style="color:#22c55e">
                ✅ KMP Detected
                </span>

                <br>

                <span style="color:#38bdf8">
                🔵 Rabin–Karp Verified
                </span>

                </div>
                """,
                unsafe_allow_html=True
            )

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
Built with ❤️ using Python, Streamlit,
KMP & Rabin–Karp Algorithms
</div>
""", unsafe_allow_html=True)